from flask import Flask, render_template

app = Flask(__name__)

#ASTERATION
@app.route("/")
def asteration():
    return render_template("asteration/index.html")

#EVENTS - ASTERATION'S
@app.route("/Asteration/Events")
def asteration_events():
    return render_template("asteration/events.html")

@app.route("/Asteration/Events/Gelora")
def e_gelora():
    return render_template("asteration/e_gelora.html")

@app.route("/Asteration/Events/Aventura")
def e_aventura():
    return render_template("asteration/e_aventura.html")

@app.route("/Asteration/Events/Etourdissante")
def e_etourdissante():
    return render_template("asteration/e_etourdissante.html")
  
@app.route("/Asteration/Events/Qaliftar")
def e_qaliftar():
    return render_template("asteration/e_qaliftar.html")

@app.route("/Asteration/Events/Reveera")
def e_reveera():
    return render_template("asteration/e_reveera.html")

@app.route("/Asteration/Events/Lunerast")
def e_lunerast():
    return render_template("asteration/e_lunerast.html")

@app.route("/Asteration/Events/Litioree")
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

#OTHER
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

@app.route("/Credence/Events")
def credence_events():
    return render_template("credence/events.html")

#EVENTS - CREDENCE'S
@app.route("/Credence/Events/Altarma")
def e_altarma():
    return render_template("credence/e_altarma.html")

@app.route("/Credence/Events/Cakrawala")
def e_cakrawala():
    return render_template("credence/e_cakrawala.html")

@app.route("/Credence/Events/Compation")
def e_compation():
    return render_template("credence/e_compation.html")

@app.route("/Credence/Events/Moration")
def e_moration():
    return render_template("credence/e_moration.html")

@app.route("/Credence/Events/Noach")
def e_noach():
    return render_template("credence/e_noach.html")

@app.route("/Credence/Events/NoxSalvatoris")
def e_nox_salvatoris():
    return render_template("credence/e_nox_salvatoris.html")

@app.route("/Credence/Events/Remoderma")
def e_remoderma():
    return render_template("credence/e_remoderma.html")

@app.route("/Credence/Events/Renaissance")
def e_renaissance():
    return render_template("credence/e_renaissance.html")

@app.route("/Credence/Events/Revoir")
def e_revoir():
    return render_template("credence/e_revoir.html")

@app.route("/Credence/Events/TalentScouting")
def e_talent_scouting():
    return render_template("credence/e_talent_scouting.html")

#OTHER
@app.route("/Credence/Arletter")
def credence_arletter():
    return render_template("credence/arletter.html")

@app.route("/Credence/About")
def credence_about():
    return render_template("credence/about.html")

if __name__ == '__main__':
    app.run(debug=True)