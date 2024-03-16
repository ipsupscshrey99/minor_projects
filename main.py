#pip3 install flask opencv-python
from flask import Flask, render_template,request , flash #This function is used to render HTML templates with dynamic data
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'png', 'webg', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):  # check ki ye file extension ke liye valid hai ky?
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def processImage():
    pass


@app.route("/") # ye sab end points hai yaha click kiya toh woh page pr locate hote hai
def home(): # home naam ke 2 functions nhi rehe sakte  hai
    return render_template("index.html")

@app.route("/About")
def About():
    return render_template("About.html")
 # dusre port pr run hoga woh website

#@app.route("/Help for use")
#def Help_for_use():
#    return render_template("Help for use.html")


#@app.route("/Contact Us")
#def Contact_Us():
#    return render_template("Contact Us.html")

#@app.route("/Disabled")
#def Disabled():
#    return render_template("Disabled.html")

@app.route("/edit" , methods = ["GET" , "POST"]) # here this are 2 list of methods
def edit():
    if request.method == "POST":

        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return "error"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return "error not selected"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template("index.html")
        return "POST request is here"
    return render_template("index.html")


app.run(debug=True,port = 5001)
