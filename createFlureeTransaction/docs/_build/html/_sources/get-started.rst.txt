Getting started
================

This package can be used to create a Fluree transaction body in .json format from a 
.ttl file. 

It extracts the prefixes from the .ttl file to create a @context field and converts 
the data to JSON-LD format as required by Fluree.

**Usage**

``main.py`` takes 3 command line arguments:

 - The path to the input ``.ttl`` file
 - The name of the Fluree ledger to make the transaction to
 - The path to the output ``.json`` file

**Creating the Fluree request**

.. code-block:: sh

	curl -X POST \
  	-H "Content-Type: application/json" \
  	--data-binary "<path/to/json/file>" \
  	http://localhost:<port>/fluree/<create/insert/etc.>
