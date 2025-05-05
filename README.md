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

# Clone the repository
git clone https://github.com/Bashiho/TeamIGS.git

# Navigate to the project's directory
cd TeamIGS

# Now we are going to make a secret key. This is used for encryption purposes, and should be kept secret.
# There are two ways to do this

# Option 1
# This is the easiest method. Simply visit https://djecrety.ir/ and generate a key.

# Option 2
# This method takes longer than the first and has no significant benefits
# Install Django
pip install django
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


# If you are running this in VSCode, you can create a Virtual Environment (venv), from
# the command pallete
# Press ctrl + shift + p to open the pallete, then select Python: Create Environment
# Select the appropriate version of python and install packages from Requirements.txt

# If you cannot do the above, do the following through a terminal
# Create a Virtual Environment for the project
python -m venv path/to/venv

# Activate the Virtual Environment
# If you are on Linux or Mac
source path/to/venv/bin/activate
# If you are on Windows
~\path\to\venv\djangodev\scripts\activate.bat

# Install Requirements
pip install -r Requirements.txt
# you might be asked to update pip, if so, then run the command given to do so
```

## Setup
This project requires some setup beyond installation.
```shell
# Start by navigating to the dircetory of the project if you aren't already there
cd TeamIGS

# Then, we need to run some commands

# We'll start by running our server once
python manage.py runserver

# From there, we will get a warning about undeployed migrations
# Simply run the command provided to migrate
python manage.py migrate

# If for whatever reason this doesn't work, we can make the migrations
# again and deploy them 
python manage.py makemigrations
python manage.py migrate
# formatted as: sqlmigrate appName migrationName
python manage.py sqlmigrate TeamIGS 0001


# After migrating, create an admin account
python manage.py createsuperuser
# You will be prompted for a username, email, and password, fill out these fields as you are asked to

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

Setting up emails takes a little bit of work, but it's not too difficult. Steps 1-4 with pictures can be found here: https://www.geeksforgeeks.org/setup-sending-email-in-django-project/

### Step 1
Sign into your google account.
### Step 2 
Click on your account icon, then click "Manage your Google Account".
### Step 3
Click the search button in the top right corner and search for "2-Step Verification". Enable this.
### Step 4
Search for "App Passwords". Click the result with that name. Create a name for the project and hit create. You will be given a password.
### Step 5
In your .env file, write\
EMAIL = "YOUR@EMAIL"\
EMAILPASS = "PASSWORD"

"YOUR@EMAIL" is the email account you used, and "PASSWORD" is the password you got in step 4.


Setting up a webserver is up to you. There are several ways to do this, and that is a choice that you, the user, must make. For now, though, you can run things locally while testing. Just make sure to follow Django's advice for what to do before going into production. The checklist can be found below. \
https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/
