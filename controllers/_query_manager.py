""" Class to manage queries on the Parking System .
    Can be Extended to include more queries.
"""

class query_manager:

    # ========================
    # query -> slot_no from Age
    # ========================

    def get_registration_no_from_age(self, parking_lot, age):
        registration_numbers = []

        for i in parking_lot.slots:
            if i != -1 and i.age == age:
                registration_numbers.append(i.regno)

        return registration_numbers

    # ========================
    # query ->  slot_no from Reg_no
    # ========================

    def get_slot_no_from_regno(self,parking_lot, regno):

        for i in range(len(parking_lot.slots)):
            if parking_lot.slots[i].regno == regno:
                return i + 1

        return -1

    # ========================
    # query -> slots from Age
    # ========================

    def get_slot_no_from_age(self, parking_lot, age):
        slotNumbers = []
        for i in range(len(parking_lot.slots)):
            if parking_lot.slots[i] == -1:
                continue
            if parking_lot.slots[i].age == age:
                slotNumbers.append(str(i+1))
        return slotNumbers
