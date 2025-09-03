class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        self.mapping = {1: "B", 2: "M", 3:"S"}

    def addCar(self, carType: int) -> bool:
        # get car type
        if self.mapping[carType] == "B":
            self.big -= 1
            return True if self.big >= 0 else False
        elif self.mapping[carType] == "M":
            self.medium -= 1
            return True if self.medium >= 0 else False
        else:
            self.small -= 1
            return True if self.small >= 0 else False



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

"""
Plan:
b = 1
m = 1
s = 0

add(2)
m = 0
return true

add (2)
m = -1
return false
"""