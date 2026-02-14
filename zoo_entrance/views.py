from .forms import userLoginForm
from . models import ZooUser
from django.shortcuts import render, redirect

# Create your views here.

'''
index is the landing page for the zoo app. When a user navigates to the zoo_entrance, Django returns the index.html
index.html is also where the login form lives. The form is submitted, a account is retrieved or created and the user is sent to 
their zoo.
'''
def index(request):
    if request.method == 'POST':
        form = userLoginForm(request.POST)
        # checks if form is valid
        if form.is_valid():
            username = from.cleaned_data['username']
    
    
    #return render(request, 'zoo_entrance/index.html')
