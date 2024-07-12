from rdflib import Graph

def ttl_to_jsonld(input_name, context):
    """
    Converts a Turtle (.ttl) file to JSON-LD format using the provided context.

    @param input_name: Name of the input Turtle file.
    @param context: Context dictionary used for JSON-LD serialization.
    @return: JSON-LD serialized data.
    """
    # Create a Graph
    g = Graph()

    # Parse the Turtle file
    try:
        g.parse(input_name, format="turtle")  # default format text/turtle
    except IndexError:
        print("Please provide the input file name as a command-line argument.")
        exit(1)
    except Exception as e:
        print(f"Error parsing Turtle file: {e}")
        exit(1)

    # Check if the graph is empty
    if len(g) == 0:
        print("The graph is empty. Please check the content of the input file.")
        exit(1)

    # Serialize the graph to JSON-LD format and save to a file
    try:
        jsonld_g = g.serialize(format="json-ld", context=context, encoding="utf-8")

        return jsonld_g
    except IndexError:
        print("Please provide the input and output file names as command-line arguments.")
        exit(1)
    except Exception as e:
        print(f"Error serializing to JSON-LD format: {e}")
        exit(1)
