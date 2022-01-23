from flask import Flask, render_template, request, redirect, url_for, send_from_directory, send_file
from werkzeug.utils import secure_filename
import os
from overlay import do_the_trick

app = Flask(__name__, static_url_path='/assets')
app.config['UPLOAD_FOLDER'] = './images'
app.config['ASSETS'] = './assets'
app.config['JS'] = './'
app.config['MAX_CONTENT_LENGTH'] = 2 * 1000 * 1000

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

@app.route('/html2canvas/<name>')
def js(name):
    return send_from_directory(app.config["JS"], name)

@app.route('/assets/<name>')
def image_file(name):
    return send_from_directory(app.config["ASSETS"], name)

@app.route('/edit/',methods=['GET', 'POST'])
def config():
	return render_template("configs.html")


@app.route("/", methods=["GET", "POST"])
def base():
	if request.method == 'POST':
		if 'file' not in request.files:
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
		file_location = os.path.join(app.config['UPLOAD_FOLDER'], filename)
		file.save(file_location)
		# magic mike 
		do_the_trick(file_location)
		# delete images
		os.remove(file_location)
		# call above route /uploads/name and redict user to access image
		#return redirect(url_for('download_file', name=filename))
		return redirect("/edit")
	return render_template("base.html")

app.run()
