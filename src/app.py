from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os
from utils.allowed_files import allowed_file
from routes.clear_videos import clear_videos
from routes.list_videos import list_videos

app = Flask(__name__, static_folder="static")
app.secret_key = "secret key"
app.config["UPLOAD_FOLDER"] = "static/uploads/"

app.add_url_rule('/videos/clear', view_func=clear_videos)
app.add_url_rule('/videos/list', view_func=list_videos)

@app.route("/")
def upload_file_page():
  return render_template("index.html")
	
@app.route("/", methods = ["POST"])
def upload_file():
  if "file" not in request.files:
    flash("No file part")
    return redirect(request.url)
  file = request.files["file"]
  if file.filename == "":
    flash("No image selected for uploading")
    return redirect(request.url)
  if file and allowed_file(file.filename):
    if not os.path.exists("static"):
      os.mkdir("static")
    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
      os.mkdir(app.config["UPLOAD_FOLDER"])
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
    flash("Original label: ")
    flash("Predicted label: ")
    return render_template("index.html", filename="uploads/" + filename)
  else:
    flash("Allowed image types are -> mp4")
    return redirect(request.url)

@app.route("/display/<filename>")
def display_image(filename):
  return redirect(url_for("static", filename="uploads/" + filename), code=301)
		
if __name__ == "__main__":
  app.run(debug = True)