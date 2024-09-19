from flask import Blueprint

cars_routes = Blueprint("cars", __name__, url_prefix='/cars', static_folder='static', template_folder='templates')
from app.cars.cars import *