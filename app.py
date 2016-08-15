from flask import Flask
from flask import render_template
from flask import request
from textrankr import TextRank
from password import password
import os

app = Flask(__name__)
app.register_blueprint(password)


@app.route("/", methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html')
	else:
		if bool(os.environ.get('FLASK_DEBUG')):
			text = "로컬에서는 안됩니다. 셀프-죄송해요."
		else:
			text = TextRank(request.form['text']).summarize()

		return render_template('index.html', text=text)


if __name__ == "__main__":
	app.run()
