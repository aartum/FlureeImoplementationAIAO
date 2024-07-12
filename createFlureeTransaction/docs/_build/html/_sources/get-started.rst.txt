Getting started
================

This package can be used to create a Fluree transaction body in ``.json`` format from a
``.ttl`` file.

It converts the data to JSON-LD format (as required by Fluree) and extracts the prefixes from the ``.ttl`` file to create a ``@context`` field.

**Use**

``main.py`` takes 4 command line arguments:

 - The path to the input ``.ttl`` file
 - The path to the output ``.json`` file
 - The name of the Fluree ledger to make the transaction to
 - The base prefix for the ontology

**Creating the Fluree request**

.. code-block:: sh

	curl -X POST \
  	-H "Content-Type: application/json" \
  	--data-binary "<path/to/json/file>" \
  	http://localhost:<port>/fluree/<create/insert/etc.>
