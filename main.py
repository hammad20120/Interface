from flask import Flask, request, render_template, flash, redirect, url_for, Response, send_file
from werkzeug.utils import secure_filename
from datetime import datetime
import pandas

app = Flask(__name__)
app.secret_key = 'a key'


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


@app.route('/submit', methods=['POST'])
def submit():
    category = []
    polarity = []
    review_id = []
    comments = []

    iteration = 1
    for i in request.form.getlist('check'):
        category.append(request.form.get('category' + str(iteration)))
        polarity.append(request.form.get('polarity' + str(iteration)))
        i = i.replace("'", '')
        i = i.strip("()")
        i = i.replace("\\n", '')
        temp = i.split(", ")
        review_id.append(temp[0])
        comments.append(temp[1])
        iteration += 1

    raw_data = {'category': category, 'polarity': polarity, 'review_id': review_id, 'comments': comments}
    df = pandas.DataFrame(raw_data, columns=['category', 'polarity', 'review_id', 'comments'])
    df.to_csv("retrainComments.csv", index=False, sep='\t')
    return send_file('retrainComments.csv',
                     mimetype='text/csv',
                     attachment_filename='retrainComments-'+str(datetime.now())+'.csv',
                     as_attachment=True)


@app.route("/", methods={'POST', 'GET'})
def index():
    if request.method == 'POST':
        file = request.files['file']
        file.save(secure_filename('comments'))
        evaluation = read_file('comments')
        for i in evaluation:
            print(i)
        return render_template("upload_file.html", evaluation=evaluation, display=True)
    else:
        return render_template("upload_file.html")


app.run(debug=True, host= '0.0.0.0')
