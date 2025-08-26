# -*- coding: utf-8 -*-
from flask import Flask, render_template
from data import get_population_data, get_coordinates_data

app = Flask(__name__)

@app.route('/')
def index():
    population_data = get_population_data()
    coordinates_data = get_coordinates_data()
    
    return render_template('population.html', 
                         population_data=population_data,
                         coordinates_data=coordinates_data)

if __name__ == '__main__':
    app.run(debug=True)