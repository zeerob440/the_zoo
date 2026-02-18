from django.db import models



# USER MODEL
class ZooUser(models.Model):
    # ATTRIBUTES
    username = models.CharField(max_length = 25, unique = True)
    # we are forgoing password for now to limit complexity
    # password = models.CharField(max_length = 25)
    owned_zoos = models.TextField()

    # METHODS
    def __str__(self):
        return f"{self.username} is the current user."
    
    def list_zoos(self):
        pass
    
    def add_zoo(self):
        pass

    def remove_zoo(self):
        pass


# ZOO MODEL
class Zoo(models.Model):
    # ATTRIBUTES
    zoo_user = models.ForeignKey(ZooUser, on_delete=models.CASCADE)
    zoo_name = models.CharField(max_length = 25, unique = True)
    owned_animals = models.TextField()


    # METHODS
    def __str__(self):
        return f"{self.zoo_name} is owned by {self.zoo_user}."
    
    def list_animals(self):
        pass
    
    def add_animal(self):
        pass

    def remove_animal(self):
        pass


# ANIMAL MODEL
class ZooAnimal(models.Model):
    # ATTRIBUTES
    zoo = models.ForeignKey(Zoo, on_delete=models.CASCADE)
    nickname = models.CharField(max_length = 25, unique = True)
    species = models.CharField(max_length = 25)
    food = models.CharField(max_length=50)


    # METHODS
    def __str__(self):
        return f"{self.nickname} is a {self.species} in {self.zoo}."
    
    def feed(self):
        pass