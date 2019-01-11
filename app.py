from flask import Flask, render_template, request
from models.character import Character
import mlab

mlab.connect()
app = Flask(__name__)

@app.route('/character')
def character():
    return render_template("character.html")

@app.route('/add_character', methods=["GET", "POST"])
def add_character():
    #1. Gui form (GET)
    if request.method == "GET":
        return render_template("character_form.html")
    elif request.method == "POST":
    #4. Nhan form => Luu
        form = request.form
        print(form)
        name = form["name"]
        image = form["image"]
        rate = form["rate"]
        new_character = Character(name=name, image=image, rate=rate)
        new_character.save()
        return "GOTCHA"

@app.route('/characters')
def characters():
    character_list = Character.objects() #Get all data
    
    #Render: template + data
    return render_template("characters.html", character_list=character_list)

@app.route('/character/<given_id>')
def character_detail(given_id):
    #1. Get one character, based on id
    character = Character.objects().with_id(given_id)
    if character is None:
        return "Not found"
    else: #2. Render
        return render_template("character_detail.html", character=character)

@app.route('/character/delete/<given_id>')
def character_delete(given_id):
    character_del = Character.objects(id__exact=given_id)
    character_del.delete()
    return 'The id ' + given_id + ' was deleted'

if __name__ == '__main__':
  app.run(debug=True)