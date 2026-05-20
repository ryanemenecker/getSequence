getSequence
==============================

A tool to get a protein sequences from Uniprot using a CLI or in Python.
  
V3.0 was a significant update released on May 20, 2026. This update keeps the existing CLI and Python return formats the same while making batch sequence retrieval much faster and more reliable. Multiple queries now use threads, which fits the network-bound UniProt requests better than process-based multiprocessing. Batch calls preserve input order and can be tuned with ``max_workers`` in Python or ``--max-workers`` on the command line.

# What is getSequence?

getSequence is a Python package and command-line interface for getting protein sequences from Uniprot. If you have a list of protein names or Uniprot IDs, you can now fetch them from Uniprot either directly from the command-line or in Python. 

## How does it work?

getSequence will take in your protein name *including organism name if you'd like* or a Uniprot ID and query Uniprot. It then takes the top hit from Uniprot and gets the sequence information. You can specify multiple things from the command-line or from Python, exactly how you would if you were to use the search box on the Uniprot website. It's pretty nifty. 

# Installation

**getSequence** in availbale through PyPi - to install just run...
```bash
pip install getSequence
```

Alternatively, you can get **getSequence** directly from GitHub. 

To clone the GitHub repository and gain the ability to modify a local copy of the code, run
```bash
git clone https://github.com/ryanemenecker/getSequence.git
```
```bash
cd getSequence
```
```bash
pip install .
```
This will install **getSequence** locally.

# Usage:

There are two ways you can use getSequence:
1. Directly from the command-line
2. From within Python

## Using getSequence from the command-line:

To use getSequence from the command-line, simply use the ``getseq`` command followed by the name of your protein. The name of your protein can be just the protein name, the name and organism, or the Uniprot ID. If you use the Uniprot ID, it is recommended that you use the ``-u`` flag to let getseq know that you're inputting a Uniprot ID. 

### Getting single sequences
  
By default, getseq will just print your sequence to the terminal. However you can also save the output (more on that later). 

**Example**
```bash
getseq p53 mouse
>sp|p02340|p53 mouse cellular tumor antigen p53 os=mus musculus ox=10090 gn=tp53 pe=1 sv=4
MTAMEESQSDISLELPLSQETFSGLWKLLPPEDILPSPHCMDDLLLPQDVEEFFEGPSEALRVSGAPAAQDPVTETPGPVAPAPATPWPLSSFVPSQKTYQGNYGFHLGFLQSGTAKSVMCTYSPPLNKLFCQLAKTCPVQLWVSATPPAGSRVRAMAIYKKSQHMTEVVRRCPHHERCSDGDGLAPPQHLIRVEGNLYPEYLEDRQTFRHSVVVPYEPPEAGSEYTTIHYKYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRDSFEVRVCACPGRDRRTEEENFRKKEVLCPELPPGSAKRALPTCTSASPPQKKKPLDGEYFTLKIRGRKRFEMFRELNEALELKDAHATEESGDSRAHSSYLKTKKGQSTSRHKKTMVKKVGPDSD
```

### Getting multiple sequences
  
You can also get multiple sequences using a single command by separating your queries by commas. **Multiple entries must be comma separated**.

Multiple command-line queries are fetched in parallel. By default, getSequence uses up to 32 workers and caps that number at the number of queries. You can tune this with ``--max-workers`` if you want fewer simultaneous UniProt requests.

