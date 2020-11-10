
def parse_file(input_file):
    with open(input_file , 'r') as file:
        lines = [line.rstrip() for line in file]
    return lines
