
"""
Class to Represent Parking Lot and associated methods.

-> Data Members :

    capacity // indicates the capacity of the ParkingLot
    slot_id // indicates the Slot_id of the slots
    total_occupied_slots // indicates the number of Ocuupied Slots
    slots // Structure to actually hold the Slots

-> Methods :
    __init__()
    _get_slots()
    allocate_parking_lot( capacity )
    _get_vacant_slots()
    park_car( car )
    leave( slot_id )
    get_registraion_no_from_age( age )
    get_slot_no_from_regno( registraion_no )
    get_slot_no_from_age( age )

"""

from entities.car import Car

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

    def _get_slots(self):
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

    def __get_vacant_slot(self):
        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                return i

    # ========================
    # Method to Park Vehicle
    # ========================

    def park_vehicle(self, regno, age , size=1):
        if self.total_occupied_slots < self.capacity:
            id = self.__get_vacant_slot()
            size = 1
            self.slots[id] = Car(regno,int(age))
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
            age = self.slots[slot_id - 1].age
            self.slots[slot_id - 1] = -1
            self.total_occupied_slots = self.total_occupied_slots - size
            return (regno, age)
        else:
            return (-1, -1)

    """ def get_registration_no_from_age(self, age):
        registration_numbers = []

        for i in self.slots:
            if i != -1 and i.age == age:
                registration_numbers.append(i.regno)

        return registration_numbers

    # ========================
    # query ->  slot_no from Reg_no
    # ========================

    def get_slot_no_from_regno(self,regno):

        for i in range(len(self.slots)):
            if self.slots[i].regno == regno:
                return i + 1

        return -1

    # ========================
    # query -> slots from Age
    # ========================

    def get_slot_no_from_age(self, age):
        slotNumbers = []
        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                continue
            if self.slots[i].age == age:
                slotNumbers.append(str(i+1))
        return slotNumbers """
