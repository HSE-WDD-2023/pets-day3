from flask import Flask, render_template, request
import pets as fsp

app = Flask(__name__)

TYPES = ["dog", "cat", "reptile", "rabbit", "mouse"]
SERVICES = ["grooming", "boarding", "training", "agility", "check-ups"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("registration.html", pet_types=TYPES,
                                                services=SERVICES)

@app.route("/success", methods=["POST"])
def success():
    # first grab the data that user entered
    owner = request.form.get("owner")
    if not owner:
        msg = "No Owner Name Entered"
        return render_template("error.html", msg=msg)
    pet = request.form.get("pet")
    if not pet:
        msg = "Please tell us you pet's name"
        return render_template("error.html", msg=msg)
    pet_type = request.form.get("pet-type")
    if pet_type not in TYPES:
        msg = f"Sorry we do not work with {pet_type}s at this time."
        return render_template("error.html", msg=msg)
    services = request.form.getlist("service")

    # create a dict to hold the pet info
    pet_dict = {
        "owner": owner,
        "pet": pet,
        "type": pet_type,
        "services": services
    }
    # now add this dict to the json file
    fsp.add_pet(pet_dict)


    # show the success message page passing in the
    # owner and pet names
    return render_template("success.html",
                           owner_name=owner,
                           pet_name=pet,
                           pet_type=pet_type)


@app.route("/show")
def show():
    all_pets = fsp.load_pets()
    return render_template("show.html", all_pets=all_pets)


@app.route("/grooming")
def grooming()
    # create a route that will show all the pets who are only
    # interested in grooming services
    # create a function in pets.py that will only grab out the
    #   registered pets with grooming in services
    #   this function should return a list of dicts
    # use the results of the function to render a template that will
    #   show the data in a table or a list or some other format
    return "Grooming"
