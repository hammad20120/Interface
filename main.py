from flask import Flask, request, render_template
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.secret_key = 'a key'

catlist = ['Choose Category','grading', 'knowledge', 'presentation', 'counselling', 'punctuality', 'favoritism']
columnHeader = ['Review ID', 'Text', 'Category', 'Polarity']


def read_file(file):
    i = 0
    strs = []
    with open(file, 'r', encoding="utf8") as f:
        lines = f.readlines()

    f.close()
    for l in lines:
        if i != 0:
            strs.append(lines[i].split('\t', 3))
        i += 1

    return strs


@app.route("/", methods={'POST', 'GET'})
def index():
    if request.method == 'POST':
        file = request.files['file']
        file.save(secure_filename('comments'))
        evaluation = read_file('comments')
        return render_template("upload_file.html", catlist=catlist, columnHeader=columnHeader, evaluation=evaluation,
                               display=True)
    else:
        return render_template("upload_file.html")


app.run(debug=True, host='0.0.0.0')
