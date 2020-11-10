"""
This is a Utility to parse a file.
"""

def parse_file(input_file):
    try:
        with open(input_file , 'r') as file:
            lines = [line.rstrip() for line in file]
        return lines
    except:
        print("No file found on the path provided")
        return
