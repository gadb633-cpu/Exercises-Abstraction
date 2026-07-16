from abc import ABC,abstractmethod
# 1. Abstract Delivery Method
class DeliveryMethod(ABC):
    @abstractmethod
    def deliver(self,order_id):
        pass
class BikeDelivery(DeliveryMethod):
    def deliver(self,order_id):
        return f"Order {order_id} delivered by bike."
bike1 = BikeDelivery()
print(bike1.deliver(101)) 

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
drone1 = DroneDelivery()
print(drone1.deliver(202))
car1 = CarDelivery()
print(car1.deliver(202))

        
        



