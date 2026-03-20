from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        a = int(request.form["a"])
        b = int(request.form["b"])
        return str(a + b)

    return render_template("index.html")

app.run(debug=True)