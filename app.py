from re import I
from flask import Flask, render_template, request, redirect, url_for,flash

app = Flask(__name__)
#app.config['SECRET_KEY']='ICCS'
app.secret_key = "ICCS"

@app.route("/", methods = ["GET", "POST"])
def helloworld():
    flash("What's your name?")
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        formData = request.form
        guest_name = formData['guest_name']
        flash("Hello " + guest_name)
        return redirect(url_for("helloworld"))

if __name__ == '__main__':
    app.run(debug=True)