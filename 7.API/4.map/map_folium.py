# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # 63 Building coordinates (latitude, longitude)
    location = {
        'lat': 37.5197,
        'lon': 126.9394,
        'name': '63 Building',
        'zoom': 15
    }
    return render_template('map.html', location=location)

if __name__ == '__main__':
    app.run(debug=True)