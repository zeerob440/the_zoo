# the_zoo
Group 5, Jermey Baltazar, Gabriel Abney, Zach Roberts zoo application

General Django workflow.

django app deployment pipeline, V2 8 FEB 2026

1 create a folder for the project to live on.
 
2. create virtual environment, open the folder with PowerShell: 
	python -m venv nameOfVenv

3. Activate the virtual environment PowerShell: 
	venv\Scripts\activate
	
	a. to deactivate at the end of the work session PowerShell:
		deactivate
		
4. While venv is active; PowerShell: // django must be installed in a virtual environment for each django project.
	pip install django 
	
5. Structure files for django project PowerShell:
	django-admin startproject confing . // this orders files so they are not nested.

7. Activate database apps local to Django PowerShell:
	python manage.py migrate
	
8. Declare new app PowerShell:
	python manage.py startapp enterNameOfAppHere

	
9. Activate server PowerShell:
	python manage.py runserver
	
	a. to deactivate server PowerShell:
	CTR + C

10. to build code in a folder PowerShell: # will launch VS Code, write code save in VS Code.
	code nameOfProgram.py 
	
11. When new apps are created, they need to be added to the config/setting.py in INSTALLED_APPS: list installed apps in the venv to run.

Database Operations: (models.py)

The database is declared via Python classes in zoo/models.py. Once a class is created, it needs to be migrated to the database:
	In PowerShell from the folder with your virtual environment in it, input:
	python manage.py migrate

This will save the schema and import it into the database. Think of it as similar to a GitHub commit, except with Django for appending the database as we develop the application.
