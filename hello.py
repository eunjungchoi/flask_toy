from flask import Flask
from flask import render_template
from flask import request
from textrankr import TextRank


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        textrank = TextRank(request.form['text'])
        return render_template('index.html', text=textrank.summarize())


if __name__ == "__main__":
    app.run()
