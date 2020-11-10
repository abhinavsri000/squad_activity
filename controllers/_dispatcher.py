"""
Utility to dispatch the commands
"""

from globals.global_mappings import *
from entities.car import Car
from entities.driver import Driver
from controllers._query_manager import query_manager

def execute(parking_lot,instruction):

    # Split commands and @params from instruction

    cmd , arg = instruction.split(" ",1)
    query = query_manager()
    # ===============================================
    # Case for Allocating Parking with number of slots
    # ===============================================

    if cmd == CREATE_PARKING_LOT:
        capacity = int(arg)
        capa = parking_lot.allocate_parking_lot(capacity)
        print('Created parking of '+str(capa)+' slots')

    # ===============================================
    # Case for Parking the car
    # ===============================================

    elif cmd == PARK:
        regno = arg.split(' ')[0]
        age = arg.split(' ')[2]
        car = Car(regno,Driver(age))
        slot_booked = parking_lot.park_vehicle(car)
        if slot_booked == -1:
            print("Parking Full")
        else:
            print('Car with vehicle registration number “' + str(regno) + '” has been parked at slot number ' + str(slot_booked))

    # ===============================================
    # Case for Leaveing the Parking
    # ===============================================

    elif cmd == LEAVE:
        leave_slotid = int(arg)
        car_info = parking_lot.leave(leave_slotid)
        if car_info[0] != -1:
            print('Slot number {} vacated, the car with vehicle registration number “{}” left the space, the driver of the car was of age {}'.format(leave_slotid, car_info[0], car_info[1]))

    # ===============================================
    # Case for querying Vehicle_registration_Number by age
    # ===============================================

    elif cmd == FETCH_SLOTS_USING_DRIVER_AGE:
        age = int(arg)
        regnos = query.get_registration_no_from_age(parking_lot,age)
        print(', '.join(regnos))

    # ===============================================
    # Case for querying the Slot_no by age
    # ===============================================

    elif cmd == FETCH_VEHICLE_REG_NO_FOR_AGE:
        age = int(arg)
        slotnos = query.get_slot_no_from_age(parking_lot,age)
        print(', '.join(slotnos))

    # ===============================================
    # Case for querying slot_no from Registraion No
    # ===============================================

    elif cmd == FETCH_SLOTS_USING_REG_NO:
        regno = arg
        slotno = query.get_slot_no_from_regno(parking_lot,regno)
        if slotno == -1:
            print("Not found")
        else:
            print(slotno)

    # ===============================================
    # Case for exiting the program
    # ===============================================

    elif cmd == EXIT:
        exit(0)
