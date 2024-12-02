# What is this?
This package is used to create a Fluree transaction body in `.json` format from a `.ttl` file.

It converts the data to JSON-LD format (as required by Fluree) and extracts the prefixes from the `.ttl` file to create an `@context` field.

# Getting started
Find the complete documentation under `docs/_build/html/index.html`

## Run

`main.py` takes 4 command line arguments:

1. The path to the input .ttl file
2. The path to the output .json file
3. The name of the Fluree ledger to make the transaction to
4. The base prefix for the ontology

`python3 main.py <path/to/ttl/file\> <path/to/json/file> <ledger-name> <base-prefix>`

For example:

`python3 main.py ./data/smallaia.ttl ./data/smallaia.json aiao/base aia`

It returns a `.json` file which can be used as body for a Fluree request. For example:

<pre>
<code id="curl-command">curl -X POST \
-H "Content-Type: application/json" \
--data-binary "<path/to/json/file>" \
http://localhost:<port>/fluree/<create/insert/etc.></code>
</pre>

## Update the Sphinx documentation

The documentation for this package is created using Sphinx. To update the documentation:

1. Activate a virtual environment if you are using one
2. Run `pip install -r requirements.txt` (or pip3 for MacOS)
3. Navigate to the `docs` folder
4. Run `make html`
