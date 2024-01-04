from flask import Flask, render_template

app = Flask(__name__)

#ASTERATION
@app.route("/")
def asteration():
    return render_template("asteration/index.html")

#EVENTS
@app.route("/Asteration/Events")
def asteration_events():
    return render_template("asteration/events.html")

@app.route("/Asteration/Events/Litiorée")
def e_litioree():
    return render_template("asteration/e_litioree.html")

@app.route("/Asteration/Events/Armone")
def e_armone():
    return render_template("asteration/e_armone.html")

@app.route("/Asteration/Events/Pelita")
def e_pelita():
    return render_template("asteration/e_pelita.html")

@app.route("/Asteration/Events/Aksara")
def e_aksara():
    return render_template("asteration/e_aksara.html")

#OTHERS
@app.route("/Asteration/Updates")
def asteration_updates():
    return render_template("asteration/updates.html")

@app.route("/Asteration/Clubs")
def asteration_clubs():
    return render_template("asteration/clubs.html")

@app.route("/Asteration/About")
def asteration_about():
    return render_template("asteration/about.html")

#CREDENCE
@app.route("/Credence")
def credence():
    return render_template("credence/index.html")

@app.route("/Credence/About")
def credence_about():
    return render_template("credence/about.html")

if __name__ == '__main__':
    app.run(debug=True)