# 5 floors
# 20 spaces per floor
from enum import Enum

class Ticket:
    # id: String
    # floor: String
    def __init__(self, id, floor, car):
        self.id = id
        self.floor = floor
        self.car = car
"""

floor_list = [0,0,0,0,0]
tickets = {
    ticket_id => [ticket, floor]
    2 => []
    3 => []
    4 => []
    5 => []
}

"""


class CarSize(Enum):
    COMPACT = "COMPACT"
    STANDARD = "STANDARD"

class Car:
    def __init__(self, size):
        self.size = size
        
class Garage:
    def __init__(self, total_floors, compact_spaces_per_floor, standard_spaces_per_floor):
        
        self.floors = []
        for i in range(total_floors):
            self.floors.append([0,0]) # (compact_spaces, standard_spaces)
        self.tickets = {}
        self.max_compact_spaces_per_floor = compact_spaces_per_floor
        self.standard_spaces_per_floor = standard_spaces_per_floor
        self.next_ticket_id = 0
        
    def enter(self, car):
        open_floor_with_compact_space = None
        open_floor_with_standard_space = None
        
        # Find floor with open space
        for idx, cur_floor_occupancy in enumerate(self.floors):
            cur_floor_compact_occupancy = cur_floor_occupancy[0]
            cur_floor_standard_occupancy = cur_floor_occupancy[1]
            
            if car.size == CarSize.COMPACT.value:
                if cur_floor_compact_occupancy < self.max_compact_spaces_per_floor:
                    open_floor_with_compact_space = idx+1
                    break
                if open_floor_with_standard_space is None or open_floor_with_standard_space < self.standard_spaces_per_floor:
                    open_floor_with_standard_space = idx+1
            elif car.size == CarSize.STANDARD.value:
                if cur_floor_standard_occupancy < self.standard_spaces_per_floor:
                    open_floor_with_standard_space = idx+1
                    break
        
        # Check if floor found        
        if open_floor_with_compact_space is None and open_floor_with_standard_space is None:
            raise Exception("Parking Garage is full")
        
        # Create new Ticket
        open_floor = open_floor_with_standard_space
        compact_spot_used = False
        if car.size == CarSize.COMPACT.value and open_floor_with_compact_space is not None:
            open_floor = open_floor_with_compact_space
            compact_spot_used = True
            
        new_ticket = Ticket(self.next_ticket_id, open_floor, car)
        
        self.next_ticket_id += 1
        self.tickets[new_ticket.id] = new_ticket
        
        if compact_spot_used:
            self.floors[open_floor-1][0] += 1
        else:
            self.floors[open_floor-1][1] += 1
        
        return new_ticket
        
    def exit(self, ticket):
        # Remove occupancy from ticket floor
        ticket_floor = ticket.floor - 1
        car = ticket.car
        
        if car.size == CarSize.COMPACT.value:
            self.floors[ticket_floor][0] -= 1
        else:
            self.floors[ticket_floor][1] -= 1
        
        # Delete ticket from ticket queue
        del self.tickets[ticket.id]
        
        
garage = Garage(5, 12, 10)
prev_ticket = None
compact_car = Car(CarSize.COMPACT.value)
standard_car = Car(CarSize.STANDARD.value)

for i in range(100):
    ticket = garage.enter(compact_car)
    print("Compact Ticket %s" % i, ticket.id, ticket.floor)
    print(garage.floors)
    
    ticket1 = garage.enter(standard_car)
    print("Standard Ticket %s" % i, ticket1.id, ticket1.floor)
    print(garage.floors)
    
    
    if i % 5 == 0 and prev_ticket != None:
        print("Exiting garage", prev_ticket.id)
        garage.exit(prev_ticket)
        # print(garage.tickets, garage.floors)
    
    prev_ticket = ticket
    