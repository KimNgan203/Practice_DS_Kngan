class Animal:
    def __init__(self, name, age, description):
        self.name = name
        self.age = age
        self.des = description
    
    def xemThongTin(self):
        return f"Tên: {self.name}\nTuổi: {self.age}\nMô tả: {self.des}"
    
    def tiengKeu(self):
        return "Unknown" 

class Tiger(Animal):
    def __init__(self, name, age, description, sound, prey):
        super().__init__(name, age, description)
        self.sound = sound
        self.prey = prey
    
    def xemThongTinHo(self):
        return f"{super().xemThongTin()}\nCon mồi: {self.prey}"
    
    def tiengKeu(self):
        return f"Tiếng kêu: {self.sound}"

class Dog(Animal):
    def __init__(self, name, age, description, sound, breed):
        super().__init__(name, age, description)
        self.sound = sound
        self.breed = breed
    
    def xemThongTinCho(self):
        return f"{super().xemThongTin()}\nGiống chó: {self.breed}"

    def tiengKeu(self):
        return f"Tiếng kêu: {self.sound}"

class Human(Animal):
    def __init__(self, name, age, description, sound, status):
        super().__init__(name, age, description)
        self.sound = sound
        self.status = status
    
    def xemThongTinNguoi(self):
        return f"{super().xemThongTin()}\nTình trạng hôn nhân: {self.status}"
    
    def tiengKeu(self):
        return f"Ngôn ngữ: {self.sound}"

Ho = Tiger("Hổ Việt Nam", "10", "đáng xợ wa", "Grr", "Gì cũng chén")
print(Ho.xemThongTinHo())
print(Ho.tiengKeu())

print(f"\n")

Cho = Dog("Milo", "7", "siêu cute", "Gâu Gâu", "Husky")
print(Cho.xemThongTinCho())
print(Cho.tiengKeu())

print(f"\n")

SinhvienIS = Human("ISers", "20", "thông minh s1tg", "tiếng sao Hỏa", "Ế bền vững")
print(SinhvienIS.xemThongTinNguoi())
print(SinhvienIS.tiengKeu())