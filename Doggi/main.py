from flask import Flask, render_template
from dog_api import dog
import json


app = Flask(__name__)
app.secret_key = b'W#J%3(%&JE%&/HW'


@app.route("/", methods=["GET", "POST"])
def home():
    dogs = dog.master_breeds()
    img = dog.random_image()
    JSONdogs = json.dumps(dogs)
    JSONdict = json.dumps(dog.all_breeds())
    return render_template("home.html", dogs=dogs, img=img, JSONdogs2=JSONdogs, JSONdict2=JSONdict)





if __name__ == "__main__": app.run()
