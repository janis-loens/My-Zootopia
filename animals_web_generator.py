import json

def load_data(file_path):
    """Load data from a JSON file."""
    with open(file_path, 'r') as handle:
        return json.load(handle)
    
def get_data(data):
    """Print data in a readable format."""
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
        



animals_data = load_data('animals_data.json')
print(get_data(animals_data))
