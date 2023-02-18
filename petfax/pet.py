from flask import (Blueprint, render_template)
import json

#opening and reading file
pets = json.load(open('pets.json'))
#print(pets)

bp = Blueprint('pet', __name__, url_prefix='/pets')

@bp.route('/')
def index():
    return render_template('pets/index.html', pets = pets)

@bp.route('/<int:pet_id>')
def one_pet(pet_id):
    #finding the index number in the list
    pet = pets[pet_id-1]
    #only using one pet, not iterating over a list of pets
    return render_template('pets/pet_page.html', pet=pet)