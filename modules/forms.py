from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class CVForm(FlaskForm):
    personal_info = TextAreaField(
        'Informations Personnelles', validators=[DataRequired()])
    professional_experience = TextAreaField(
        'Expérience Professionnelle', validators=[DataRequired()])
    education = TextAreaField('Formation', validators=[DataRequired()])
    skills = TextAreaField('Compétences', validators=[DataRequired()])
    languages = TextAreaField('Langues', validators=[DataRequired()])
    hobbies = TextAreaField('Loisirs')
    submit = SubmitField('Créer CV')
