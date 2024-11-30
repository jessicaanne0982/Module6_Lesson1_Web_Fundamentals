# Task 1 - Setting Up a Python Virtual Environment and Installing Packages
"""
1. In terminal, navigate to cd Documents/SE_Bootcamp/Module6.
2. mkdir Lesson1_Web_Fundamentals
3. cd Lesson1_Web_Fundamentals
4. python3 -m venv myenv
5. source myenv/bin/activate
6. pip install requests
7. Create a file OUTSIDE of venv folder called exploring_the_web_and_python.py
"""
 
# Task 2 - Fetching Data from the Pokémon API
import requests
import json
 
response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
json_data = response.text
 
pikachu_data = json.loads(json_data)
 
print(pikachu_data["name"])
print(pikachu_data["abilities"])

# Task 3 - Analyzing and Displaying Data
import requests
import json

def fetch_pokemon_data(pokemon_names):
    pokemon_list = []

    for pokemon_name in pokemon_names:
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
        response = requests.get(url)
        pokemon_info = response.json()
        name = pokemon_info.get("name")
        # To get just the names of the abilities, create a list and loop through the abilities for each pokemon
        abilities = []
        for ability in pokemon_info.get("abilities"):
            abilities.append(ability['ability']['name'])
        weight = pokemon_info.get("weight")
        print(f"Name: {name}, Ability: {abilities}, Weight: {weight}")
        # add the name, abilities, and weight to a new list and return for use in the calculate_average_weight function
        pokemon_list.append((name, abilities, weight))
    return pokemon_list
            
def calculate_average_weight(pokemon_list):
    total_weight = 0
    # iterate through the list of pokemon and add their weights together
    for pokemon in pokemon_list:
        total_weight += pokemon[2]
    # take the total weight and divide by the total number of pokemon in the list
    average_weight = total_weight / len(pokemon_list)
    return average_weight

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemon_list = fetch_pokemon_data(pokemon_names)
average_weight = calculate_average_weight(pokemon_list)
print(f"The average weight of the Pokemon is {average_weight}")




