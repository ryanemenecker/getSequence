##
## getseq.py
## 
## getseq.py contains all the user-facing function associated with getSequence. 
## If a new function is added it should be included
## here and added to the __all__ list
## 

'''
Note:
Some of the way getseq is written seems a bit redundant (see get_sequence.py). 
This is because getseq was originally made primarily for use
in other packages that I have. Some of the ways this is implemented
is rather particular, which has constrained how I update the code
in getseq. It's honestly easier to have some redundancy here
than to fix all the bugs I would inevitably introduce in all my
other packages that use getseq by updating and refactoring this code. 
'''

## Handles the primary functions

# NOTE - any new functions must be added to this list!
__all__ =  ['getseq']
 
## main imports 
import os
import sys
import urllib3
import protfasta

## internal imports
from getSequence.get_sequence import getseq_from_string as _getseq_from_string
from getSequence.get_sequence import get_seqs_from_list as _get_seqs_from_list
from getSequence.getsequence_exceptions import RetreiveSequenceError


def getseq(query, uniprot_id=False, just_sequence=False,
    return_dict=False, ignore_failures=False, output_file=None):
    '''
    User facing functionality to get sequences. 

    Parameters
    ----------
    query : str or list
        A single query to search for as a string or
        a list of queries to search for.
    uniprot_id : bool
        Whether or not to use the uniprot id.
    just_sequence : bool
        Whether or not to just return the sequence.
    return_dict : bool
        Whether or not to return a dictionary.
    ignore_failures : bool
        Whether or not to ignore failures.
    output_file : str
        The output file to write the sequences to.

    Returns
    -------
    list or dict
        If output_file is None,
            by default returns a nested list where the first element 
            in each list is the uniprot header and the second is the sequence. 
            If return_dict is True, returns a dictionary where the keys are the 
            uniprot headers and the values are the sequences.
        If output_file is not None,
            None. Just saves the output. 

    '''
    # check output_file
    if output_file is not None:
        # set return_dict to True. Makes it easier to use protfasta. 
        return_dict=True
        # get the path and file
        path = os.path.dirname(output_file)
        file = os.path.basename(output_file)
        if os.path.exists(path)==False:
            raise Exception(f'Path {path} does not exist.')        
    
    # check if we have a list
    if isinstance(query, list):
        # get sequences from list
        values= _get_seqs_from_list(query, uniprot_id=uniprot_id, 
            just_sequence=just_sequence, return_dict=return_dict, 
            ignore_failures=ignore_failures)
        if output_file is not None:
           protfasta.write_fasta(values, output_file)
        else:
           return values
    elif isinstance(query, str):
        # set blank val for values
        values=''
        # get sequence from string
        if ignore_failures==False:
            values = _getseq_from_string(query, uniprot_id=uniprot_id, 
                just_sequence=just_sequence, return_dict=return_dict)            
        else:
            try:
                values = _getseq_from_string(query, uniprot_id=uniprot_id, 
                    just_sequence=just_sequence, return_dict=return_dict)
            except:
                print(f'Unable to retrieve sequence for {query}')
        # write out if needed.
        if values !=  '':
            if output_file is not None:
                protfasta.write_fasta(values, output_file)
            else:
                return values
    else:
        raise Exception('Query must be a string or a list of strings')
