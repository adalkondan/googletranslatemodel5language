!pip install googletrans==4.0.0rc1
from googletrans import Translator

# Create a translator object
translator = Translator(service_urls=['translate.google.com'])

# Get input text from the user
text = input("Enter the text to translate: ")

# Define the target languages
languages = {
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
    'Hindi': 'hi',
    'Tamil': 'ta'
}

# Translate the input text to each target language
for language, code in languages.items():
    translation = translator.translate(text, dest=code)
    translated_text = translation.text
    print(f"{language}: {translated_text}")
