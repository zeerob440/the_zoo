from django import forms
from .models import ZooUser, Zoo, ZooAnimal
#creates form for user login at zoo_entrance

# Form to allow users to log in
class userLoginForm(forms.Form):
    username = forms.CharField(
        max_length = 25,
        label = 'Enter your name'
    )

    # given no password protected login for expediency and simplicity, logins will be written as lower-case only.
    def clean_username(self):
        username =self.cleaned_data['username']
        return username.strip().lower()


# Form to allow creating new zoos
"""
class ZooCreationForm(forms.Form):
    zoo_name = forms.CharField(
        max_length = 25,
        label = 'Enter a name for the zoo'
    )
    # potential spot to add a boolean to control if zoo is public or not
    # public = forms.BooleanField()
"""
#updated to follow ModelForm
class ZooForm(forms.ModelForm):
    class Meta:
        model = Zoo
        fields = ('zoo_name', 'zoo_location', 'public')


# Form to create new animals
"""
class AnimalCreationForm(forms.Form):
    # we will need to create a dropdown list for valid animals here instead of a character field
    species = forms.CharField(
        max_length = 25,
        label = 'Enter the species'
    )
    nickname = forms.CharField(
        max_length = 25,
        label = 'Give your animal a name'
    )
    # we will need to create a dropdown for valid food here instead of a character field
    food = forms.CharField(
        max_length = 25,
        label = 'Enter what food the animal will eat'
    )
"""
#updated to follow ModelForm
class AnimalForm(forms.ModelForm):
    class Meta:
        model = ZooAnimal
        fields = ('nickname', 'species', 'food')
