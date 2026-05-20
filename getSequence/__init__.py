"""A CLI to get a uniprot sequence returned to terminal"""

from importlib.metadata import PackageNotFoundError, version

# Add imports here
from getSequence.getseq import getseq, batch_getseq


# Handle version
try:
	__version__ = version("getSequence")
except PackageNotFoundError:
	from ._version import __version__
