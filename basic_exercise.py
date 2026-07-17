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

# 7. Abstract + Static Togetherד
class DeliveryMethod(ABC):
    @abstractmethod
    def deliver(self,order_id):
        pass
    @abstractmethod
    def get_eta(self):
        pass
class WalkingDelivery(DeliveryMethod):
    def deliver(self,order_id):
        return f"Order {order_id} — walking delivery."

    def get_eta(self):
        self.slow_ETA = 60   
        return self.slow_ETA
class ExpressDelivery(DeliveryMethod):
    def deliver(self,order_id):
        return f"Order {order_id} — experss delivery."
    def get_eta(self):
        self.fast_ETA = 10  
        return self.fast_ETA
class DeliveryHelper(DeliveryMethod):
    @staticmethod
    def faster(d1, d2):
        if d1.get_eta() > d2.get_eta():
            return f"Faster option: {d2.__class__.__name__}"
        else:
            return f"Faster option: {d1.__class__.__name__}"            
d1 = WalkingDelivery()
d2 = ExpressDelivery()
print(DeliveryHelper.faster(d1,d2))

# 8. Notification Abstract Class
class Notifier(ABC):
    @abstractmethod
    def send(self,recipient, message):
        pass
class PushNotifier(Notifier):
    def send(self,recipient, message):
        return f"Push to {recipient}: {message}"
class WhatsAppNotifier(Notifier):
    def send(self,recipient, message):
        return f"WhatsApp to {recipient}: {message}"
class InAppNotifier(Notifier):
    def send(self,recipient, message):
        return f"In-app banner for {recipient}: {message}"
push_no = PushNotifier()
WhatsApp_No = WhatsAppNotifier()
InApp_No = InAppNotifier()
list_instances = [push_no,WhatsApp_No,InApp_No]
for instance in list_instances:
    print(instance.send("customer_42","Your order is on the way!"))

# 8. Notification Abstract Class
class Restaurant(ABC):
    @abstractmethod
    def get_menu(self):
        self.list1 = []
        return self.list1
    @abstractmethod
    def prepare_order(self,item_name):
        pass
class ItalianRestaurant(Restaurant):
    def get_menu(self):
        self.menu = ['pasta', 'pizza', 'tiramisu']
        return self.menu
    def prepare_order(self,item_name):
        return f"{item_name} its make"
class SushiRestaurant(Restaurant):
    def get_menu(self):
        self.menu = ['maki', 'nigiri', 'ramen']
        return self.menu
    def prepare_order(self,item_name):
        return f"{item_name} its make with chopstics"
pizza = ItalianRestaurant()
sushi = SushiRestaurant()
list_restaurant = [pizza,sushi]
for restaurant in list_restaurant:
    print(restaurant.get_menu())
    print(restaurant.prepare_order("chips"))

# 10. Full Delivery Platform
class DeliveryMethod(ABC):
    @abstractmethod
    def deliver(self,order_id):
        pass
    @abstractmethod
    def get_eta(self):
        pass
    @abstractmethod
    def get_cost(self,distance_km):
        pass
class BikeDelivery(DeliveryMethod):
    def deliver(self,order_id):
        return order_id
    def get_eta(self):
        self.ETA = 60
        return self.ETA

    def get_cost(self,distance_km):
        self.distance = distance_km
        return self.distance

class DroneDelivery(DeliveryMethod):
    def deliver(self,order_id):
        return order_id
        
    def get_eta(self):
        self.ETA = 40
        return self.ETA
    def get_cost(self,distance_km):
        self.distance = distance_km
        return self.distance
bike1 = BikeDelivery()
drone1 = DroneDelivery()
class Platform():
    list_delivory = [bike1,drone1]
    def cheapest_option(self,distance_km):
        self.item = self.list_delivory[0].get_cost(distance_km)
        for self.delivory in self.list_delivory:
            if self.delivory.get_cost(distance_km) > self.item:
                self.item = self.delivory.__class__.__name__
        return self.item        
    def fastest_option(self):
        self.item_fastest = self.list_delivory[0].get_eta()
        for self.delivory in self.list_delivory:
            if self.delivory.get_eta() < self.item_fastest:
                self.item_fastest = self.delivory
        return self.item_fastest.__class__.__name__
p = Platform()
print(p.cheapest_option(5.0))
print(p.fastest_option()) 







    




