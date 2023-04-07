import os
import sys

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_path)

from models.system import Admins
from helpers.hash import generate_hash

user = Admins(username='0day', password=generate_hash('smith0000'))
user.save()
