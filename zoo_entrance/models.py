from django.db import models



# USER MODEL
class ZooUser(models.Model):
    # ATTRIBUTES
    username = models.CharField(max_length = 25, unique = True)
    # we are forgoing password for now to limit complexity
    # password = models.CharField(max_length = 25)

    # METHODS
    def __str__(self):
        return f"{self.username}"
    
    

# ZOO MODEL
class Zoo(models.Model):
    # ATTRIBUTES
    zoo_user = models.ForeignKey(ZooUser, on_delete=models.CASCADE)
    zoo_name = models.CharField(max_length = 25, unique = True)
    # potential attribute for making a public zoos page for everyone to see
    # public = models.BooleanField()


    # METHODS
    def __str__(self):
        return f"{self.zoo_name}"
    


# ANIMAL MODEL
class ZooAnimal(models.Model):
    # ATTRIBUTES
    zoo = models.ForeignKey(Zoo, on_delete=models.CASCADE)
    nickname = models.CharField(max_length = 25, unique = True)
    species = models.CharField(max_length = 25)
    food = models.CharField(max_length=50)


    # METHODS
    def __str__(self):
        return f"{self.nickname}"
    
    def feed(self):
        pass