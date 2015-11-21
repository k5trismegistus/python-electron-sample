from __future__ import print_function
import os, sys, time
from flask import Flask
from flask import render_template
from jinja2 import FileSystemLoader

app_root_dir = os.path.join(os.path.dirname(__file__) + '../../')
views_dir = os.path.join(app_root_dir + 'views/')

app = Flask(__name__)
app.jinja_loader = FileSystemLoader(views_dir)

@app.route("/")
def hello():
    # dbg = {
    #     'os.path.dirname(__file__): ': os.path.abspath(os.path.dirname(__file__)),
    #     'views_dir': os.path.abspath(views_dir)
    # }
    # return str(dbg)
    return render_template('main.html')

if __name__ == "__main__":
    sys.stdout.flush()
    app.run(host='127.0.0.1', port=5000, debug=True)
