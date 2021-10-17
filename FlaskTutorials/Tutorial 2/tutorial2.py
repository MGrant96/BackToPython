from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# Define pages on website
@app.route("/<name>") # Define how to acces this specific page with the decorator @app.route
def home(name):
    return render_template("index.html", content = ["Mick", "Ciaran", "Glenn"], r = 9000, name = name)

if __name__ == "__main__":
    app.run()

# py ".\tutorial2.py" 
# or nodemon ".\tutorial2.py" 