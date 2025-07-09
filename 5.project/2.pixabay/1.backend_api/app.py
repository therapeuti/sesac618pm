from flask import Flask, jsonify, url_for
import random
app = Flask(__name__)

dog_images = [
    "cat.jpg",
    "cat2.jpg"
]


@app.route('/')
def random_dog():
    random_img = random.choice(dog_images)
    # image_url = url_for('static', filename='img/{random_img}') # 상대경로가 만들어짐
    image_url = url_for('static', filename='img/{random_img}', _external=True) # 절대경로...?
    return jsonify({'url':image_url})

if __name__=='__main__':
    app.run(debug=True)