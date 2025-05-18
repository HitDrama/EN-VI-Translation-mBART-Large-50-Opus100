from flask import render_template, request, redirect, url_for,flash
from forms.translation_form import EnviForm
from models.translation_model import Translator

def dichenvi():
    model = Translator()
    form = EnviForm()
    result = None
    if form.validate_on_submit():
        vanban = form.english_text.data.strip()
        result=model.translate_text(vanban)

    return render_template('dichenvi.html', form=form, result=result)