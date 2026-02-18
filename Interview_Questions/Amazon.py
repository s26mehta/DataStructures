# Amazon lockers come in different sizes. When a delivery person brings a package to a locker they scan the package for
# dimensions and the system should automatically open an empty locker of the smallest size that will accomadate the
# package. Write an algorithm that will pick the correct locker size
#
# locker = [1,2,3,4,5,6,7,10,20,30,400,1000]
# package = [100,3,2,6,7,2,1,100,200,400]
# placement = [400, 3, 2, 6, 7, 4, 1, 100]
#
# locker sizes range from 1 to n?
# package size range from 1 to n?
#
# locker sizes range [small, medium, large] = [4,3,2]
# packages of size [small, medium, large]
# info of package: size, delivery_date, arrival_date, locker_id,




from enum import Enum

class Size(Enum):
    SMALL = 0
    MEDIUM = 1
    LARGE = 2


class LockerStatus(Enum):
    Open = 0
    Closed = 1


class Package:

    def __init__(self, id, dimensions, delivery_date):
        self.id = id
        self.dimensions = dimensions
        self.delivery_date = delivery_date
        self.locker_id = None
        self.size = None

    def set_locker_id(self, locker_id):
        self.locker_id = locker_id

    def remove_locker_id(self):
        self.locker_id = None

    def compute_size(self):
        total_size = self.dimensions[0] * self.dimensions[1] * self.dimensions[
            2]
        if total_size < 4:
            self.size = Size.SMALL
        if total_size >= 4 and total_size < 10:
            self.size = Size.MEDIUM
        if total_size >= 4 and total_size < 10:
            self.size = Size.LARGE
        return self.size


class Locker:

    def __init__(self, id, size):
        self.id = id
        self.size = size
        self.current_status = LockerStatus.Closed


class LockerSystem:

    def __init__(self):
        self.lockers = []  # [small, medium, large]
        self.locker_ids_available = {
            Size.SMALL: [],
            Size.MEDIUM: [],
            Size.LARGE: []
        }
        self.locker_ids_used = set()
        self.codes_to_open_lockers = {}
        self.lockers_under_service = set()

    def add_locker(self, locker):
        if locker.size == Size.SMALL:
            self.locker_ids_available[Size.SMALL].append(locker)
        if locker.size == Size.MEDIUM:
            self.locker_ids_available[Size.MEDIUM].append(locker)
        if locker.size == Size.LARGE:
            self.locker_ids_available[Size.LARGE].append(locker)

    def new_package(self, id, dimensions, delivery_date):
        package = Package(id, dimensions, delivery_date)
        package_size = package.compute_size()
        actual_size_not_available = False
        for locker_size in [e.value for e in Size if e.value >= package_size]:
            if package_size == locker_size:
                while len(self.locker_ids[locker_size]) > 0:
                    locker = self.locker_ids[locker_size].pop()
                    if self.can_locker_open(locker):
                        self.open_locker(locker)
                        return True
                actual_size_not_available = True
            if locker_size > package_size and actual_size_not_available:
                while len(self.locker_ids[locker_size]) > 0:
                    locker = self.locker_ids[locker_size].pop()
                    if self.can_locker_open(locker):
                        self.open_locker(locker)
                        return True
        return False

    def can_locker_open(self, locker):
        if locker not in self.lockers_under_service and locker not in self.locker_ids_used:
            return True
        return False

    def open_locker(self, locker):
        locker.current_status = LockerStatus.Open

    def action_at_locker_close(self, locker):
        self.locker_ids_used.append(locker)

    def open_lock_with_code(self, code):
        if code in self.codes_to_open_lockers:
            for locker in self.codes_to_open_lockers[code]:
                if locker not in self.lockers_under_service:
                    self.open_locker(locker)









#####################################
# Alternate

"""
An Amazon pickup location has a series of lockers for packages to be dropped off and picked up. 
Packages can come in many sizes. We have lockers of varying sizes as well. 
Model the lockers, packages and pickup location and 
implement an algorithm for efficiently finding the best possible empty locker for a given package.
"""


from enum import Enum

class Size(Enum):
    Small = "small"
    Medium = "medium"
    Large = "large"
    XLarge = "xlarge"

class Locker:
    def __init__(self, id, size):
        self.id = id
        self.size = size
        self.package = None

class Package:
    def __init__(self, id, size, weight):
        self.id = id
        self.size = size
        self.weight = weight

class Location:
    def __init__(self, lockers):
        self.lockers = {} # {'small': set(), 'medium': set(), 'large': set()}
        for locker in lockers:
            self.add_new_locker(locker)
        self.used_lockers = set()
        self.in_service_lockers = set()
        self.sizes = [Size.Small, Size.Medium, Size.Large, Size.XLarge]

    def find_locker_for_package(self, package):
        if package.size not in self.lockers or len(self.lockers[package.size]) == 0:
            size_found = False
            for _, size in enumerate(self.sizes):
                if size_found:
                    if size in self.lockers and len(self.locker[size]) > 0:
                        return self.lockers[size].pop()
                if size == package.size:
                    size_found = True
            return None
        return self.lockers[package.size].pop()
                
    def put_package_in_locker(self, package):
        locker = self.find_locker_for_package(package)
        if locker:
            return self.mark_locker_as_used(locker, package)
        else:
            return None
        
    def add_new_locker(self, locker):
        if locker.size not in self.lockers:
            self.lockers[locker.size] = set()
        self.lockers[locker.size].add(locker)
    
    def add_package_to_locker_locker(self, locker, package):
        if locker in self.lockers[locker.size]:
            self.lockers[locker.size].remove(locker)
        self.used_lockers.append(locker)
        locker.package = package
    
    def remove_locker_for_service(self, locker):
        if locker in self.lockers[locker.size]:
            self.lockers[locker.size].remove(locker)
        if locker in self.used_lockers:
            self.used_lockers[locker.size].remove(locker)
        self.in_service_lockers.add(locker)

    def put_locker_for_availability(self, locker):
        self.used_lockers.remove(locker)
        if locker in self.lockers[locker.size]:
            self.lockers[locker.size].remove(locker)
        self.used_lockers.append(locker)