# Reads landing_dispersion_main_only and checks impact velocity. 
# If, for a simulation, it is too high, it will remove that data point
# Returns a dictionary of the removed data points. 
# Key = Parachute Area

def impact_errors(file_name):
    return 0


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
        
    #create error_analysis.txt file with open() method
    file_path = "error_analysis.txt"

    with open(file_path, "a") as file:
        #"a" stands for append, we want to add to the file instead of overwriting what's already in the file
        #create file if it does not already exist

        for key in impact: #traverse through dictionary
            file.write("Landing Error: speed was " + str(impact[key][0]) + " m/s " + str(impact[key][1]) + "\n")
        
        for key in cord:
            file.write("Shock Error: cord experienced " + str(cord[key][0]) + " N, " + "speed was " + str(cord[key][1]) + " m/s " + str(cord[key][2]) + "\n")
