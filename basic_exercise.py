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