**Example**
```bash
getseq mouse p53, human p53, dog p53
>sp|p02340|p53 mouse cellular tumor antigen p53 os=mus musculus ox=10090 gn=tp53 pe=1 sv=4
MTAMEESQSDISLELPLSQETFSGLWKLLPPEDILPSPHCMDDLLLPQDVEEFFEGPSEALRVSGAPAAQDPVTETPGPVAPAPATPWPLSSFVPSQKTYQGNYGFHLGFLQSGTAKSVMCTYSPPLNKLFCQLAKTCPVQLWVSATPPAGSRVRAMAIYKKSQHMTEVVRRCPHHERCSDGDGLAPPQHLIRVEGNLYPEYLEDRQTFRHSVVVPYEPPEAGSEYTTIHYKYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRDSFEVRVCACPGRDRRTEEENFRKKEVLCPELPPGSAKRALPTCTSASPPQKKKPLDGEYFTLKIRGRKRFEMFRELNEALELKDAHATEESGDSRAHSSYLKTKKGQSTSRHKKTMVKKVGPDSD
>sp|p04637|p53 human cellular tumor antigen p53 os=homo sapiens ox=9606 gn=tp53 pe=1 sv=4
MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGPDEAPRMPEAAPPVAPAPAAPTPAAPAPAPSWPLSSSVPSQKTYQGSYGFRLGFLHSGTAKSVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHERCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKGEPHHELPPGSTKRALPNNTSSSPQPKKKPLDGEYFTLQIRGRERFEMFRELNEALELKDAQAGKEPGGSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD
>sp|q29537|p53 canlf cellular tumor antigen p53 os=canis lupus familiaris ox=9615 gn=tp53 pe=2 sv=2
MEESQSELNIDPPLSQETFSELWNLLPENNVLSSELCPAVDELLLPESVVNWLDEDSDDAPRMPATSAPTAPGPAPSWPLSSSVPSPKTYPGTYGFRLGFLHSGTAKSVTWTYSPLLNKLFCQLAKTCPVQLWVSSPPPPNTCVRAMAIYKKSEFVTEVVRRCPHHERCSDSSDGLAPPQHLIRVEGNLRAKYLDDRNTFRHSVVVPYEPPEVGSDYTTIHYNYMCNSSCMGGMNRRPILTIITLEDSSGNVLGRNSFEVRVCACPGRDRRTEEENFHKKGEPCPEPPPGSTKRALPPSTSSSPPQKKKPLDGEYFTLQIRGRERYEMFRNLNEALELKDAQSGKEPGGSRAHSSHLKAKKGQSTSRHKKLMFKREGLDSD
```

**Example - limit parallel workers**
```bash
getseq mouse p53, human p53, dog p53 --max-workers 3
```
  
#### Disabling the separation of multiple entries by commas

You can disable the separation of multiple entries by commas using the ``-i`` or ``-ignore-commas`` flag. This will let you input queries of protein names that contain commmas without having the query separated into multiple queries!
  
**Example**
```bash
getseq human Beta-1,4 N-acetylgalactosaminyltransferase -i
>sp|q6l9w6|b4gn3 human beta-1,4-n-acetylgalactosaminyltransferase 3 os=homo sapiens ox=9606 gn=b4galnt3 pe=1 sv=2
MGSPRAARPPLLLRPVKLLRRRFRLLLALAVVSVGLWTLYLELVASAQVGGNPLNRRYGSWRELAKALASRNIPAVDPHLQFYHPQRLSLEDHDIDQGVSSNSSYLKWNKPVPWLSEFRGRANLHVFEDWCGSSIQQLRRNLHFPLYPHIRTTLRKLAVSPKWTNYGLRIFGYLHPFTDGKIQFAIAADDNAEFWLSLDDQVSGLQLLASVGKTGKEWTAPGEFGKFRSQISKPVSLSASHRYYFEVLHKQNEEGTDHVEVAWRRNDPGAKFTIIDSLSLSLFTNETFLQMDEVGHIPQTAASHVDSSNALPRDEQPPADMLRPDPRDTLYRVPLIPKSHLRHVLPDCPYKPSYLVDGLPLQRYQGLRFVHLSFVYPNDYTRLSHMETHNKCFYQENAYYQDRFSFQEYIKIDQPEKQGLEQPGFEENLLEESQYGEVAEETPASNNQNARMLEGRQTPASTLEQDATDYRLRSLRKLLAQPREGLLAPFSKRNSTASFPGRTSHIPVQQPEKRKQKPSPEPSQDSPHSDKWPPGHPVKNLPQMRGPRPRPAGDSPRKTQWLNQVESYIAEQRRGDRMRPQAPGRGWHGEEEVVAAAGQEGQVEGEEEGEEEEEEEDMSEVFEYVPVFDPVVNWDQTFSARNLDFQALRTDWIDLSCNTSGNLLLPEQEALEVTRVFLKKLNQRSRGRYQLQRIVNVEKRQDQLRGGRYLLELELLEQGQRVVRLSEYVSARGWQGIDPAGGEEVEARNLQGLVWDPHNRRRQVLNTRAQEPKLCWPQGFSWSHRAVVHFVVPVKNQARWVQQFIKDMENLFQVTGDPHFNIVITDYSSEDMDVEMALKRSKLRSYQYVKLSGNFERSAGLQAGIDLVKDPHSIIFLCDLHIHFPAGVIDAIRKHCVEGKMAFAPMVMRLHCGATPQWPEGYWEVNGFGLLGIYKSDLDRIGGMNTKEFRDRWGGEDWELLDRILQAGLDVERLSLRNFFHHFHSKRGMWSRRQMKTL
```

