import django
import pydoc
import os

def runPydoc():
    '''Script to create pydoc documentation. Required due to Django requiring extra setup to work with pydoc.

    Code Date: April 16
    Programmer: Russell de Vries
    '''
    os.environ['DJANGO_SETTINGS_MODULE'] = 'TeamIGS.settings'
    django.setup()
    pydoc.cli()