import sys

import get_context
import ttl_jsonld
import request_body

# Check if the input and output file paths are provided
if len(sys.argv) != 4:
    print("Usage: python main <path/to/ttlfile> <ledger name> <path/to/json/file>")
    sys.exit(1)

input_name = sys.argv[1]
ledger = sys.argv[2]
output_name = sys.argv[3]

context = get_context.extract_prefixes(input_name)

jsonld_data = ttl_jsonld.ttl_to_jsonld(input_name, context).decode("utf-8")

_, graph = request_body.extract_context_and_graph(jsonld_data)

try:
    request_body.create_output_json(context, ledger, graph, output_name)
    print("Success! Request body generated.")
except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

