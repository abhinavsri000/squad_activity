"""
Helper Utility to parse command line arguments
"""
import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action="store", required=False, dest='src_file', help="Input File")
    return parser

def parse_args():
    parser = create_parser()
    args = parser.parse_args()
    arg = vars(args)
    return arg
