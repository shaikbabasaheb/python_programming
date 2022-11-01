from abc import ABC,abstractmethod

class AbstractionDemo(ABC): 
    @abstractmethod       #abstractmethod
    def HousingInterest(self):
        None
    @abstractmethod      #abstractmethod
    def VehicleInterest(self):
        None
        
class SBI(AbstractionDemo): #concrete class
    def HousingInterest(self):
        print('Housing interest is 8.55')
    def VehicleInterest(self):
        print('Vehicle Interest is 7.55')

obj=SBI()
obj.HousingInterest()
obj.VehicleInterest()
