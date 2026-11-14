# Reads landing_dispersion_main_only and checks impact velocity. 
# If, for a simulation, it is too high, it will remove that data point
# Returns a dictionary of the removed data points. 
# Key = Parachute Area

import json
from pathlib import Path

max_acceptable_landing_velocity = -5 # negative because going down, max means -4 is too much velocity or speed

def impact_errors(file_name):

    returndict = {}

    # this just makes the file path relative to the script, otherwise its an absolute path relative to the terminal
    # the following two lines are not needed for ipynb files
    script_dir = Path(__file__).resolve().parent
    file_path = script_dir / file_name

    with open(file_path, "r", encoding="utf-8") as file:
        records = [json.loads(line) for line in file if line.strip()]

    for record in records:
        if record["impact_velocity"] < max_acceptable_landing_velocity:
            returndict[record["index"]] = [record["impact_velocity"], record]
            print(f"Unsuccessful run: {record}")
            print()
        else:
            print(f"Successful run: {record}")
            print()
            
        # print(record)

    
    print(returndict)
    return returndict


# Reads landing_dispersion_main_only and checks speed when main opens. 
# If, for a simulation, speed was too high (force analysis)
# Returns a dictionary of the removed data points 
# Key = Parachute Area

def cord_errors(file_name):
    return 0

# Takes both dictionaries from shock and landing errors
# Compiles errors into a document "error_analysis.txt"
# Lists reason of failure (If landing, lists speed. If shock, lists shock force + speed)

def compile_errors(impact, cord):
    return 0


impact_errors("landing_dispersion_main_only.outputs.txt")
