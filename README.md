## Parking System
## Dependencies

- Python 3.+ (written in 3.8.5)
Make sure python 3.+ is installed and is added to the PATH. The project is not backward compatible to python 2.+.

## Project Structure

[] parking_project directory is the Project directory.

├── ...<br/>
├── ...<br/>
├── parking_project<br/>
│   └── controllers<br/>
│   │   ├── _dispatcher.py<br/>
│   │   ├── _query_manager.py<br/>
│   └── entities<br/>
│   │    ├── _vehicle.py<br/>
│   │    ├── car.py<br/>
│   │    ├── driver.py<br/>
│   │    ├── parking_lot.py<br/>
│   └── globals<br/>
│   │    ├── gloabal_mappings.py<br/>
│   └── helpers<br/>
│   │    ├── file_io_helper.py<br/>
│   │    ├── parse_arg_helper.py<br/>
│   └── resources<br/>
│   │    ├── inputs<br/>
│   │    |   ├── input1.txt<br/>
│   │    |   ├── input2.txt<br/>
│   │    |   ├── input3.txt<br/>
│   │    |   ├── sample_input.txt<br/>
│   └── tests<br/>
│   │    ├── test_resources<br/>
│   │    |   ├── input<br/>
│   │    |   |   ├── input0.txt<br/>
│   │    |   |   ├── input1.txt<br/>
│   │    |   |   ├── input2.txt<br/>
│   │    ├──test.py<br/>
│   └── __main__.py<br/>
│   └── sample_input.txt<br/>
├── ...<br/>
├── ...<br/>


## Setup Instructions

1. Clone the repository : $ git clone https://github.com/abhinavsri000/squad_activity.git
2. $ cd squad_activity
3. Activate the virtual env : $ source env/bin/activate or . env/bin/activate
4. $ cd parking_project
5. Run `python3 __main__.py -f <absolute or relative input file path>`

examples :<br/>
    Run `python3 __main__.py -f ./resources/inputs/sample_input.txt` or<br/>
    Run `python3 __main__.py -f ./sample_input.txt` or<br/>
    Run `python3 __main__.py -f ../sample_input.txt` or<br/>


## Run Tests
1. Clone the repository : $ git clone https://github.com/abhinavsri000/squad_activity.git
2. $ cd squad_activity
3. Activate the virtual env : $ source env/bin/activate or . env/bin/activate
4. $ cd parking_project
5. Run `python3 -m tests.test_helpers` or
Run `python3 -m tests.test_query_manager`


## Problem Description

We own a parking lot that can hold up to ‘n’ cars at any given point in time. Each slot is given a number starting at one increasing with increasing distance from the entry point in steps of one. We want to create an automated ticketing system that allows our customers to use our parking lot without human intervention.

When a car enters the parking lot, we want to have a ticket issued to the driver. The ticket issuing process includes:-

We are taking note of the number written on the vehicle registration plate and the age of the driver of the car.

And we are allocating an available parking slot to the car before actually handing over a ticket to the driver (we assume that our customers are kind enough to always park in the slots allocated to them).

The customer should be allocated a parking slot that is nearest to the entry. At the exit, the customer returns the ticket, marking the slot they were using as being available.

Due to government regulation, the system should provide us with the ability to find out:-
1. Vehicle Registration numbers for all cars which are parked by the driver of a certain age,
2. Slot number in which a car with a given vehicle registration plate is parked.
3. Slot numbers of all slots where cars of drivers of a particular age are parked.

We interact with the system via a file-based input system, i.e. it should accept a filename as an input. The file referenced by filename will contain a set of commands separated by a newline, we need to execute the commands in order and produce output.
