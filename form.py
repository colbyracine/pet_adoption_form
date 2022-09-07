from tokenize import String
from wtforms import StringField, IntegerField, BooleanField, SelectField, TextAreaField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, URL, NumberRange, Optional, Length


class AddPetForm(FlaskForm):
    # form to add a new adoptable pet
    name = StringField("Pet Name", validators=[InputRequired()])
    # species = StringField("Species/Breed", validators=[InputRequired()])
    photo_url = StringField("Image address of pet", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30)])
    notes = StringField("Notes about the adoptee")
    available = BooleanField("Available")
    
    # setting up choices for species
    species = SelectField("Species", choices=[('Cat'), ('Dog'), ('Porcupine')])
    
    
class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )

    available = BooleanField("Available?")