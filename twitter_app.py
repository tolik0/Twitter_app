from flask import Flask, render_template, request, redirect, url_for
from twitter import list_friends
from create_map import make_coordinates, map_create

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def main_page():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        return redirect("/{}".format(name))
    return render_template("index.html")


@app.route('/<name>')
def map(name):
    try:
        users = list_friends(name)
    except:
        continue
    users = make_coordinates(users)
    return map_create(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
