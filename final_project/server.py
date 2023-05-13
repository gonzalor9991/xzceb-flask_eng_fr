# rom machinetranslation import translator
from flask import Flask, request, render_template
from machinetranslation import Translator

app = Flask(__name__)


@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translatorObj = Translator()
    textToTranslate = translatorObj.english_to_french(textToTranslate)
    # Write your code here
    return textToTranslate


@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translatorObj = Translator()
    textToTranslate = translatorObj.french_to_english(textToTranslate)
    return textToTranslate


# Write the code to render template
@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
