# This program will create a database that connects to the sqlite database where it stores
# the population data for the top 10 populated cities in the United States in 2023. It also
# simulates the population growth and decline for the next 20 years for each year. It will
# then ask the user to pick which city they would like to see a visual representation
# of the growth and decline for the next 20 years.


import sqlite3
import random
import matplotlib.pyplot as plt


# Constants for cities
DB_NAME = "population.db"
CITIES = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "Austin"
]

# Creates a database, population table and inserts the 2023 population
def create_database():

    # Connects to the sqlite database
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    # Creates a table for the population of each city
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    """)

    # Estimate of 2023 population in each city
    population_2023 = [8800000, 3900000, 2700000, 2300000, 1600000,
                       1500000, 1400000, 1400000, 1300000, 930000]

    for i in range(len(CITIES)):
        cursor.execute("""
            INSERT INTO population (city, year, population)
            VALUES (?, ?, ?)
        """, (CITIES[i], 2023, population_2023[i]))

    connection.commit()
    connection.close()

    print("Database and 2023 population records have been created successfully.\n")



# Creates a growth chart of the next 20 years of each state and inserts it into the database
def simulate_population_growth():

    # Connects to the sqlite database
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    # A loop through each city
    for city in CITIES:

        # Find the population of each city in 2023
        cursor.execute("""
            SELECT population FROM population
            WHERE city=? AND year=2023
        """, (city,))
        row = cursor.fetchone()
        current_population = row[0]

        # Simulates the population of the city for the next 20 years
        for year in range(2024, 2044):

            # Finding the growth rate, calculating the new population estimate and insert the new population
            growth_rate = random.uniform(-0.02, 0.04)
            current_population = int(current_population * (1 + growth_rate))
            cursor.execute("""
                INSERT INTO population (city, year, population)
                VALUES (?, ?, ?)
            """, (city, year, current_population))

    connection.commit()
    connection.close()

    print("Population simulation is complete and stored in the database.\n")



# Asks the user what city they would like to display the population growth to
def show_population_growth_graph():

    # Prints a list of cities
    print("Select a city from the top 10 most populated cities in 2023:\n")
    for i, city in enumerate(CITIES, start=1):
        print(f"{i}. {city}")

    # Asks user to choose a city by inputting a numerical number
    choice = int(input("\nEnter the number of the city you would like to see the population growth over the next 20 years: "))

    # Validates the user's input, if not the program will ask to restart the program
    if choice < 1 or choice > len(CITIES):
        print("\nInvalid Input. Restart the program and try typing in a numerical number associated with each city.")
        return

    city_choice = CITIES[choice - 1]

    # Connects to sqlite database
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    # Retrieve the population of the user's selected city
    cursor.execute("""
        SELECT year, population FROM population
        WHERE city=?
        ORDER BY year
    """, (city_choice,))

    results = cursor.fetchall()
    connection.close()

    # Makes the years and population separated into a list
    years = [row[0] for row in results]
    populations = [row[1] for row in results]

    # Creates a plot for the population
    plt.figure(figsize=(10, 5))
    plt.plot(years, populations, marker='o')

    plt.title(f"Population Growth for {city_choice}")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)

    plt.show()



# Main function in order it is executed
def main():

    create_database()

    simulate_population_growth()

    show_population_growth_graph()


# Main function that runs the program
if __name__ == "__main__":
    main()
