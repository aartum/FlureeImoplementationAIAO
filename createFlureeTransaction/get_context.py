import sys

def extract_prefixes(file_path):
    """
    Extracts prefixes from a .ttl file and constructs a dictionary representing
    the "@context" from those prefixes. This dictionary is used in JSON-LD to
    prevent the use of verbose URIs.

    Args:
        file_path (str): The path to the .ttl file from which prefixes are extracted.

    Returns:
        dict: A dictionary where keys are prefixes (strings) and values are URIs (strings).
    """
    prefix_dict = {}

    # Read the file and extract lines starting with @prefix
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('@prefix'):
                parts = line.split()
                if len(parts) == 4 and parts[0] == '@prefix':
                    prefix = parts[1][:-1]  # Remove the trailing ':'
                    if prefix == '':
                        prefix = ':'  # Use ":" for empty prefix
                    uri = parts[2][1:-1]  # Remove the surrounding '<' and '>'
                    prefix_dict[prefix] = uri

    return prefix_dict

def print_dict(prefix_dict):
    """
    Prints the contents of the provided dictionary in the format "<key>: <value>".

    Args:
        prefix_dict (dict): The dictionary to print.
    """
    for key, value in prefix_dict.items():
        print(f'"{key}": "{value}"')

def main():
    """
    Main function to execute the extraction and printing of prefixes from a .ttl file.
    """
    # Check if the file path is provided
    if len(sys.argv) != 2:
        print("Usage: python extract_prefixes.py <path_to_ttl_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    # Extract prefixes and create dictionary
    prefix_dict = extract_prefixes(file_path)

    # Print the resulting dictionary in the desired format
    print_dict(prefix_dict)

if __name__ == "__main__":
    main()
