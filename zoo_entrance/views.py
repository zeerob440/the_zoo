from django.shortcuts import render

# Create your views here.

'''index is the landing page for the zoo app. When a user navigates to the zoo_entrance, Django returns the index.html'''
def index(request):
    return render(request, 'zoo_entrance/index.html')
