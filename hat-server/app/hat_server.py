from flask import Flask, request, render_template
import json

ANNIMATION_PATH="/opt/hat_server/annimations/"

app = Flask(__name__)
 
@app.route('/')
def index():
    """Show a list of animations available"""
    return "Hat server"

@app.route('/edit-animation')
def edit_animation():
    """Show the editor for an animation"""
    return render_template('edit_animation.html')
 
@app.route('/save-animation', methods = ['POST'])
def save_animation():
    """Take an animation and save it."""
    #import ipdb; ipdb.set_trace()
    data = request.get_json()
    annimation_name = data["name"]
    print("NAME: {}".format(annimation_name))

    filename = "{}{}.json".format(ANNIMATION_PATH, annimation_name)
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)
    # do something with this data variable that contains the data from the node server
    return json.dumps({"newdata":"hereisthenewdatayouwanttosend"})
 
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)