### Additional usage from the command-line

#### Saving the output of a query

If you want to save the output, you can use the ``-o`` or ``--output`` flag. This will save the output to a file to your specified destination.

You can save to a full path or to a file in the current directory.
  
**Example - multiple sequence**
```bash
getseq mouse p53, human p53, dog p53 -o /Users/thisCoolUser/Desktop/my_sequences/p53_seqs.fasta
	
Sequences saved to /Users/thisCoolUser/Desktop/my_sequences/p53_seqs.fasta

```

**Example - save to the current directory**
```bash
getseq mouse p53 -o p53_mouse.fasta
```
  
**NOTE** - by default, if you have any queries that fail **and** you're saving the output, getseq will save a second file called 'failed_queries.txt' that contains all queries that failed. getseq will let you know if this happens!
  
**Example -**
```bash
getseq mouse p53, human p53, doggggg p53 -o /Users/thisCoolUser/Desktop/my_sequences/p53_seqs.fasta
	
Sequences saved to /Users/thisCoolUser/Desktop/my_sequences/p53_seqs.fasta

Failed queries detected!
Failed queries saved to /Users/thisCoolUser/Desktop/my_sequences/failed_queries.txt
```
  
**If you want to disable the save file output,** you can use the ``-p`` or ``-print_failed_queries`` flag. This will just print the failed queries to the terminal and not save it to a file.

**Example -**
```bash
getseq mouse p53, human p53, doggggg p53 -o /Users/thisCoolUser/Desktop/my_sequences/p53_seqs.fasta
Sequences saved to /Users/thisCoolUser/Desktop/my_sequences/p53_seqs.fasta
Failed queries detected!

Failed queries:
Unable to retrieve sequence for the query 'doggggg p53'
```

#### Query by Uniprot ID

If you want to search by Uniprot ID, use the ``-u`` or ``--uniprot`` flag. The getseq command doesn't require you to use the ``-u`` flag when using a Uniprot ID as the query, but it does increase the accuracy of your query if you do. If you use the ``-u`` flag, you can also search for specific isoforms. **If you do not use the -u flag, you will not be able to retrieve specific isoforms**. 

