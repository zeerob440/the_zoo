from .forms import userLoginForm, ZooForm, AnimalForm
from django.shortcuts import render, redirect, get_object_or_404
# data models below
from .models import ZooUser, Zoo, ZooAnimal


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

    # remove the following all() statement and use the filter below when we get login working
    # testing zoos = Zoo.objects.filter(zoo_user=user) to prevent any user for seeing all zoo that exist in the database
    zoos = Zoo.objects.filter(zoo_user=user)
    #zoos = Zoo.objects.filter(zoo_user = request.user)
    #zoos = [1,2,3]
    '''
    Django ORM dunder to follow a relationship in this case ZooUser > zoo field > check zoo_user
    so find animals where the animal's zoo's zoo_user is the current user. 
    '''
    animals = ZooAnimal.objects.filter(zoo__zoo_user=user)
    #animals = [1,2,3,4]
    # all values being passed must be in the SAME dictionary as different key value pairs
    # pass 'user' : user into zoo_home render, test to see if it returns the user's name in the <h2> element in home.html, it works. 
    return render(request, 'zoo_entrance/zoo_list.html', {'zoos': zoos,'animals':animals, 'user' : user})
    
    #return render(request, 'zoo_entrance/home.html', {'user': user})


def zoo_detail(request, pk):
    #render user name in zoo_detail.html
    user_id = request.session.get('user_id')
    user = ZooUser.objects.get(id=user_id)
    zoo = get_object_or_404(Zoo, pk=pk, zoo_user=user)
    animals = ZooAnimal.objects.filter(zoo=zoo)
    return render(request, 'zoo_entrance/zoo_detail.html', {'zoo': zoo, 'animals': animals, 'user': user})


def zoo_new(request):
     #if request.method == "POST":
        #form = ZooForm(request.POST)
        #if form.is_valid():
            #zoo = form.save(commit=False)
            # use the following line when we get login working and then remove the zoo.zoo_user=testuser line
            #zoo.zoo_user = request.user
            #zoo.zoo_user = ZooUser.objects.get(username='testuser')
            #zoo.save()
            #return redirect('zoo_entrance:zoo_detail', pk=zoo.pk)
    #else:
        #form = ZooForm()
    #return render(request, 'zoo_entrance/zoo_edit.html', {'form': form})
   # connect a new zoo to current user
    user_id = request.session.get('user_id')

    if not user_id:
       return redirect('zoo_entrance:index')
   
    user = ZooUser.objects.get(id=user_id)

    if request.method == 'POST':
       form = ZooForm(request.POST)
       if form.is_valid():
           zoo = form.save(commit=False)
           # set new zoo to logged in user
           zoo.zoo_user = user
           zoo.save()
           return redirect('zoo_entrance:zoo_detail', pk=zoo.pk) 
    else:
        form = ZooForm()
    return render(request, 'zoo_entrance/zoo_edit.html', {'form' : form})

def zoo_edit(request, pk):
    zoo = get_object_or_404(Zoo, pk=pk)
    if request.method == "POST":
        form = ZooForm(request.POST, instance=zoo)
        if form.is_valid():
            zoo = form.save(commit=False)
            zoo.save()
            return redirect('zoo_entrance:zoo_detail', pk=zoo.pk)
    else:
        # test render of user in zoo_detail
        user_id = request.session.get('user_id')
        user = ZooUser.objects.get(id=user_id)
        form = ZooForm(instance=zoo)
    return render(request, 'zoo_entrance/zoo_edit.html', {'form': form, 'user': user})


def animal_detail(request, pk):
    # add username to detail.html
    user_id = request.session.get('user_id')
    user = ZooUser.objects.get(id=user_id)
    animal = get_object_or_404(ZooAnimal, pk=pk)
    return render(request, 'zoo_entrance/animal_detail.html', {'animal': animal, 'user' : user})


def animal_new(request, pk):
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            animal = form.save(commit=False)
            animal.zoo = Zoo.objects.get(id=pk)
            animal.save()
            return redirect('zoo_entrance:animal_detail', pk=animal.pk)
    else:
        form = AnimalForm()
    return render(request, 'zoo_entrance/animal_edit.html', {'form': form})


def animal_edit(request, pk):
    animal = get_object_or_404(ZooAnimal, pk=pk)
    if request.method == "POST":
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            zoo = form.save(commit=False)
            zoo.save()
            return redirect('zoo_entrance:animal_detail', pk=animal.pk)
    else:
        form = AnimalForm(instance=animal)
        # render user in animal_edit()
        user_id = request.session.get('user_id')
    user = ZooUser.objects.get(id=user_id)
    return render(request, 'zoo_entrance/animal_edit.html', {'form': form, 'user' : user})