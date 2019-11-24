import flask

app = flask.Flask(__name__)

print("running")

@app.route("/")
def index():
    print("The main page is about to be rendered")
    return flask.render_template("index.html", title="home")

@app.route("/downloads/shrek.zip")
def get_shrek():
    return flask.send_file("shrek.zip", attachment_filename="shrek.zip")

@app.route("/downloads/nicholascage.zip")
def get_nicholascage():
    return flask.send_file("nicholascage.zip", attachment_filename="nicholascage.zip")

@app.route("/downloads/ronaldmcdonald.zip")
def get_ronaldmcdonald():
    return flask.send_file("ronaldmcdonald.zip", attachment_filename="ronaldmcdonald.zip")

@app.route("/downloads/trump.zip")
def get_trump():
    return flask.send_file("trump.zip", attachment_filename="trump.zip")

@app.route("/downloads/emoji.zip")
def get_emoji():
    return flask.send_file("emoji.zip", attachment_filename="emoji.zip")


@app.route("/downloads/all.zip")
def get_all():
    return flask.send_file("all.zip", attachment_filename="all.zip")