**Example**
**isoform 2**
```bash
getseq P49021-2, P49021-3 -u
>>sp|P49021-2|TIM_DROME Isoform R of Protein timeless OS=Drosophila melanogaster OX=7227 GN=tim
MDWLLATPQLYSAFSSLGCLEGDTYVVNPNALAILEEINYKLTYEDQTLRTFRRAIGFGQNVRSDLIPLLENAKDDAVLESVIRILVNLTVPVECLFSVDVMYRTDVGRHTIFELNKLLYTSKEAFTEARSTKSVVEYMKHILESDPKLSPHKCDQINNCLLLLRNILHIPETHAHCVMPMMQSMPHGISMQNTILWNLFIQSIDKLLLYLMTCPQRAFWGVTMVQLIALIYKDQHGSGDSSPMLTSDPTSDSSDNGSNGRGMGGGMREGTAATLQEVSRKGQEYQNAMARVPADKPDGSEEASDMTGNDSEQPGSPEQSQPAGESMDDGDYEDQRHRQLNEHGEEDEDEDEVEEEEYLQLGPASEPLNLTQQPADKVNNTTNPTSSAPQGCLGNEPFKPPPPLPVRASTSAHAQMQKFNESSYASHVSAVKLGQKSPHAGQLQLTKGKCCPQKRECPSSQSELSDCGYGTQVENQESISTSSNDDDGPQGKPQHQKPPCNTKPRNKPRTIMSPMDKKELRRKKLVKRSKSSLINMKGLVQHTPTDDDISNLLKEFTVDFLLKGYSYLVEELHMQLLSNAKVPIDTSHFFWLVTYFLKFAAQLELDMEHIDTILTYDVLSYLTYEGVSLCEQLELNARQEGSDLKPYLRRMHLVVTAIREFLQAIDTYNKVTHLNEDDKAHLRQLQLQISEMSDLRCLFVLLLRRFNPSIHSKQYLQDLVVTNHILLLILDSSAKLGGCQTIRLSEHITQFATLEVMHYYGILLEDFNNNGEFVNDCIFTMMHHIGGDLGQIGVLFQPIILKTYSRIWEADYELCDDWSDLIEYVIHKFMNTPPKSPLTIPTTSLTEMTKEHNQEHTVCSWSQEEMDTLYWYYVQSKKNNDIVGKIVKLFSNNGNKLKTRISIIQQLLQQDIITLLEYDDLMKFEDAEYQRTLLTTPTSATTESGIEIKECAYGKPSDDVQILLDLIIKENKAQHLLWLQRILIECCFVKLTLRSGLKVPEGDHIMEPVAYHCICKQKSIPVVQWNNEQSTTMLYQPFVLLLHKLGIQLPADAGSIFARIPDYWTPETMYGLAKKLGPLDKLNLKFDASELEDATASSPSRYHHTGPRNSLSSVSSLDVDLGDTEELALIPEVDAAVEKAHAMASTPSPSEIFAVPKTKHCNSIIRYTPDPTPPVPNWLQLVMRSKCNHRTGPSGDPSDCIGSSSTTVDDEGFGKSISAATSQAASTSMSTVNPTTTLSLNMLNTFMGSHNENSSSSGCGGTVSSLSMVALMSTGAAGGGGNTSGLEMDVDASMKSSFERLEVNGSHFSRANNLDQEYSAMVASVYEKEKELNSDNVSLASDLTRMYVSDEDDRLERTEIRVPHYH
>>sp|P49021-3|TIM_DROME Isoform O of Protein timeless OS=Drosophila melanogaster OX=7227 GN=tim
MDWLLATPQLYSAFSSLGCLEGDTYVVNPNALAILEEINYKLTYEDQTLRTFRRAIGFGQNVRSDLIPLLENAKDDAVLESVIRILVNLTVPVECLFSVDVMYRTDVGRHTIFELNKLLYTSKEAFTEARSTKSVVEYMKHILESDPKLSPHKCDQINNCLLLLRNILHIPETHAHCVMPMMQSMPHGISMQNTILWNLFIQSIDKLLLYLMTCPQRAFWGVTMVQLIALIYKDQHVSTLQKLLSLWFEASLSESSEDNESNTSPPKQGSGDSSPMLTSDPTSDSSDNGSNGRGMGGGMREGTAATLQEVSRKGQEYQNAMARVPADKPDGSEEASDMTGNDSEQPGSPEQSQPAGESMDDGDYEDQRHRQLNEHGEEDEDEDEVEEEEYLQLGPASEPLNLTQQPADKVNNTTNPTSSAPQGCLGNEPFKPPPPLPVRASTSAHAQMQKFNESSYASHVSAVKLGQKSPHAGQLQLTKGKCCPQKRECPSSQSELSDCGYGTQVENQESISTSSNDDDGPQGKPQHQKPPCNTKPRNKPRTIMSPMDKKELRRKKLVKRSKSSLINMKGLVQHTPTDDDISNLLKEFTVDFLLKGYSYLVEELHMQLLSNAKVPIDTSHFFWLVTYFLKFAAQLELDMEHIDTILTYDVLSYLTYEGVSLCEQLELNARQEGSDLKPYLRRMHLVVTAIREFLQAIDTYNKVTHLNEDDKAHLRQLQLQISEMSDLRCLFVLLLRRFNPSIHSKQYLQDLVVTNHILLLILDSSAKLGGCQTIRLSEHITQFATLEVMHYYGILLEDFNNNGEFVNDCIFTMMHHIGGDLGQIGVLFQPIILKTYSRIWEADYELCDDWSDLIEYVIHKFMNTPPKSPLTIPTTSLTEMTKEHNQEHTVW
```

