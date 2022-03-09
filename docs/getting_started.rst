*********************************
Getting Started with getSequence
*********************************

What is getSequence?
====================

getSequence is a command-line interface for printing protein sequences from Uniprot to your terminal. I made this because I was tired of having to navigate to the website, copy a sequence, and format it. It also has functionality to use in Python.


How does it work?
====================

getSequence will take in your name and query Uniprot. It then takes the top hit from Uniprot and gets the sequence information. You can specify multiple things from the command-line or form Python, exactly how you would if you were to use the search box on the Uniprot website.

This seems kind of unnecessary...
==================================

Fair enough. I still think it's nifty.

Installation
=============

**getSequence** in availbale through PyPi - to install just run...

.. code-block:: bash

	$ pip install getSequence


Alternatively, you can get **getSequence** directly from GitHub. 

To clone the GitHub repository and gain the ability to modify a local copy of the code, run

.. code-block:: bash

	$ git clone https://github.com/ryanemenecker/getSequence.git
	$ cd getSequence
	$ pip install .

This will install **getSequence** locally. If you modify the source code in the local repository, be sure to re-install with `pip`.

For documentation, see https://getsequence.readthedocs.io/en/latest/getting_started.html