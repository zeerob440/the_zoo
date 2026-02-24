from django.contrib import admin
from .models import ZooUser
from .models import Zoo
from .models import ZooAnimal

# Register your models here.
admin.site.register(ZooUser)
admin.site.register(Zoo)
admin.site.register(ZooAnimal)