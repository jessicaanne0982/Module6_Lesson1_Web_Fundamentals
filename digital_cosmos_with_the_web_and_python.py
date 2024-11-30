# Task 1 - Set up a Python Virtual Environment and Install Required Packages
"""
1. In terminal, navigate to cd Documents/SE_Bootcamp/Module6.
2. mkdir Lesson1_Web_Fundamentals
3. cd Lesson1_Web_Fundamentals
4. python3 -m venv myenv
5. source myenv/bin/activate
6. pip install requests
7. Create a file OUTSIDE of venv folder called digital_cosmos_with_the_web_and_python.py
"""
 
# Task 2 - Fetch Data from a Space API 
import requests
import json

def fetch_planet_data(): 

    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
   
    for planet in planets:
        if planet['isPlanet']:
            name = planet.get('englishName')
            mass = planet.get('mass').get('massValue')
            orbit_period = planet.get('sideralOrbit')
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

fetch_planet_data()

# Task 3 - Data Presentation and Analysis

import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    planet_data = [] 
   
    for planet in planets:
        if planet['isPlanet']:
            name = planet.get('englishName')
            mass = planet.get('mass').get('massValue')
            planet_data.append((name, mass))
    return planet_data

def find_heaviest_planet(planets):
    heaviest_planet = max(planets, key=lambda planet: planet[1])
    return heaviest_planet

planets = fetch_planet_data() 
name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} kg.")



        