from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

data_list = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        id_val = request.form.get("id", "").strip()
        nama = request.form.get("nama", "").strip()
        usia = request.form.get("usia", "").strip()
        menu = request.form.get("menu", "").strip()
        
        if id_val and nama and usia and menu:
            data_list.append({
                "id": id_val,
                "nama": nama,
                "usia": usia,
                "menu": menu
            })
            return redirect(url_for("hasil"))
            
    return render_template("form.html")

@app.route("/hasil")
def hasil():
    query = request.args.get("q", "").strip().lower()
    if query:
        filtered = [d for d in data_list if query in d["id"].lower() or query in d["nama"].lower()]
    else:
        filtered = data_list
    return render_template("hasil.html", data=filtered, q=query)

if __name__ == "__main__":
    app.run(debug=True)
