import random
import time
from timer_module import timer
import logging

logging.basicConfig(filename="zombie.log", level=logging.INFO)

class Person:
    
	# People don't die just their energy decreases. Because over the years they have become immune to zombies.

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.scores = 0
        self.weapon = ["gun", "rifle", "knife", "sword", "RPG-7", "pickaxe", "shovel"]
        
    def take_damage(self, damage):
        self.health -= damage
        return self.health

    def calculate_score(self, zombie):
        if isinstance(zombie, BossZombie):
            self.scores += 100
            return f"Congratulations, your point is {self.scores}. You earned 100 points because you killed the '{zombie.name} zombie'"
        elif isinstance(zombie, FastZombie):
            self.scores += 50
            return f"Congratulations, your point is {self.scores}. You earned 50 points because you killed the '{zombie.name} zombie'"
        elif isinstance(zombie, TankZombie):            
            self.scores += 75
            return f"Congratulations, your point is {self.scores}. You earned 75 points because you killed the '{zombie.name} zombie'"
        elif isinstance(zombie, AngryZombie):            
            self.scores += 60
            return f"Congratulations, your point is {self.scores}. You earned 60 points because you killed the '{zombie.name} zombie'"
        elif isinstance(zombie, Zombie):            
            self.scores += 25
            return f"Congratulations, your point is {self.scores}. You earned 25 points because you killed the '{zombie.name} zombie'"
        return self.scores

    @timer
    def attack(self, zombie):
        weapon = random.choice(self.weapon)
        if isinstance(zombie, Zombie):
            return f"When you see the {zombie.name} zombie; Run! Run faster! and suddenly turn back, attack and use the {weapon}!!!"
        return "There's nothing to attack!"

import time
from timer_module import timer
from datetime import datetime
import logging

class Zombie:
   
    def __init__(self, name):
        self.name = name
        self.speed = 5
        self.damage = 10
        self.action = ["bite", "scratch"]
        self.health = 100

    @timer
    def attack_human(self, person):
        action = random.choice(self.action)
        if action == "bite":
            person.take_damage(5)
        elif action == "scratch":
            person.take_damage(2)
        time.sleep(5)
        return f"{self.name} {action}es you! Your health: {person.health}"

    def move(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"{self.name} moved at {timestamp}"
        logging.info(log_message)
        return log_message
    
    def heal(self, amount: int, person):
        self.health += amount
        return f"{self.name} healed! Health: {self.health}. Because {self.name} attack {person.name} and ate brains!"

    def __str__(self):
        return f"{self.name} (Speed: {self.speed}, Damage: {self.damage})"

    def roar(self):
        print("Braaainsss...!")
        
    def zombie_take_damage(self):
        weapon_damage = {"gun": 20, "rifle": 30, "knife": 10, "sword": 15, "RPG-7": 50, "pickaxe": 10, "shovel": 10}
        weapon = random.choice(list(weapon_damage.keys()))
        damage = weapon_damage[weapon]
        self.health -= damage
        return f"{self.name} took {damage} damage from {weapon}! Health is now {self.health}."

class BossZombie(Zombie):
    def __init__(self, name="Boss"):
        super().__init__(name)
        self.health = 150 
        self.damage = 20

class FastZombie(Zombie):
    def __init__(self, name="Fast"):
        super().__init__(name)
        self.speed = 10
        self.damage = 5
        self.action = ["pounce", "claw"]

    def attack_human(self, person):
        action = random.choice(self.action)
        if action == "pounce":
            person.take_damage(7)
        elif action == "claw":
            person.take_damage(3)
        time.sleep(0.5)
        return f"{self.name} {action}es you quickly! Your health: {person.health}"

class TankZombie(Zombie):
    def __init__(self, name="Tank"):
        super().__init__(name)
        self.speed = 2
        self.health = 200
        self.damage = 15
        self.action = ["smash", "slam"]

    def attack_human(self, person):
        action = random.choice(self.action)
        if action == "smash":
            person.take_damage(18)
        elif action == "slam":
            person.take_damage(12)
        time.sleep(2)
        return f"{self.name} {action}es you heavily! Your health: {person.health}"

class AngryZombie(Zombie):
    def __init__(self, name="Angry", target=Person):
        super().__init__(name)
        self.target = target
        self.speed = 7
        self.damage = 12
        self.action = ["thrash", "bite furiously"]

    def attack_human(self, person):
        action = random.choice(self.action)
        if action == "thrash":
            person.take_damage(15)
        elif action == "bite furiously":
            person.take_damage(10)
        time.sleep(1.5)
        return f"{self.name} {action}es you with rage! Your health: {person.health}"

# Example Usage:
person = Person("Jonathan")
normal_zombie = Zombie("Crawler")
boss = BossZombie()
fast_zombie = FastZombie()
tank_zombie = TankZombie()
angry_zombie = AngryZombie()

# Basic Attack & Scoring
print(person.attack(normal_zombie))		# Random weapon selection
print(person.take_damage(normal_zombie.damage))		# Health reduction
print(person.calculate_score(normal_zombie))		# Score update
print(person.scores)
print("-" * 20)
print(person.attack(boss))
print(person.take_damage(boss.damage))
print(person.calculate_score(boss))
print(person.scores)
print("-" * 20)
print(person.attack(tank_zombie))
print(person.take_damage(tank_zombie.damage))
print(person.calculate_score(tank_zombie))
print(person.scores)
print("-" * 20)
print(angry_zombie.attack_human(person))
print("-" * 20)
print(normal_zombie.attack_human(person))
print(normal_zombie.attack_human(person))

# Zombie Healing Mechanic
print(normal_zombie.heal(5, person))		# Zombie regains health
print("-" * 20)

# Movement Logging (check zombie.log file)
print(normal_zombie.move())		# Logs to zombie.log & returns message
print("-" * 20)
print(normal_zombie.zombie_take_damage())


















