Using getSequence from the command-line:
----------------------------------------

The primary intended usage of getSequence is from the command-line. To use getSequence from the command-line, simply use the ``getseq`` command followed by the name of your protein. The name of your protein can be just the protein name, the name and organism, or the Uniprot ID. 

**Example**

.. code-block:: bash
	
	$ getseq p53

would return

.. code-block:: bash
	
	>Homo_sapiens_p53_P04637
	MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGPDEAPRMPEAAPPVAPAPAAPTPAAPAPAPSWPLSSSVPSQKTYQGSYGFRLGFLHSGTAKSVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHERCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKGEPHHELPPGSTKRALPNNTSSSPQPKKKPLDGEYFTLQIRGRERFEMFRELNEALELKDAQAGKEPGGSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD

By default getSequence will return the sequence as a FASTA formatted sequence where the first line is the name of the protein as well as the organism it is from and finally the actual Uniprot ID. This is because just typing in something like p53 doesn't gaurentee you will get the p53 you want. If you had wanted the mouse p53 in the previous example, you would have gotten the incorrect sequence. However, you can add more details like the following example:

**Example**

.. code-block:: bash
	
	$ getseq p53 mouse

would return

.. code-block:: bash
	
	>Mus_musculus_P53_P02340
	MTAMEESQSDISLELPLSQETFSGLWKLLPPEDILPSPHCMDDLLLPQDVEEFFEGPSEALRVSGAPAAQDPVTETPGPVAPAPATPWPLSSFVPSQKTYQGNYGFHLGFLQSGTAKSVMCTYSPPLNKLFCQLAKTCPVQLWVSATPPAGSRVRAMAIYKKSQHMTEVVRRCPHHERCSDGDGLAPPQHLIRVEGNLYPEYLEDRQTFRHSVVVPYEPPEAGSEYTTIHYKYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRDSFEVRVCACPGRDRRTEEENFRKKEVLCPELPPGSAKRALPTCTSASPPQKKKPLDGEYFTLKIRGRKRFEMFRELNEALELKDAHATEESGDSRAHSSYLKTKKGQSTSRHKKTMVKKVGPDSD


**Additional Usage**

**Printing the full Uniprot ID-**

If you want to print the full uniprot ID rather than the shortened default one, use the ``-v`` or ``--verbose`` flag.

**Example**

.. code-block:: bash
	
	$ getseq p53 mouse -v

would return

.. code-block:: bash
	
	>sp|P02340|P53_MOUSE Cellular tumor antigen p53 OS=Mus musculus OX=10090 GN=Tp53 PE=1 SV=4
	MTAMEESQSDISLELPLSQETFSGLWKLLPPEDILPSPHCMDDLLLPQDVEEFFEGPSEALRVSGAPAAQDPVTETPGPVAPAPATPWPLSSFVPSQKTYQGNYGFHLGFLQSGTAKSVMCTYSPPLNKLFCQLAKTCPVQLWVSATPPAGSRVRAMAIYKKSQHMTEVVRRCPHHERCSDGDGLAPPQHLIRVEGNLYPEYLEDRQTFRHSVVVPYEPPEAGSEYTTIHYKYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRDSFEVRVCACPGRDRRTEEENFRKKEVLCPELPPGSAKRALPTCTSASPPQKKKPLDGEYFTLKIRGRKRFEMFRELNEALELKDAHATEESGDSRAHSSYLKTKKGQSTSRHKKTMVKKVGPDSD

**Just printing the sequence-**

If you just want to print the sequence, use the ``-s`` or ``--silent`` flag. WARNING: If you do this, you will not know if you got the exact sequence that you want! The reason the Uniprot ID, organism, and protein name are printed back to you is to help you check that you got the protien that you want!

**Example**

.. code-block:: bash
	
	$ getseq p53 mouse -s

would return

.. code-block:: bash
	
	MTAMEESQSDISLELPLSQETFSGLWKLLPPEDILPSPHCMDDLLLPQDVEEFFEGPSEALRVSGAPAAQDPVTETPGPVAPAPATPWPLSSFVPSQKTYQGNYGFHLGFLQSGTAKSVMCTYSPPLNKLFCQLAKTCPVQLWVSATPPAGSRVRAMAIYKKSQHMTEVVRRCPHHERCSDGDGLAPPQHLIRVEGNLYPEYLEDRQTFRHSVVVPYEPPEAGSEYTTIHYKYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRDSFEVRVCACPGRDRRTEEENFRKKEVLCPELPPGSAKRALPTCTSASPPQKKKPLDGEYFTLKIRGRKRFEMFRELNEALELKDAHATEESGDSRAHSSYLKTKKGQSTSRHKKTMVKKVGPDSD