class Dog:
    
    species = "Canis familiaris"

    def __init__(self, breed, age):
        
        self.breed = breed
        self.age = age

    def display_details(self):
        print("Species:", Dog.species)
        print("Breed:", self.breed)
        print("Age:", self.age, "years")
        print("-" * 30)
dog1 = Dog("Labrador", 3)
dog2 = Dog("German Shepherd", 5)
dog1.display_details()
dog2.display_details()
