from flask import Flask, request, render_template, json, redirect

app = Flask(__name__)
jsnfile = 'data.json'



@app.route('/', methods=['GET', "POST"])
def index():
    with open(jsnfile, 'r') as ps:
        peliculas = json.load(ps)
    return render_template("index.html",  peliculas=peliculas)

@app.route("/addfilm", methods = ['GET', 'POST'])
def addFilm():
    if request.method == 'GET':
        return render_template('addfilm.html', pelicula={})
    if request.method == 'POST':
        id = request.form["id"]
        name = request.form["name"]
        year = request.form["year"]
        with open(jsnfile, 'r+') as ps:
            peliculas = json.load(ps)
        peliculas.append({"id": id, "name": name, "year": year})
        with open(jsnfile, 'w') as ps:
            json.dump(peliculas, ps)
        return redirect('/')
    

@app.route('/updatefilm/<string:id>',methods = ['GET','POST'])
def updatefilm(id):
    with open(jsnfile) as ps:
        peliculas = json.load(ps)
    if request.method == 'GET':
        pelicula = [x for x in peliculas if x['id'] == id][0]
        return render_template("addfilm.html", pelicula=pelicula)
    if request.method == 'POST':
        for pelicula in peliculas:
            if(pelicula['id'] == id):
                pelicula['name'] = request.form["name"]
                pelicula['year'] = request.form["year"]
                break
        with open(jsnfile, 'w') as ps:
            json.dump(peliculas, ps)
        return redirect('/')


@app.route('/deletefilm/<string:id>')
def deletefilm(id):
    with open(jsnfile) as ps:
        peliculas = json.load(ps)
    newfilmlist = []
    for pelicula in peliculas:
        if(pelicula['id'] != id):
            newfilmlist.append(pelicula)
    with open(jsnfile, 'w') as pw:
        json.dump(newfilmlist, pw)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=5001)