#### Just print sequence

If you just want to print the sequence, use the ``-j`` or ``--just_sequence`` flag. WARNING: If you do this, you will not know if you got the exact sequence that you want! The reason the Uniprot ID, organism, and protein name are printed back to you is to help you check that you got the protien that you want!

**Example**
```bash
getseq p53 mouse -j
MTAMEESQSDISLELPLSQETFSGLWKLLPPEDILPSPHCMDDLLLPQDVEEFFEGPSEALRVSGAPAAQDPVTETPGPVAPAPATPWPLSSFVPSQKTYQGNYGFHLGFLQSGTAKSVMCTYSPPLNKLFCQLAKTCPVQLWVSATPPAGSRVRAMAIYKKSQHMTEVVRRCPHHERCSDGDGLAPPQHLIRVEGNLYPEYLEDRQTFRHSVVVPYEPPEAGSEYTTIHYKYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRDSFEVRVCACPGRDRRTEEENFRKKEVLCPELPPGSAKRALPTCTSASPPQKKKPLDGEYFTLKIRGRKRFEMFRELNEALELKDAHATEESGDSRAHSSYLKTKKGQSTSRHKKTMVKKVGPDSD
```

## Using getSequence from Python:

getSequence exposes ``getseq`` and ``batch_getseq`` in Python. To use them, first import the functions you need.
```python
from getSequence import getseq, batch_getseq
```
Now you can use getseq.
  
The ``getseq`` function can take either a string that is a single query or a list of strings for multiple queries. If it is a single query, by default it returns a list with the first entry in the list being the Uniprot header and the second one being the sequence. For multiple queries, a list of lists is returned. Multiple Python queries are fetched in parallel and keep the same order as the input list.

**Example - single query**
```python
getseq('p53')
['sp|p04637|p53 human cellular tumor antigen p53 os=homo sapiens ox=9606 gn=tp53 pe=1 sv=4', 'MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGPDEAPRMPEAAPPVAPAPAAPTPAAPAPAPSWPLSSSVPSQKTYQGSYGFRLGFLHSGTAKSVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHERCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKGEPHHELPPGSTKRALPNNTSSSPQPKKKPLDGEYFTLQIRGRERFEMFRELNEALELKDAQAGKEPGGSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD']
```

