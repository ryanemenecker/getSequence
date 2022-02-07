"""
Unit and regression test for the getSequence package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import getSequence


def test_getSequence_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "getSequence" in sys.modules
