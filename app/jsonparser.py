import json

def format_json_file(input_file_path, output_file_path):
    """
    Reads a JSON file, formats it with proper indentation, and writes the formatted JSON to a new file.

    :param input_file_path: Path to the input JSON file.
    :param output_file_path: Path where the formatted JSON file will be saved.
    """
    try:
        with open(input_file_path, 'r') as input_file:
            # Load JSON data from file
            json_data = json.load(input_file)

            # Format JSON data with indentation
            formatted_json = json.dumps(json_data, indent=4)

            # Write formatted JSON to output file
            with open(output_file_path, 'w') as output_file:
                output_file.write(formatted_json)

        print(f"JSON file formatted and saved to '{output_file_path}'")

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
    except FileNotFoundError:
        print(f"File not found: {input_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


format_json_file("data_file.json","formatted.json")