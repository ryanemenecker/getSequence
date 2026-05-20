"""
Unit and regression test for the getSequence package.
"""

# Import package, test suite, and other packages as needed
import sys
import importlib

import pytest

import getSequence
from getSequence.getsequence_exceptions import RetreiveSequenceError


def test_getSequence_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "getSequence" in sys.modules


def test_getseq_writes_to_current_directory(monkeypatch, tmp_path):
    getseq_module = importlib.import_module("getSequence.getseq")
    written = {}

    def fake_getseq_from_string(*args, **kwargs):
        assert kwargs["just_sequence"] is False
        return {"sp|test|protein": "MSEQ"}

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(getseq_module, "_getseq_from_string", fake_getseq_from_string)
    monkeypatch.setattr(
        getseq_module.protfasta,
        "write_fasta",
        lambda values, output_file: written.update(
            {"values": values, "output_file": output_file}
        ),
    )

    getseq_module.getseq("protein", just_sequence=True, output_file="protein.fasta")

    assert written == {"values": {"sp|test|protein": "MSEQ"}, "output_file": "protein.fasta"}


def test_get_seqs_from_list_keeps_order_and_ignores_failures(monkeypatch):
    sequence_module = importlib.import_module("getSequence.get_sequence")

    def fake_getseq_from_string(query, **kwargs):
        if query == "bad query":
            raise RetreiveSequenceError("no sequence")
        return {f"header-{query}": f"sequence-{query}"}

    monkeypatch.setattr(sequence_module, "getseq_from_string", fake_getseq_from_string)

    values = sequence_module.get_seqs_from_list(
        ["first", "bad query", "second"], ignore_failures=True, max_workers=3
    )

    assert values == [["header-first", "sequence-first"], ["header-second", "sequence-second"]]


def test_batch_getseq_uses_list_query_path(monkeypatch):
    getseq_module = importlib.import_module("getSequence.getseq")
    observed = {}

    def fake_getseq(query, max_workers=None, **kwargs):
        observed["query"] = query
        observed["max_workers"] = max_workers
        observed["kwargs"] = kwargs
        return [["header-first", "sequence-first"], ["header-second", "sequence-second"]]

    monkeypatch.setattr(getseq_module, "getseq", fake_getseq)

    assert getseq_module.batch_getseq(("first", "second"), max_workers=2) == [
        ["header-first", "sequence-first"],
        ["header-second", "sequence-second"],
    ]
    assert observed == {
        "query": ["first", "second"],
        "max_workers": 2,
        "kwargs": {},
    }


def test_normalize_max_workers_validates_positive_integer():
    sequence_module = importlib.import_module("getSequence.get_sequence")

    assert sequence_module._normalize_max_workers(None, 100) == 32
    assert sequence_module._normalize_max_workers(4, 2) == 2
    with pytest.raises(ValueError):
        sequence_module._normalize_max_workers(0, 2)
