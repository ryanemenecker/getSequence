getSequence
==============================

A tool to get a uniprot sequence returned to terminal or from within Python.

## What is getSequence?

getSequence is a command-line interface for printing protein sequences from Uniprot to your terminal. I made this because I was tired of having to navigate to the website, copy a sequence, and format it. It also has functionality to use in Python.

## How does it work?

getSequence will take in your name and query Uniprot. It then takes the top hit from Uniprot and gets the sequence information. You can specify multiple things from the command-line or form Python, exactly how you would if you were to use the search box on the Uniprot website.

## This seems kind of unnecessary...

Fair enough. I still think it's nifty.

# Installation

**getSequence** in availbale through PyPi - to install just run...

	$ pip install getsequence


Alternatively, you can get **getSequence** directly from GitHub. 

To clone the GitHub repository and gain the ability to modify a local copy of the code, run

	$ git clone https://github.com/ryanemenecker/getSequence.git
	$ cd getSequence
	$ pip install .

This will install **getSequence** locally.

# Usage:

There are two ways you can use metapredict:
1. Directly from the command-line
2. From within Python

## Using getSequence from the command-line:

The primary intended usage of getSequence is from the command-line. To use getSequence from the command-line, simply use the ``getseq`` command followed by the name of your protein. The name of your protein can be just the protein name, the name and organism, or the Uniprot ID. 

**Example**

	$ getseq p53

would return

	>Homo_sapiens_p53_P04637
	MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGPDEAPRMPEAAPPVAPAPAAPTPAAPAPAPSWPLSSSVPSQKTYQGSYGFRLGFLHSGTAKSVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHERCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKGEPHHELPPGSTKRALPNNTSSSPQPKKKPLDGEYFTLQIRGRERFEMFRELNEALELKDAQAGKEPGGSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD

By default getSequence will return the sequence as a FASTA formatted sequence where the first line is the name of the protein as well as the organism it is from and finally the actual Uniprot ID. This is because just typing in something like p53 doesn't gaurentee you will get the p53 you want. If you had wanted the mouse p53 in the previous example, you would have gotten the incorrect sequence. However, you can add more details like the following example:

**Example**

	$ getseq p53 mouse

would return

	>Mus_musculus_P53_P02340
	MTAMEESQSDISLELPLSQETFSGLWKLLPPEDILPSPHCMDDLLLPQDVEEFFEGPSEALRVSGAPAAQDPVTETPGPVAPAPATPWPLSSFVPSQKTYQGNYGFHLGFLQSGTAKSVMCTYSPPLNKLFCQLAKTCPVQLWVSATPPAGSRVRAMAIYKKSQHMTEVVRRCPHHERCSDGDGLAPPQHLIRVEGNLYPEYLEDRQTFRHSVVVPYEPPEAGSEYTTIHYKYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRDSFEVRVCACPGRDRRTEEENFRKKEVLCPELPPGSAKRALPTCTSASPPQKKKPLDGEYFTLKIRGRKRFEMFRELNEALELKDAHATEESGDSRAHSSYLKTKKGQSTSRHKKTMVKKVGPDSD


**Additional Usage**

**Printing the full Uniprot ID-**

If you want to print the full uniprot ID rather than the shortened default one, use the ``-v`` or ``--verbose`` flag.

**Example**

	$ getseq p53 mouse -v

would return

	>sp|P02340|P53_MOUSE Cellular tumor antigen p53 OS=Mus musculus OX=10090 GN=Tp53 PE=1 SV=4
	MTAMEESQSDISLELPLSQETFSGLWKLLPPEDILPSPHCMDDLLLPQDVEEFFEGPSEALRVSGAPAAQDPVTETPGPVAPAPATPWPLSSFVPSQKTYQGNYGFHLGFLQSGTAKSVMCTYSPPLNKLFCQLAKTCPVQLWVSATPPAGSRVRAMAIYKKSQHMTEVVRRCPHHERCSDGDGLAPPQHLIRVEGNLYPEYLEDRQTFRHSVVVPYEPPEAGSEYTTIHYKYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRDSFEVRVCACPGRDRRTEEENFRKKEVLCPELPPGSAKRALPTCTSASPPQKKKPLDGEYFTLKIRGRKRFEMFRELNEALELKDAHATEESGDSRAHSSYLKTKKGQSTSRHKKTMVKKVGPDSD

**Just printing the sequence-**

If you just want to print the sequence, use the ``-s`` or ``--silent`` flag. WARNING: If you do this, you will not know if you got the exact sequence that you want! The reason the Uniprot ID, organism, and protein name are printed back to you is to help you check that you got the protien that you want!

**Example**

	$ getseq p53 mouse -s

would return

	MTAMEESQSDISLELPLSQETFSGLWKLLPPEDILPSPHCMDDLLLPQDVEEFFEGPSEALRVSGAPAAQDPVTETPGPVAPAPATPWPLSSFVPSQKTYQGNYGFHLGFLQSGTAKSVMCTYSPPLNKLFCQLAKTCPVQLWVSATPPAGSRVRAMAIYKKSQHMTEVVRRCPHHERCSDGDGLAPPQHLIRVEGNLYPEYLEDRQTFRHSVVVPYEPPEAGSEYTTIHYKYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRDSFEVRVCACPGRDRRTEEENFRKKEVLCPELPPGSAKRALPTCTSASPPQKKKPLDGEYFTLKIRGRKRFEMFRELNEALELKDAHATEESGDSRAHSSYLKTKKGQSTSRHKKTMVKKVGPDSD

## Using getSequence from the Python:

getSequence has one function in Python called ``getseq``. To use it, Firt you need to import getseq. To do so, simply input-

	from getSequence import getseq

Now you can use getseq.

By default, the getseq function returns a list is returned where the first element is the full Uniprot ID, the second is the protein sequence, and the third is teh short Uniprot ID. 

**Example**

	getseq('p53')
	['>sp|P04637|P53_HUMAN Cellular tumor antigen p53 OS=Homo sapiens OX=9606 GN=TP53 PE=1 SV=4', 'MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGPDEAPRMPEAAPPVAPAPAAPTPAAPAPAPSWPLSSSVPSQKTYQGSYGFRLGFLHSGTAKSVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHERCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKGEPHHELPPGSTKRALPNNTSSSPQPKKKPLDGEYFTLQIRGRERFEMFRELNEALELKDAQAGKEPGGSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD', 'P04637']


**Additional Usage**

**Just return the sequence**

To just return the protein sequence as a string, set ``just_sequence=True``

**Example**

	getseq('p53', just_sequence=True)
	'MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGPDEAPRMPEAAPPVAPAPAAPTPAAPAPAPSWPLSSSVPSQKTYQGSYGFRLGFLHSGTAKSVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHERCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKGEPHHELPPGSTKRALPNNTSSSPQPKKKPLDGEYFTLQIRGRERFEMFRELNEALELKDAQAGKEPGGSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD'


### Copyright

Copyright (c) 2022, Ryan Emenecker


#### Acknowledgements
 
Project based on the 
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.6.
