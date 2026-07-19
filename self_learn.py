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

# 3. Transport Factory
class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

class Truck(Transport):
    def deliver(self):
        return "Delivering by land in a truck."

class Ship(Transport):
    def deliver(self):
        return "Delivering by sea in a cargo ship."

class Plane(Transport):
    def deliver(self):
        return "Delivering by air in an airplane."

def create_transport(transport_type):
    if transport_type == "truck":
        return Truck()
    elif transport_type == "ship":
        return Ship()
    elif transport_type == "plane":
        return Plane()
    return 

t1 = create_transport("truck")
t2 = create_transport("ship")
t3 = create_transport("plane")
print(t1.deliver())
print(t2.deliver())
print(t3.deliver())

#4. Report Exporter
class ReportExporter(ABC):
    @abstractmethod
    def export(self):
        pass

class PDFExporter(ReportExporter):
    def export(self):
        return "Exporting report as PDF"

class CSVExporter(ReportExporter):
    def export(self):
        return "Exporting report as CSV"

class JSONExporter(ReportExporter):
    def export(self):
        return "Exporting report as JSON"

def create_exporter(export_type):
    if export_type == "pdf":
        return PDFExporter()
    elif export_type == "csv":
        return CSVExporter()
    elif export_type == "json":
        return JSONExporter()
    return 

exp1 = create_exporter("pdf")
print(exp1.export())
exp2 = create_exporter("csv")
print(exp2.export())
exp3 = create_exporter("json")
print(exp3.export())