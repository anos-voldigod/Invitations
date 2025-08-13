from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def invite():
    # This function will run when someone visits the main homepage
    return render_template('invite.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
