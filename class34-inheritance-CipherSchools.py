class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = max(price,0)
    def make_a_call(self,number):
        return f"calling {number}.."
    def full_name(self):
        return f"{self.brand} {self.model_name}"
    
class SmartPhone(Phone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
        super().__init__(brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera
        
phone = Phone('samsung','J2',700)
smartPhone = SmartPhone('Realme','5s',10000,'4GB','64GB','48MP')
print(phone.full_name())
print(smartPhone.full_name()+ f" and its price is {smartPhone.price}") 
        