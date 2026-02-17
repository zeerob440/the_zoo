from django.db import models

# Create your models here.

#user model
class ZooUser(models.Model):
    username = models.CharField(max_length = 25, unique = True)

    def __str__(self):
        return self.username


# animal model
class Zoo(models.Model):
    zoo_name = models.CharField(max_length = 25, unique = True)

    def __str__(self):
        return self.zoo_name

