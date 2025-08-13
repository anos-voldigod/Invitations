from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def invite():
    return render_template("invite.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
