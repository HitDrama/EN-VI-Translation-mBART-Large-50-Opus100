from flask_wtf import FlaskForm
from wtforms import IntegerField,TextAreaField,SubmitField,SelectField
from wtforms.validators import DataRequired

class EnviForm(FlaskForm):
    english_text=TextAreaField("Nhập văn bản",validators=[DataRequired()])
    submit=SubmitField("En to Vi")