from flask import Flask, render_template
from models.system import Admins

from helpers.hash import generate_hash

def index():
    return render_template('login.html')
    
    
def login(request):
    
    
    