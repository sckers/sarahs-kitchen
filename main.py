from flask import Flask

# create Flask instance
app = Flask(__name__)

# decorator to add URL route
@app.route("/")
# add content to page
def homepage():
  return "<h1>There's nothing here.</h1>"

# add page for adding a recipe
@app.route("/addrecipe")
def add_recipe():
  return "<h1>On this page you can add new recipes to your cookbook.</h1>"
