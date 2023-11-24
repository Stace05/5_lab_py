class RaceHorse:
    def __init__(self, name, speed, age):
        self.__name = name
        self.__speed = speed
        self.__age = age
        self.__placeInRace = None
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    
    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self, new_speed):
        self.__speed = new_speed
    
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, new_age):
        self.__age = new_age
    
    @property
    def placeInRace(self):
        return self.__placeInRace
    @placeInRace.setter
    def placeInRace(self, new_placeInRace):
        self.__placeInRace = new_placeInRace
        
    
class Race:
    def __init__(self):
        self.participants = []

    def add_participant(self, horse):
        if 3 <= horse.age <= 7:
            self.participants.append(horse)

    def remove_participant(self, horse):
        if horse in self.participants:
            self.participants.remove(horse)

    def calculate_winner(self):
        avg_age = sum(horse.age for horse in self.participants) / len(self.participants)
        
        def comparison(horse):
            return (horse.speed, horse.age - avg_age)
        
        sorted_participants = sorted(self.participants, key=comparison, reverse=True)
        
        for i, horse in enumerate(sorted_participants[:3]):
            horse.placeInRace = i + 1
            print(f"Place {i + 1}: {horse.name}")
        return sorted_participants[0]

race = Race()
horse1 = RaceHorse("Horse1", 25, 3)
horse2 = RaceHorse("Horse2", 24, 7)
horse3 = RaceHorse("Horse3", 20, 4)
horse4 = RaceHorse("Horse4", 31, 4)  
race.add_participant(horse1)
race.add_participant(horse2)
race.add_participant(horse3)
race.add_participant(horse4)

winner = race.calculate_winner()

