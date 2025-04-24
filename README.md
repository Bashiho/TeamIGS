# TeamIGS

## Table of Contents
- [About](#-about)
- [The Team](#-the-team)
- [Installation](#-installation)
- [Setup](#-setup)
- [Credits](#-credits)

## About
Project from Team IGS for Comp 380 Section 20432\
Somewhat basic implementation of an E-commerce website\
**[Jira Project Board](https://teamigs.atlassian.net/jira/software/projects/SCRUM/boards/1/backlog)**

**Project Prompt**\
"A software that performs simple E-commerce site for a “abc” sales Company. The functions include searching for
an item, order, including shipping methods; pay an item using credit card etc. Confirmation of the purchase
should be sent to the user’s email address."

## The Team
- Russell de Vries (@Bashiho)
- Finn Bishop (@Arrowsurf)
- Steven Navarrete (@Steven2700)
- Andy Martinez (@AndyJM24)

## Installation
```shell
# Open Command Prompt or Powershell on Windows and Terminal on Mac or Linux

# Check if Git is installed
git --version
# Download it here if it is not installed 
# https://git-scm.com/downloads

# Check if python is installed 
python --version
# Download the latest version if it is not installed
# https://www.python.org/downloads/

# Now we are going to make a secret key. This is used for encryption purposes, and should be kept secret.
# There are two ways to do this

# Option 1
# This is the easiest method. Simply visit https://djecrety.ir/ and generate a key.

# Option 2
# This method takes longer than the first and has no significant benefits over the other.
# Create a Django project
# Create a file directory where you want the project to be stored
mkdir DjangoProject
# Navigate into that directory
cd DjangoProject
# Create a django project
$ django-admin startproject projectname djangoproject

# After you have your key, create a file called '.env'. 
# In this .env file, write the following, and paste your key where it says 'YOUR KEY' 
# DJANGOSECRET = 'YOUR KEY'

# Clone the repository
git clone https://github.com/Bashiho/TeamIGS.git

# Navigate to the project's directory
cd TeamIGS

# Create a Virtual Environment for the project
python -m venv ~/.virtualenvs/venv

# Activate the Virtual Environment
# If you are on Linux or Mac
source ~/.virtualenvs/venv/bin/activate
# If you are on Windows
~\.virtualenvs\djangodev\scripts\activate.bat

# Install Requirements
pip install -r requirements.txt
# You might get an error, and it might ask you to update pip. To do so, run the command that it prompts you to run. It will look something like this for Windows users.
python.exe -m pip install --upgrade pip

# Finally, move your .env file into the directory alongside manage.py
```

## Setup
This project requires some setup beyond installation.
```shell
# Start by navigating to the dircetory of the project
cd TeamIGS

# Then, we need to run some commands

# Start by making and deploying migrations. This will initialize our database with the parameters given by
# the models defined in the program
# Making migrations
python manage.py makemigrations

# Deploying the migrations
python manage.py migrate
python manage.py sqlmigrate TeamIGS 0001

#Then, create an admin account
python manage.py createsuperuser
# You will be prompted for a username, email, and password, simply fill out these bits of information.

# Then, to run the server locally and test that everything is working,
python manage.py runserver

```

From here, there will be a url provided in the console. It will look something like this:\
http://127.0.0.1:8000 \
Navigating to this page will lead you to an empty home page. To add items, navigate to\
http://127.0.0.1:8000/admin \
From here, sign into the admin account you created earlier.\
Then, we can create items. This is done by clicking the "+Add" button next to "Items".\
![Add Items](https://github.com/Bashiho/TeamIGS/blob/main/Resources/readme-arrow-items.png?raw=true)\
From here, fill out the fields with the information that you desire. The only section of note is images, which you can upload directly from your computer. They will be stored locally alongside the project files in /static/images/itemImages.\
These items should automatically appear on the home page of the website as they are added.

Setting up a webserver is up to you. There are several ways to do this, and that is a choice that you, the user, must make. For now, though, you can run things locally while testing. Just make sure to follow Django's advice for what to do before going into production. The checklist can be found below. \
https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/
