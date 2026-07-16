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

    




