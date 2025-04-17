import django
import pydoc
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'TeamIGS.settings'
django.setup()
pydoc.cli()