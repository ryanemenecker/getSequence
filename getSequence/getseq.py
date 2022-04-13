##
## getseq.py
## 
## getseq.py contains all the user-facing function associated with getSequence. If a new function is added it should be included
## here and added to the __all__ list
## 

##Handles the primary functions

# NOTE - any new functions must be added to this list!
__all__ =  ['getseq']
 
import os
import sys
import urllib3

from getSequence.get_sequence import seq_from_name as _seq_from_name
from getSequence.get_sequence import fetch_sequence as _fetch_sequence
from getSequence.getsequence_exceptions import RetreiveSequenceError

def getseq(name, just_sequence=False):
	'''
	function to get the sequence from uniprot.

	Parameters
	-----------
	name : String
		The name of the protein as a string.

	just_sequence : bool
	 	Whether to return just the sequence.


	Returns
	-------
	By default, returns a list where:
		[0] = full Uniprot ID
		[1] = Protein sequence
		[2] = Just the Uniprot ID
	'''

	try:
		fullID_seq_name = _seq_from_name(name)
		if just_sequence == True:
			return fullID_seq_name[1]
		else:
			return fullID_seq_name
	except:
		if just_sequence == False:
			return _fetch_sequence(name, return_full_id=True)
		else:
			return _fetch_sequence(name)		







