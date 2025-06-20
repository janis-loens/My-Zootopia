import json

def load_data(file_path):
    """Load data from a JSON file."""
    with open(file_path, 'r') as handle:
        return json.load(handle)
    
def print_data(data):
    """Print data in a readable format."""
    for fox in data:   
        name = fox['name']
        diet = fox['characteristics']['diet']
        location = fox['locations']
        try:    
            type = fox['characteristics']['type']
            print(f"Name: {name}\nDiet: {diet}\nLocation: {', '.join(location)}\nType: {type}\n")
        except KeyError:
            print(f"Name: {name}\nDiet: {diet}\nLocation: {', '.join(location)}\n")

animals_data = load_data('animals_data.json')
# Print the loaded data
print_data(animals_data)
