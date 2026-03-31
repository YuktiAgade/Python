import pandas as pd
import numpy as np

# Create states data
states_data = {
    'State_Name': ['Maharashtra', 'Uttar Pradesh', 'Rajasthan', 'Madhya Pradesh', 'Tamil Nadu'],
    'Area_sq_km': [307713, 240928, 342239, 308252, 130058],
    'Population': [123144223, 199812341, 68548437, 72626809, 72147030]
}

# Create DataFrame
states_df = pd.DataFrame(states_data)

# Calculate population density (people per sq km)
states_df['Population_Density'] = states_df['Population'] / states_df['Area_sq_km']
states_df['Population_Density'] = states_df['Population_Density'].round(2)

print("=" * 80)
print("STATES DATABASE MANAGEMENT SYSTEM")
print("=" * 80)

# a) Print the complete information of states
print("\na) Complete Information of States:")
print("-" * 80)
print(states_df.to_string(index=False))
print("\n")

# b) Print the name of the State having largest Area
largest_area_state = states_df.loc[states_df['Area_sq_km'].idxmax(), 'State_Name']
largest_area = states_df['Area_sq_km'].max()
print(f"b) State with Largest Area:")
print("-" * 80)
print(f"{largest_area_state} - {largest_area:,} sq km")
print("\n")

# c) Print the name of State having largest population
largest_population_state = states_df.loc[states_df['Population'].idxmax(), 'State_Name']
largest_population = states_df['Population'].max()
print(f"c) State with Largest Population:")
print("-" * 80)
print(f"{largest_population_state} - {largest_population:,} people")
print("\n")

# d & g) Calculate population density (already done in DataFrame creation)
print("d & g) Population Density Calculation:")
print("-" * 80)
print("Population density calculated and added as new column 'Population_Density'")
print("\n")

# e & h) Determine the name of State with highest population density
highest_density_state = states_df.loc[states_df['Population_Density'].idxmax(), 'State_Name']
highest_density = states_df['Population_Density'].max()
print(f"e & h) State with Highest Population Density:")
print("-" * 80)
print(f"{highest_density_state} - {highest_density:.2f} people/sq km")
print("\n")

# f) Print the name of State having largest population (same as c)
print(f"f) State with Largest Population:")
print("-" * 80)
print(f"{largest_population_state} - {largest_population:,} people")
print("\n")

# Additional Statistics
print("=" * 80)
print("ADDITIONAL STATISTICS")
print("=" * 80)
print(f"\nTotal Area covered by these states: {states_df['Area_sq_km'].sum():,} sq km")
print(f"Total Population: {states_df['Population'].sum():,} people")
print(f"Average Population Density: {states_df['Population_Density'].mean():.2f} people/sq km")
print("\n")

# Interactive menu for Lab Assignment 2
print("\n" + "=" * 80)
print("INTERACTIVE MENU - LAB ASSIGNMENT 2")
print("=" * 80)
while True:
    print("\nSelect an operation:")
    print("1. Print complete information of states")
    print("2. Show state with largest area")
    print("3. Show state with largest population")
    print("4. Show population density of all states")
    print("5. Show state with highest population density")
    print("6. Show sorted states by population")
    print("7. Show sorted states by area")
    print("8. Exit")
    
    choice = input("\nEnter your choice (1-8): ")
    
    if choice == '1':
        print("\nComplete States Information:")
        print(states_df.to_string(index=False))
    
    elif choice == '2':
        print(f"\nState with Largest Area: {largest_area_state} ({largest_area:,} sq km)")
    
    elif choice == '3':
        print(f"\nState with Largest Population: {largest_population_state} ({largest_population:,} people)")
    
    elif choice == '4':
        print("\nPopulation Density of States:")
        print(states_df[['State_Name', 'Population_Density']].to_string(index=False))
    
    elif choice == '5':
        print(f"\nState with Highest Population Density: {highest_density_state} ({highest_density:.2f} people/sq km)")
    
    elif choice == '6':
        sorted_by_pop = states_df.sort_values('Population', ascending=False)
        print("\nStates Sorted by Population (Descending):")
        print(sorted_by_pop[['State_Name', 'Population']].to_string(index=False))
    
    elif choice == '7':
        sorted_by_area = states_df.sort_values('Area_sq_km', ascending=False)
        print("\nStates Sorted by Area (Descending):")
        print(sorted_by_area[['State_Name', 'Area_sq_km']].to_string(index=False))
    
    elif choice == '8':
        print("Exiting...")
        break
    
    else:
        print("Invalid choice! Please try again.")
