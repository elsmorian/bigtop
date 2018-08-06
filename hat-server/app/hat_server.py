from flask import Flask, request, render_template
import json
 
app = Flask(__name__)
 
@app.route('/')
def index():
	return "Flask server"

@app.route('/edit-animation')
def edit_animation():
	return render_template('edit_animation.html')
 
@app.route('/postdata', methods = ['POST'])
def postdata():
    data = request.get_json()
    print(data)
    # do something with this data variable that contains the data from the node server
    return json.dumps({"newdata":"hereisthenewdatayouwanttosend"})
 
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)