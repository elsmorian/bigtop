from glob import glob
import json
import os

from flask import Flask, request, render_template


ANIMATION_PATH = "/opt/hat_server/animations/"

app = Flask(__name__)
 
@app.route('/')
def index():
    """Show a list of animations available"""

    return render_template(
        'list_animations.html',
        animations=get_animations(),
    )

@app.route('/make-animation-active', methods = ['POST'])
def make_animation_active():
    """Make an animation active."""
    data = request.get_json()
    status = {
        "name": data["name"],
        "type": "run_single",
    }
    with open("current.status", 'w') as outfile:
        json.dump(status, outfile)
    return json.dumps({"status":"ok"})

@app.route('/edit-animation')
def edit_animation():
    """Show the editor for an animation"""
    animation_data = {}
    if request.args.get('name'):
        animation_name = "{}{}.json".format(
            ANIMATION_PATH,
            request.args.get('name'),
        )
        with open(animation_name, 'r') as animation_file:
            animation_data = json.loads(animation_file.read())
    return render_template(
        'edit_animation.html',
        animation_data=animation_data,
    )
 
@app.route('/save-animation', methods = ['POST'])
def save_animation():
    """Take an animation and save it."""
    #import ipdb; ipdb.set_trace()
    data = request.get_json()
    animation_name = data["name"]
    print("NAME: {}".format(animation_name))

    filename = "{}{}.json".format(ANIMATION_PATH, animation_name)
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)
    return json.dumps({"status":"ok"})
 
def get_animations():
    """Get all valid animations."""
    files = glob("{}*.json".format(ANIMATION_PATH))
    animations = []
    for file in files:
        file_without_path = file.split("/")[-1]
        file_without_extension = file_without_path.split(".")[0]
        animations.append(file_without_extension)
    return animations


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)
