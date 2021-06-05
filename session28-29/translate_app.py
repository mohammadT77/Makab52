import translators
from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/<target_lang>', methods=['GET', 'POST'], defaults={'from_lang': 'auto', 'provider': 'google'})
@app.route('/<target_lang>/<from_lang>', methods=['GET', 'POST'], defaults={'provider': 'google'})
@app.route('/<target_lang>/<from_lang>/<provider>', methods=['GET', 'POST'])
def translate_func(target_lang, from_lang, provider):
    text = request.values['text']
    translator = getattr(translators, provider)
    output = translator(text, from_lang, target_lang)
    return render_template('translate.html', translated_text=output)


app.run(host='0.0.0.0')
