from .forms import userLoginForm
from django.shortcuts import render, redirect
# data models below
from . models import ZooUser
from .models import Zoo
from .models import ZooAnimal

# Create your views here.

'''
index is the landing page for the zoo app. When a user navigates to the zoo_entrance, Django returns the index.html
index.html is also where the login form lives. The form is submitted, a account is retrieved or created and the user is sent to 
their zoo. For simplicity, users simply login with their name, if the name is not written into the database, the account is 
simply created. While not secure enough for a true enterprise application, this method was chosen for expediency. 

'''
def index(request):
    if request.method == 'POST':
        form = userLoginForm(request.POST)
        # checks if form is valid, if so runs cleaned_data
        if form.is_valid():
            username = form.cleaned_data['username']

        # uses Django function get_or_create to get a user or create a user if one is not in the database.
        user, created = ZooUser.objects.get_or_create(username = username)
        # stores the use_id in the session to track the logged in user.
        request.session['user_id'] = user.id

        # redirects to zoo_home after login, uses Django URL namespace avoid hardcoded paths
        return redirect('zoo_entrance:zoo_home')
    
    else:
        form = userLoginForm()

    return render(request, 'zoo_entrance/index.html', {'form': form})

def zoo_home(request):
    user_id = request.session.get('user_id')

    if not user_id:
        return redirect('zoo_entrance:index')
    
    user = ZooUser.objects.get(id= user_id)

    zoos = Zoo.objects.all() 
    #zoos = [1,2,3]
    return render(request, 'zoo_entrance/zoo_list.html', {'zoos': zoos})

    #return render(request, 'zoo_entrance/home.html', {'user': user})

"""
# we commented this block out because we want to consolidate the zoo list to home.html
def zoo_list(request):
    zoos = Zoo.objects.all() #== request.session['user_id'])
    #zoos = [1,2,3]
    return render(request, 'zoo_entrance/zoo_list.html', {'zoos': zoos})
"""
    
