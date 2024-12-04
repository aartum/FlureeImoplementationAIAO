# /**
#  * @file jsonld_to_json.py
#  *
#  * @brief Converts JSON-LD data to a structured JSON format with specific fields.
#  */

import json
import sys

def extract_context_and_graph(jsonld_data):
    """
    Extracts the "@context" and "@graph" from JSON-LD data.

    :param jsonld_data: JSON-LD data in string format.
    :return: Tuple containing context dictionary and graph list.
    :throws ValueError: If "@context" or "@graph" is missing in JSON-LD data.
    """
    jsonld_data = json.loads(jsonld_data)

    if '@context' not in jsonld_data:
        raise ValueError('Missing "@context" in JSON-LD data')

    context = jsonld_data['@context']

    if '@graph' not in jsonld_data:
        raise ValueError('Missing "@graph" in JSON-LD data')

    graph = jsonld_data['@graph']

    return context, graph

def create_output_json(context, ledger, graph, output_file_path):
    """
    Creates a structured JSON output file to be used as the request body for a transaction into a Fluree ledger.

    :param context: Dictionary containing the "@context".
    :param ledger: Name of the Fluree ledger.
    :param graph: List containing the "@graph".
    :param output_file_path: Path to the output JSON file.
    """
    output_data = {
        "@context": context,
        "ledger": ledger,
        "insert": graph
    }

    with open(output_file_path, 'w') as output_file:
        json.dump(output_data, output_file, indent=2)

def main():
    """
    Main function to execute the JSON-LD to JSON conversion.
    Reads command-line arguments for input JSON-LD file, ledger name, and output JSON file path.
    """
    if len(sys.argv) != 4:
        print("Usage: python jsonld_to_json.py <jsonld_file> <ledger_name> <output_json_file>")
        sys.exit(1)

    jsonld_file = sys.argv[1]
    ledger_name = sys.argv[2]
    output_file = sys.argv[3]

    try:
        context, graph = extract_context_and_graph(jsonld_file)
        create_output_json(context, ledger_name, graph, output_file)
        print(f"Successfully created JSON file: {output_file}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
