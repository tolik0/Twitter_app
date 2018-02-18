from flask import Flask, render_template, request, redirect, url_for
from twitter import list_friends
from create_map import make_coordinates, map_create

app = Flask(__name__)


# main page
@app.route('/', methods=['POST', 'GET'])
def main_page():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        return redirect("/{}".format(name))
    return render_template("index.html")


# page of map
@app.route('/<name>')
def map(name):
    users = list_friends(name)
    users = make_coordinates(users)
    return map_create(users)


if __name__ == '__main__':
    app.run()
