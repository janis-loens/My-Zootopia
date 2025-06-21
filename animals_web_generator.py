import json

def load_data(file_path) -> list:
    """Load data from a JSON file."""
    with open(file_path, 'r') as handle:
        return json.load(handle)
    
def get_data(data) -> str:
    """Generate a string with information about foxes.
    Args:
        data (list): A list of dictionaries containing animal data.
    Returns:
        str: A formatted string with information about each fox.
    """
    foxes = ''
    for fox in data:   
        name = fox['name']
        diet = fox['characteristics']['diet']
        location = fox['locations']
        try:    
            type = fox['characteristics']['type']
            foxes += f"Name: {name}\nDiet: {diet}\nLocation: {', '.join(location)}\nType: {type}\n\n"
        except KeyError:
            foxes += f"Name: {name}\nDiet: {diet}\nLocation: {', '.join(location)}\n\n"
    return foxes

def read_html(file_path) -> str:
    """Read the content of an HTML file.
    Args:
        file_path (str): The path to the HTML file.
    Returns:
        str: The content of the HTML file.
    """
    with open(file_path, 'r') as file:
        return file.read()

        



animals_data = load_data('animals_data.json')
foxes_data = get_data(animals_data)
html_data = read_html('animals_template.html')