**Example - multiple queries**
```python
getseq(['human p53', ' dog p53', ' mouse p53'])
[['sp|p04637|p53 human cellular tumor antigen p53 os=homo sapiens ox=9606 gn=tp53 pe=1 sv=4', 'MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGPDEAPRMPEAAPPVAPAPAAPTPAAPAPAPSWPLSSSVPSQKTYQGSYGFRLGFLHSGTAKSVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHERCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKGEPHHELPPGSTKRALPNNTSSSPQPKKKPLDGEYFTLQIRGRERFEMFRELNEALELKDAQAGKEPGGSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD'], ['sp|q29537|p53 canlf cellular tumor antigen p53 os=canis lupus familiaris ox=9615 gn=tp53 pe=2 sv=2', 'MEESQSELNIDPPLSQETFSELWNLLPENNVLSSELCPAVDELLLPESVVNWLDEDSDDAPRMPATSAPTAPGPAPSWPLSSSVPSPKTYPGTYGFRLGFLHSGTAKSVTWTYSPLLNKLFCQLAKTCPVQLWVSSPPPPNTCVRAMAIYKKSEFVTEVVRRCPHHERCSDSSDGLAPPQHLIRVEGNLRAKYLDDRNTFRHSVVVPYEPPEVGSDYTTIHYNYMCNSSCMGGMNRRPILTIITLEDSSGNVLGRNSFEVRVCACPGRDRRTEEENFHKKGEPCPEPPPGSTKRALPPSTSSSPPQKKKPLDGEYFTLQIRGRERYEMFRNLNEALELKDAQSGKEPGGSRAHSSHLKAKKGQSTSRHKKLMFKREGLDSD'], ['sp|p02340|p53 mouse cellular tumor antigen p53 os=mus musculus ox=10090 gn=tp53 pe=1 sv=4', 'MTAMEESQSDISLELPLSQETFSGLWKLLPPEDILPSPHCMDDLLLPQDVEEFFEGPSEALRVSGAPAAQDPVTETPGPVAPAPATPWPLSSFVPSQKTYQGNYGFHLGFLQSGTAKSVMCTYSPPLNKLFCQLAKTCPVQLWVSATPPAGSRVRAMAIYKKSQHMTEVVRRCPHHERCSDGDGLAPPQHLIRVEGNLYPEYLEDRQTFRHSVVVPYEPPEAGSEYTTIHYKYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRDSFEVRVCACPGRDRRTEEENFRKKEVLCPELPPGSAKRALPTCTSASPPQKKKPLDGEYFTLKIRGRKRFEMFRELNEALELKDAHATEESGDSRAHSSYLKTKKGQSTSRHKKTMVKKVGPDSD']]
```

**Example - tune parallel workers**
```python
getseq(['human p53', 'dog p53', 'mouse p53'], max_workers=3)
```

The ``batch_getseq`` helper also fetches queries in parallel and accepts the same keyword arguments as ``getseq``. It is useful when you want to make the batch behavior explicit in your code.

**Example - batch_getseq**
```python
batch_getseq(['human p53', 'dog p53', 'mouse p53'], max_workers=3)
```

### Additional usage in Python

#### Searching by Uniprot ID
  
When searching by Uniport ID, it is recommended that you explicitly set ``uniprot_id=True`` when using the ``getseq`` function. This will make the query explicitly call that specific Uniprot ID instead of searching Uniprot for the ID. This **is the only way that you can get specific splicing isoforms when using getseq because searching specific isoforms using the Uniprot search functionality doesn't gaurantee the correct isoform**. 
  
**Example**
```python
getseq('P49021-3', uniprot_id=True)
['>sp|P49021-3|TIM_DROME Isoform O of Protein timeless OS=Drosophila melanogaster OX=7227 GN=tim', 'MDWLLATPQLYSAFSSLGCLEGDTYVVNPNALAILEEINYKLTYEDQTLRTFRRAIGFGQNVRSDLIPLLENAKDDAVLESVIRILVNLTVPVECLFSVDVMYRTDVGRHTIFELNKLLYTSKEAFTEARSTKSVVEYMKHILESDPKLSPHKCDQINNCLLLLRNILHIPETHAHCVMPMMQSMPHGISMQNTILWNLFIQSIDKLLLYLMTCPQRAFWGVTMVQLIALIYKDQHVSTLQKLLSLWFEASLSESSEDNESNTSPPKQGSGDSSPMLTSDPTSDSSDNGSNGRGMGGGMREGTAATLQEVSRKGQEYQNAMARVPADKPDGSEEASDMTGNDSEQPGSPEQSQPAGESMDDGDYEDQRHRQLNEHGEEDEDEDEVEEEEYLQLGPASEPLNLTQQPADKVNNTTNPTSSAPQGCLGNEPFKPPPPLPVRASTSAHAQMQKFNESSYASHVSAVKLGQKSPHAGQLQLTKGKCCPQKRECPSSQSELSDCGYGTQVENQESISTSSNDDDGPQGKPQHQKPPCNTKPRNKPRTIMSPMDKKELRRKKLVKRSKSSLINMKGLVQHTPTDDDISNLLKEFTVDFLLKGYSYLVEELHMQLLSNAKVPIDTSHFFWLVTYFLKFAAQLELDMEHIDTILTYDVLSYLTYEGVSLCEQLELNARQEGSDLKPYLRRMHLVVTAIREFLQAIDTYNKVTHLNEDDKAHLRQLQLQISEMSDLRCLFVLLLRRFNPSIHSKQYLQDLVVTNHILLLILDSSAKLGGCQTIRLSEHITQFATLEVMHYYGILLEDFNNNGEFVNDCIFTMMHHIGGDLGQIGVLFQPIILKTYSRIWEADYELCDDWSDLIEYVIHKFMNTPPKSPLTIPTTSLTEMTKEHNQEHTVW']
```

