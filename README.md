# THE ZOO README
SDEV 220 Group 5 Zoo Management Application
Jeremy Baltazar, Gabriel Abney, Zach Roberts


## Setup
This application runs a local server using Django that is accessible in the user's browser.
The user will need to have Python 3.14 or greater, and will use the VENV module to install Django 6.0.2 using the requirements.txt file.
Follow the following steps to set up the server properly:
1. Open up the folder containing the local copy of this repo in terminal/VSCode.
2. Create the virtual environment using the command 'python -m venv v'
3. Activate the virtual environment using the command 'v\Scripts\activate.ps1' 
3. Install required modules (Django 6.0.2 in this case) using the command 'pip install -r requirements.txt'
4. Now run the server using the command 'python manage.py runserver'
5. Access the server in your browser at the URL 'http://127.0.0.1:8000'

## Navigating the site
### Login
The landing page for the site displays a form for the user to login or create an account using a single field. Typing a new username will create a new account and typing an existing username will open a previously created account to access those zoos.
### Zoo Homepage
You will be redirected the zoo management homepage.  This will display all the user's created zoos as well as the animals in those zoos.  Upon account creation, this list will be empty. Click the 'Add a new zoo?' link to create a new zoo, or if you have already created zoos, click the zoo's name to view its page.
### Adding a Zoo
Enter the name of a zoo as well as its location, and check the box if you'd like it to be open to the public. Click save and you will be redircted to the zoo's detail page.
### Zoo Detail Page
This page displays a list of the attributes of the selected zoo, as well as any animals residing in it. The animal list will be empty when the zoo is first created. Click the 'Edit this zoo?' button to change attributes of this zoo. Click the 'Add a new animal?' button to go to the animal creation page. If animals exist, click an animal's name to go to its detail page.
### Edit Zoo Details Page
This is identical to the 'New Zoo' page, but should populate with the selected zoo's details. Hit save after making any changes and be redirected to the zoo details page.
### Add New Animals Page
This page allows you to enter details for a newly created animal. Click save when done to be redirected to the animal details page.
### Animal Details Page
This page shows the details of the selected animal including all the attributes it was given. Click 'Edit this animal?' to edit the attributes in the Edit Page.

All your changes in any of these pages should save immediately to your local copy of the database located in the repo folder and will be accessible when the server is run in the future. Just use the same login credentials to access your created zoos.

Have fun creating zoos and filling them with animals!


## Note for the professor:
Our team used Discord as our communication platform where we managed our meetings and recorded our progress live and over text.
All of our updates and commits are preserved in GitHub repo branches that are mostly named according to the week of the work in which they were made.
Our project uses Classes to manage the ZooUser, Zoo, and ZooAnimal models in our SQLite3 database and our models.py file as well as when forms are submitted to the backend. Our project uses dictionaries to pass information to generate views in each of the views.py functions. Our project stores URLs in a list in our urls.py for generating static and dynamic URLs for the app.
Thanks for a great semester!