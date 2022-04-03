from flask import Flask, render_template
from webforms import RecipeForm

# create Flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

# decorator to add URL route
@app.route("/")
# add content to page
def homepage():
  return render_template("home.html")

# add page for adding a recipe
@app.route("/addrecipe", methods=['GET', 'POST'])
def add_recipe():
  recipe_title = None
  ingredients = []
  recipe_instr = []
  form = RecipeForm()
  # validate form
  if form.validate_on_submit():
    recipe_title = form.recipe_title.data
    form.recipe_title.data = ""
  return render_template("addrecipe.html", recipe_title = recipe_title, form = form)

# create custom error pages
# invalid url
@app.errorhandler(404)
def page_not_found(e):
  return render_template("404.html"), 404

# internal server error
@app.errorhandler(500)
def page_not_found(e):
  return render_template("500.html"), 500