#### Just return the sequence

To just return the protein sequence as a string, set ``just_sequence=True``

**Example**
```python
getseq('p53', just_sequence=True)
'MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGPDEAPRMPEAAPPVAPAPAAPTPAAPAPAPSWPLSSSVPSQKTYQGSYGFRLGFLHSGTAKSVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHERCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKGEPHHELPPGSTKRALPNNTSSSPQPKKKPLDGEYFTLQIRGRERFEMFRELNEALELKDAQAGKEPGGSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD'
```

#### Return a dictionary instead of a list

If you want to return a dictionary instead of a list, set ``return_dict=True``. The dictionary will have the Uniprot ID as the key and the sequence as the value. 

**Example**
```python
getseq(['human p53', ' dog p53', ' mouse p53'], return_dict=True)
{'sp|p04637|p53 human cellular tumor antigen p53 os=homo sapiens ox=9606 gn=tp53 pe=1 sv=4': 'MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGPDEAPRMPEAAPPVAPAPAAPTPAAPAPAPSWPLSSSVPSQKTYQGSYGFRLGFLHSGTAKSVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHERCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKGEPHHELPPGSTKRALPNNTSSSPQPKKKPLDGEYFTLQIRGRERFEMFRELNEALELKDAQAGKEPGGSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD', 'sp|q29537|p53 canlf cellular tumor antigen p53 os=canis lupus familiaris ox=9615 gn=tp53 pe=2 sv=2': 'MEESQSELNIDPPLSQETFSELWNLLPENNVLSSELCPAVDELLLPESVVNWLDEDSDDAPRMPATSAPTAPGPAPSWPLSSSVPSPKTYPGTYGFRLGFLHSGTAKSVTWTYSPLLNKLFCQLAKTCPVQLWVSSPPPPNTCVRAMAIYKKSEFVTEVVRRCPHHERCSDSSDGLAPPQHLIRVEGNLRAKYLDDRNTFRHSVVVPYEPPEVGSDYTTIHYNYMCNSSCMGGMNRRPILTIITLEDSSGNVLGRNSFEVRVCACPGRDRRTEEENFHKKGEPCPEPPPGSTKRALPPSTSSSPPQKKKPLDGEYFTLQIRGRERYEMFRNLNEALELKDAQSGKEPGGSRAHSSHLKAKKGQSTSRHKKLMFKREGLDSD', 'sp|p02340|p53 mouse cellular tumor antigen p53 os=mus musculus ox=10090 gn=tp53 pe=1 sv=4': 'MTAMEESQSDISLELPLSQETFSGLWKLLPPEDILPSPHCMDDLLLPQDVEEFFEGPSEALRVSGAPAAQDPVTETPGPVAPAPATPWPLSSFVPSQKTYQGNYGFHLGFLQSGTAKSVMCTYSPPLNKLFCQLAKTCPVQLWVSATPPAGSRVRAMAIYKKSQHMTEVVRRCPHHERCSDGDGLAPPQHLIRVEGNLYPEYLEDRQTFRHSVVVPYEPPEAGSEYTTIHYKYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRDSFEVRVCACPGRDRRTEEENFRKKEVLCPELPPGSAKRALPTCTSASPPQKKKPLDGEYFTLKIRGRKRFEMFRELNEALELKDAHATEESGDSRAHSSYLKTKKGQSTSRHKKTMVKKVGPDSD'}
```


