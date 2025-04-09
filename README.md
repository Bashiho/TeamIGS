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

# Create a Virtual Environment for the project
python3 -m venv ~/.virtualenvs/djangodev

# Activate the Virtual Environment
source ~/.virtualenvs/djangodev/bin/activate
# Alternatively, if source command is not available
. ~/.virtualenvs/djangodev/bin/activate

# Install Requirements
pip install -r requirements.txt
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
http://127.0.0.1:8000\
Navigating to this page will lead you to an empty home page. To add items, navigate to\
http://127.0.0.1:8000/admin\
From here, sign into the admin account you created earlier.\
Then, create a category for objects to be placed into. This is done by clicking the button that reads "+Add" next to "Categories".
<!-- ![Add Categories](http://link to image) -->
From here, simply fill out the fields with the desired information.\
Then, we can create items. This is done by clicking the "+Add" button next to "Items".
<!-- ![Add Items](http://link to image) -->
From here, fill out the fields with the information that you desire. The only section of note is images, which you can upload directly from your computer. They will be stored locally alongside the project files in /static/images.\
These items should automatically appear on the home page of the website as they are added.\

