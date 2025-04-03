import random


class Character:
    def __init__(self,n,h,a,d,s):

        self.char_name=n
        self.health=h
        self.attack_power=a
        self.defence=d
        self.speed=s
    def attack(self,target):
        target.take_damage(self.attack_power)
    
    def take_damage(self,amount):
        self.health -= amount

    def is_alive(self):
        if self.health<=0:
            return False
        return True

class Warrior(Character):
    def __init__(self,rage, n, h, a, d, s):
        super().__init__(n, h, a, d, s)
        self.rage=rage
        
    
    def bersekMode(self,health):
        if health <30:
            self.attack_power =2 * self.attack_power #POWER DOUBLES 
    
class Mage(Character):
    def __init__(self,mana, n, h, a, d, s):
        super().__init__(n, h, a, d, s)
        self.mana=mana
    
    def fireBall(self,damage):
        if self.mana >= 10: 
            damage = self.attack_power + 10 
            self.target.take_damage(damage)
            self.health -= 5  
            self.mana -= 10


class Archer(Character):
    def __init__(self,cc, n, h, a, d, s):
        super().__init__(n, h, a, d, s)
        self.critical_chance=cc 
    

        def precisionShot(self,target):
            if random.random()<=self.critical_chance : #30%
                damage= self.attack_power *2
            else:
                damage=self.attack_power
            target.take_damage(damage)
    
