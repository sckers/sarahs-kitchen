from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, FormField, FieldList, Form
from wtforms.validators import DataRequired

class IngredientForm(Form):
    amt = StringField("Amount")
    unit = SelectField("Units", choices=['', 'tsp', 'tbsp', 'c'])
    name = StringField("Ingredient")


# create a form class
class RecipeForm(FlaskForm):
  recipe_title = StringField("Recipe Title", validators=[DataRequired()])
  ingredients = FieldList(FormField(IngredientForm), min_entries = 1)
  recipe_instr = FieldList(TextAreaField("Recipe Instructions"), min_entries = 1)
  create_recipe = SubmitField("Create")