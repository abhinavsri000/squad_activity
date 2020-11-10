
"""
Class to Represent Parking Lot and associated methods.

-> Data Members :

    capacity // indicates the capacity of the ParkingLot
    slot_id // indicates the Slot_id of the slots
    total_occupied_slots // indicates the number of Ocuupied Slots
    slots // Structure to actually hold the Slots

-> Methods :
    __init__()
    get_Slots()
    allocate_parking_lot( capacity )
    get_vacant_slots()
    park_car( car )
    leave( slot_id )
    get_registraion_no_from_age( age )
    get_slot_no_from_regno( registraion_no )
    get_slot_no_from_age( age )

"""

from entities.car import Car
from entities.driver import Driver

class Parking_Lot:

    # =========================
    # constructer
    # =========================

    def __init__(self):
        self.capacity = 0
        self.slot_id = 0
        self.total_occupied_slots = 0
        self.slots = None

    # ========================
    # Getter for Slots structure
    # ========================

    def get_slots(self):
        print(self.slots)

    # ========================
    # Allocate Parking Slots
    # ========================

    def allocate_parking_lot(self, capacity):
        self.slots = [-1] * capacity
        self.capacity = capacity
        return self.capacity

    # ========================
    # Getter for Vacant Slots
    # ========================

    def get_vacant_slot(self):
        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                return i

    # ========================
    # Method to Park Vehicle
    # ========================

    def park_vehicle(self, car, size=1):
        if self.total_occupied_slots < self.capacity:
            id = self.get_vacant_slot()
            size = 1
            self.slots[id] = car
            self.slot_id = self.slot_id + 1
            self.total_occupied_slots = self.total_occupied_slots + size
            return id + 1
        else:
            return -1

    # ========================
    # Method to vacate Slot
    # ========================

    def leave(self, slot_id, size=1):
        if self.total_occupied_slots > 0 and self.slots[slot_id - 1] != -1:
            regno = self.slots[slot_id - 1].regno
            driver = self.slots[slot_id - 1].driver
            age = driver.age
            self.slots[slot_id - 1] = -1
            self.total_occupied_slots = self.total_occupied_slots - size
            return (regno, age)
        else:
            return (-1, -1)
