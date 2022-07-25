import os
import sys

name = 'Prettify Vocabulary Card'

with open(os.path.join(os.path.dirname(__file__), './afmt.html'), 'r') as html:
    afmt = html.read()

with open(os.path.join(os.path.dirname(__file__), './qfmt.html'), 'r') as html:
    qfmt = html.read()

with open(os.path.join(os.path.dirname(__file__), './main.css'), 'r') as file:
    css = file.read()

fields = [
    'ForeignLanguageWord',
    'YourLanguageDefinition',
    'ForeignLanguagePronunciation',
    'ForeignLanguageExplanationWordType_1',
    'ForeignLanguageExplanationDetails_1',
    'ForeignLanguageExplanationWordType_2',
    'ForeignLanguageExplanationDetails_2',
    'ForeignLanguageExplanationWordType_3',
    'ForeignLanguageExplanationDetails_3',
    'YourLanguageExplanationWordType_1',
    'YourLanguageExplanationDetails_1',
    'YourLanguageExplanationWordType_2',
    'YourLanguageExplanationDetails_2',
    'YourLanguageExplanationWordType_3',
    'YourLanguageExplanationDetails_3',
]

templates = [
    {
        'name': 'Vocabulary Card',
        'afmt': afmt,
        'qfmt': qfmt
    }
]