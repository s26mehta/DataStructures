#################################################################################
## Square Interview: Problem: A farmer wants to take a fox, a chicken, and a bag
# of grain across a river. He has only one boat with which he can carry one item
# across the river at once. The only issue is that if the fox and chicken are
# left unsupervised, the fox will eat the chicken. The same goes for the chicken
# and the grain.

# Goal: Print out a series of steps that the farmer could take to transport
# all three items across the river.

# One way the farmer might solve this is to:

# Take chicken over
# Return
# Take fox over
# Return with chicken
# Take grain over
# Return
# Take chicken over
#################################################################################

class State:
    def __init__(self, start=["Fox", "Chicken", "Grain"], dest=[], farmer="start"):
        self.start = start
        self.destination = dest
        self.farmer = farmer

    def is_goal(self):
        if self.farmer is not "destination":
            return False

        if "Fox" not in self.destination:
            return False

        if "Chicken" not in self.destination:
            return False

        if "Grain" not in self.destination:
            return False

        return True

    def is_valid(self):
        if self.farmer == "destination":
            if "Chicken" not in self.destination and "Grain" not in self.destination:
                return False
            if "Fox" not in self.destination and "Chicken" not in self.destination:
                return False
        else:
            if "Chicken" not in self.start and "Grain" not in self.start:
                return False
            if "Fox" not in self.start and "Chicken" not in self.start:
                return False
        return True

    def next_states(self):
        next_states = []

        if self.farmer == "start":
            for item in self.start:
                new_state = State(self.start[:], self.destination[:], self.farmer)
                new_state.start.remove(item)
                new_state.destination.append(item)
                new_state.farmer = "destination"
                next_states.append(new_state)
        else:
            for item in self.destination:
                new_state = State(self.start[:], self.destination[:], self.farmer)
                new_state.destination.remove(item)
                new_state.start.append(item)
                new_state.farmer = "start"
                next_states.append(new_state)

        if self.farmer == "start":
            new_state = State(self.start[:], self.destination[:], self.farmer)
            new_state.farmer = "destination"
            next_states.append(new_state)
        else:
            new_state = State(self.start[:], self.destination[:], self.farmer)
            new_state.farmer = "start"
            next_states.append(new_state)

        return next_states

    def print_state(self):
        print("Farmer is %s" % self.farmer)
        print("Start is %s" % self.start)
        print("Destination is %s" % self.destination)
        print("\n")


# b = State()
# for state in b.next_states():
#     state.print_state()



