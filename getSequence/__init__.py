"""A CLI to get a uniprot sequence returned to terminal"""

# Add imports here
from .getseq import getseq as getseq

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
