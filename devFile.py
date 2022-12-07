import numpy as np

class territory: 
    def __init__(self, terrCode, name, value, adjacentTerr, buildings, stationedUnits): 
        self.terrCode = terrCode
        self.name = name
        self.value = value
        self.adjacentTerr = adjacentTerr
        self.buildings = buildings
        self.stationedUnits = stationedUnits
    def build(self): 
        print("builtBuilding")
    def moveUnit(self, destinationTerr):
        stayInFunc = True
        while stayInFunc:
            if (not destinationTerr.terrCode in self.adjacentTerr):
                print("Territories are not adjacent. Please try again!")
                stayInFunc = False
            else:         
                print("Current units stationed in " + self.name + ":")
                for key, value in self.stationedUnits.items():
                    print(key + ": " + str(value)) 
                unitsToMove = {}
                print("\nUnits to move to " + destinationTerr.name + ":")
                # Unit selection prompt and validity check
                for key in self.stationedUnits.keys():
                    cont = True
                    while cont:
                        try:
                            numToMove = input(key + ": ")
                            numToMove = int(numToMove)
                            while cont:
                                if (numToMove <= self.stationedUnits[key]) & (numToMove >= 0):
                                    unitsToMove.update({key : numToMove})
                                    cont = False
                                else:
                                    print("Number must be zero or positive and not greater than available unit type in current territory. Try again!")
                                    break  
                        except:
                            print("Please provide a number, not a word!")
                # Moving units
                for key, value in unitsToMove.items():
                    newCountOrigin = self.stationedUnits[key] - unitsToMove[key]
                    self.stationedUnits.update({key : newCountOrigin})
                    newCountDestination = destinationTerr.stationedUnits[key] + unitsToMove[key]
                    destinationTerr.stationedUnits.update({key : newCountDestination}) 
            stayInFunc = False


### Test
a = territory(1, "countryA", 3, [2,3], np.nan, {"infantry":2}) 
b = territory(2, "countryB", 1, [1], np.nan, {"infantry":1}) 
c = territory(3, "countryC", 1, [1], np.nan, {"infantry":3}) 
