from flask import Flask, request
from werkzeug.utils import secure_filename
import general_generator
import specific_generator
import specific_satisfier
import default_display
import KafkaComponents
import webbrowser
import os
import pandas as pd 

app = Flask(__name__)
MAX_DEFAULT_MATRIX_LENGTH = 7
default_matrices = default_display.generate_default_matrices_general_generator(MAX_DEFAULT_MATRIX_LENGTH, MAX_DEFAULT_MATRIX_LENGTH)

def check(value):
    try:
        val = int(value)
    except ValueError:
        return False
    if float(value) < 0:
        return False
    if val != float(value):
        return False
    return True

def file_to_string(fname):
    output = ""
    f = open(fname, "r")
    lines = f.readlines()
    f.close()
    for line in lines:
        output += line + ";"
    return output[:-1]

def write_to_file(text):
    f = open("generator.html", "w")
    f.write(text)
    f.close()
    webbrowser.open(os.path.abspath("generator.html"), new=2)
    return app.send_static_file('upload.html')


@app.route("/dimensional_analysis", methods=["GET"])
def get_dimensional_analysis():
    return app.send_static_file('upload.html')


@app.route("/dimensional_analysis", methods=["POST"])
def post_dimensional_analysis():
    form = request.form.to_dict()
    form_list_keys = list(form.keys())
    if ("General" in form_list_keys):
        if (check(form["odim"]) and check(form["sdim"]) and int(form["odim"]) < int(form["sdim"])):
            return general_generator.Model().generate_dimensional_analysis_html_script(int(form["odim"]), int(form["sdim"]), default_matrices, MAX_DEFAULT_MATRIX_LENGTH)
        return "Invalid Parameters"
    if (len(request.files.getlist("file")) > 0):
        file = request.files.getlist("file")[0]
        fname = secure_filename(file.filename)
        file.save(fname)
        if ("Specific" in form_list_keys):
            return specific_generator.Model().generate_dimensional_analysis_html_script(pd.read_csv(fname, sep=",", header=None))
        return specific_satisfier.Model().generate_dimensional_analysis_html_script(pd.read_csv(fname, sep=",", header=None))
    return "Invalid Parameters"

if __name__ == '__main__':
    app.run()