import time

def initial_set():
    # Step 1: Create and save the list
    saved_data = []
    saved_data.append("maddie")
    saved_data.append(100)
    saved_data.append(100)
    saved_data.append(100)
    saved_data.append(0)
    saved_data.append(5)
    saved_data.append(50)
    saved_data.append(0)
    saved_data.append(10)
    saved_data.append(time.time())
    saved_data.append(time.time())

    print("Original List:", saved_data)
    print("Name:", saved_data[0])
    print("Health:", saved_data[1])
    print("Happiness:", saved_data[2])
    print("Hygiene:", saved_data[3])
    print("Age:", saved_data[4])
    print("Weight:", saved_data[5])
    print("Intelligence:", saved_data[6])
    print("Hunger:", saved_data[7])
    print("Strength:", saved_data[8])
    print("First Interaction Time:", saved_data[9])
    print("Most Recent Interaction Time:", saved_data[10])
    
    # Step 2: Save to file
    with open("stats.txt", "w") as file:
        # Use a comma to separate items and convert all to strings
        file.write(", ".join(map(str, saved_data)))
    return saved_data

def initial_return():
    # Step 3: Read from file and convert back to list
    with open("stats.txt", "r") as file:
        # Read the file content
        data = file.read()
        # Split the string back into a list
        data_list = data.split(", ")

    # Optional: Convert numeric strings back to floats/integers
    data_list[1:] = [float(item) if '.' in item else int(item) for item in data_list[1:]]

    print("Data List:", data_list)
    print("First Element of Data List:", data_list[0])
    return data_list


initial_set()