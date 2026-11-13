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
    return 0