#### Ignore individual queries when doing multiple queries

By default, getseq will raise an Exception if it is unable to return a sequence using your query. You can disable this by setting ``ignore_failures`` to True. If you do this, getseq will print a out your failed queries instead of raising an Exception. 


**Example**
```python
getseq(['human p53', ' doggggggg p53', ' mouse p53'], ignore_failures=True)
Failed queries:
Unable to retrieve sequence for the query ' doggggggg p53'
[['sp|p04637|p53 human cellular tumor antigen p53 os=homo sapiens ox=9606 gn=tp53 pe=1 sv=4', 'MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGPDEAPRMPEAAPPVAPAPAAPTPAAPAPAPSWPLSSSVPSQKTYQGSYGFRLGFLHSGTAKSVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHERCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKGEPHHELPPGSTKRALPNNTSSSPQPKKKPLDGEYFTLQIRGRERFEMFRELNEALELKDAQAGKEPGGSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD'], ['sp|p02340|p53 mouse cellular tumor antigen p53 os=mus musculus ox=10090 gn=tp53 pe=1 sv=4', 'MTAMEESQSDISLELPLSQETFSGLWKLLPPEDILPSPHCMDDLLLPQDVEEFFEGPSEALRVSGAPAAQDPVTETPGPVAPAPATPWPLSSFVPSQKTYQGNYGFHLGFLQSGTAKSVMCTYSPPLNKLFCQLAKTCPVQLWVSATPPAGSRVRAMAIYKKSQHMTEVVRRCPHHERCSDGDGLAPPQHLIRVEGNLYPEYLEDRQTFRHSVVVPYEPPEAGSEYTTIHYKYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRDSFEVRVCACPGRDRRTEEENFRKKEVLCPELPPGSAKRALPTCTSASPPQKKKPLDGEYFTLKIRGRKRFEMFRELNEALELKDAHATEESGDSRAHSSYLKTKKGQSTSRHKKTMVKKVGPDSD']]
```

## Changes

### V3.0.1 (May 2026)
* Fixed versioning issue so the update can be published to pypi.

### V3.0 (May 2026)
* Replaced process-based multiprocessing with thread-based parallel fetching for list, batch, and CLI queries. This is much faster for network-bound UniProt requests and preserves the input order of results.
* Simplified ``batch_getseq`` so it now uses the same optimized list-query path as ``getseq([...])`` instead of wrapping each query in an extra public-call layer.
* Added ``max_workers`` for Python list/batch queries and ``--max-workers`` for CLI multi-query runs.
* Added request timeouts and HTTP status checks so failed UniProt responses are reported consistently instead of being parsed as sequences.
* Improved query parsing and result ranking around empty input, missing FASTA records, and headers without ``gn=`` or ``ox=`` fields.
* Fixed saving output files to the current directory, such as ``-o output.fasta`` or ``output_file='output.fasta'``.
* Made Python ``output_file`` writes force FASTA-compatible header/sequence data even when ``just_sequence=True`` is also passed.
* Fixed empty comma-separated CLI entries and changed saved failed-query reports without an output directory to ``failed_queries.txt`` in the current directory.
* Added regression tests covering ordered parallel batch results, current-directory output, worker validation, and ignored failures.

### V2.2 (October 2024)
* Made pep517 compliant, now using tomls. h/t alex

### V2.1 (March 2024)
* Added parallelization for queries h/t jeff

### V2.0 (February 2024)
* Major update to command-line and Python functionality
* Added ability to do multiple queries from a single command from CLI
* Added ability to do multiple queries by inputting a list in Python
* Added ability to save output to a file from CLI
* Added ability to save output to a file from Python
* Added ability to get different isoforms of sequences from Python and CLI


### Copyright

Copyright (c) 2022, Ryan Emenecker


#### Acknowledgements
 
•Project based on the 
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.6.
•Project motivated by my never ending need to make doing science more enjoyable. 
