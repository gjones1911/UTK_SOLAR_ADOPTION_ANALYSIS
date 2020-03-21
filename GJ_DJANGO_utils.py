import sys
import os

def init_django_site(project_name='New_Django_Project', dir=None, verbose=False):
    """Will create a new django project of the given name"""
    os.system('django-admin startproject {}'.format(project_name))

init_django_site('Delete_me_please')