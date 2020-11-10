import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action="store", required=False, dest='src_file', help="Input File")
    args = parser.parse_args()
    arg = vars(args)
    return arg
