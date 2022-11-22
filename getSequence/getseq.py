##
## getseq.py
## 
## getseq.py contains all the user-facing function associated with getSequence. If a new function is added it should be included
## here and added to the __all__ list
## 

##Handles the primary functions

# NOTE - any new functions must be added to this list!
__all__ =  ['getseq', 'visseq']
 
import os
import sys
import urllib3

from getSequence.get_sequence import seq_from_uniprot as _seq_from_uniprot
from getSequence.vis_sequence import visualize_sequence as _visualize_sequence
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
	'''

	try:
		fullID_seq_name = _seq_from_uniprot(name)
		if just_sequence == True:
			return fullID_seq_name[1]
		else:
			return fullID_seq_name
	except:
		raise RetreiveSequenceError('Unable to retrieve sequence.')
	


def visseq(name, show_patterning=['Q']):
	'''
	function to get the sequence from uniprot.

	Parameters
	-----------
	name : String
		The name of the protein as a string.

	show_patterning : list
	 	list of up to 5 residues to show patterning for


	Returns
	-------
	shows a graph immediately
	'''
	try:
		fullID_seq_name = _seq_from_uniprot(name)
	except:
		raise RetreiveSequenceError('Unable to retrieve sequence.')	
	seq_name = fullID_seq_name[0]
	sequence = fullID_seq_name[1]
	_visualize_sequence(sequence, show_patterning=show_patterning)



