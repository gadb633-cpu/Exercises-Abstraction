from abc import abstractmethod,ABC
# 1. Create Different Notifications
class Notification(ABC):
    @abstractmethod
    def get_sending_message(self):
        pass

class EmailNotification(Notification):
    def get_sending_message(self):
        return "Send an Email notification"

class SMSNotification(Notification):
    def get_sending_message(self):
        return "Send an SMS notification"

def create_notification(notification_type):
    if notification_type == "email":
        return EmailNotification()
    elif notification_type == "sms":
        return SMSNotification()
    return 

notif1 = create_notification("email")
print(notif1.get_sending_message())

notif2 = create_notification("sms")
print(notif2.get_sending_message())

# 2. Animal Factory
class Animal(ABC):
    @abstractmethod
    def get_sound(self):
        pass

class Dog(Animal):
    def get_sound(self):
        return "woof!"

class Cat(Animal):
    def get_sound(self):
        return "meow!"

class Bird(Animal):
    def get_sound(self):
        return "tweet!"

def create_animal(animal_type):
    if animal_type == "dog":
        return Dog()
    elif animal_type == "cat":
        return Cat()
    elif animal_type == "bird":
        return Bird()
    return 

animal1 = create_animal("dog")
print(animal1.get_sound())  
animal2 = create_animal("cat")
print(animal2.get_sound())  
animal3 = create_animal("bird")
print(animal3.get_sound())  