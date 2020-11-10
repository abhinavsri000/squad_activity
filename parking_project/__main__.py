# Author : Abhinav Srivastava <abhinavsri000@gmail.com>

""" Entry Point of the Automatic Ticketing System Application
"""

from helpers.parse_arg_helper import parse_args
from helpers.file_io_helper import parse_file
from controllers import _dispatcher
from entities.parking_lot import Parking_Lot


def main():

    """ The function takes command-line argument.
        @param - File Name of the InputFile
    """

    # ==================================
    # Global Parking_lot Object
    # ==================================

    parking_lot = Parking_Lot()

    # Parsing the command line argument
    arg = parse_args()
    input_file_path = arg['src_file']


    if input_file_path == None:
        print("No Input File Found.\nPlease Provide a File_Path. Use -h for more help")

    else:
        # Dispatcher.execute is called to execute the commands one by one.
        try:
            instructions = parse_file(str(input_file_path))
            for instruction in instructions:
                _dispatcher.execute(parking_lot,instruction)

        except TypeError:
            return
        except:
            print("Invalid File")

if __name__ == '__main__':
    main()
