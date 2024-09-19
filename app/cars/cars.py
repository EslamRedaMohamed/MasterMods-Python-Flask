from app.cars import cars_routes
from app.models import Car
from flask import render_template

@cars_routes.route('/')
def show_all_cars():
    cars = Car.show_all_cars()
    return render_template('cars.html', cars=cars)



