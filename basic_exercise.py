from abc import ABC,abstractmethod
# 1. Abstract Delivery Method
class DeliveryMethod(ABC):
    @abstractmethod
    def deliver(self,order_id):
        pass
class BikeDelivery(DeliveryMethod):
    def deliver(self,order_id):
        return f"Order {order_id} delivered by bike."
SkyEx = BikeDelivery()
print(SkyEx.deliver(101)) 

# 2. Two Delivery Types
class DeliveryMethod(ABC):
    @abstractmethod
    def deliver(self,order_id):
        pass
class DroneDelivery(DeliveryMethod):
    def deliver(self,order_id):
        return f"Order {order_id} dropped by drone at your door."
class CarDelivery(DeliveryMethod):
    def deliver(self,order_id):
        return f"Order {order_id} brought to your building by car."
SpeedRiders = DroneDelivery()
print(SpeedRiders.deliver(202))
car1 = CarDelivery()
print(car1.deliver(202))

# 3. Abstract with Constructor
class DeliveryMethod(ABC):
    def __init__(self,company_name):
        self.company_name =company_name
    @abstractmethod
    def deliver(self,order_id):
        pass
class BikeDelivery(DeliveryMethod):
    def __init__(self, company_name):
        super().__init__(company_name)
    def deliver(self,order_id):
        return f"[{self.company_name}] Order {order_id} — bike delivery."
class DroneDelivery(DeliveryMethod):
    def __init__(self, company_name):
        super().__init__(company_name)    
    def deliver(self,order_id):
        return f"[{self.company_name}] Order {order_id} — drone delivery."    
SkyEx = DroneDelivery("SkyEx")
SpeedRiders = BikeDelivery("SpeedRiders")
print(SkyEx.deliver(303))
print(SpeedRiders.deliver(303))

# 4. Multiple Abstract Methods
class DeliveryMethod(ABC):
    @abstractmethod
    def deliver(self,order_id):
        pass
    @abstractmethod
    def get_eta(self):
        pass
class BikeDelivery(DeliveryMethod):
    def deliver(self,order_id):
        return f"Order {order_id} — bike delivery."
    def get_eta(self):
        return f"ETA: {30}minutes"
        
class DroneDelivery(DeliveryMethod):
    def deliver(self,order_id):
        return f"Order {order_id} — drone delivery."
    def get_eta(self):
        return f"ETA: {15}minutes"
SkyEx = DroneDelivery()
SpeedRiders = BikeDelivery()      
print(SkyEx.deliver(1))
print(SpeedRiders.deliver(1))
print(SkyEx.get_eta())
print(SpeedRiders.get_eta())

# 5. Missing Implementation Error
class DeliveryMethod(ABC):
    @abstractmethod
    def deliver(self,order_id):
        pass
class BrokenDelivery(DeliveryMethod):
    def deliver(self,order_id):
        return f"Order {order_id} — broken delivery."
            
broken1 = BrokenDelivery()
print(broken1.deliver(101)) # TypeError: Can't instantiate abstract class BrokenDelivery without an implementation for abstract method 'deliver'

# 6. Static Delivery Fee Calculator
class DeliveryFee:
    @staticmethod
    def calculate(distance_km, rate_per_km):
        return distance_km * rate_per_km
    @staticmethod
    def with_surcharge(base_fee, surcharge_percent):
        return base_fee *(1+surcharge_percent/100)
    @staticmethod
    def is_free(distance_km):
        return True if distance_km<=2.0 else False
print(DeliveryFee.calculate(5,3.0))
print(DeliveryFee.with_surcharge(15.0,10))    
print(DeliveryFee.is_free(1.5))    


    




