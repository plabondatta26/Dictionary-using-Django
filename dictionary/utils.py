import json
from .models import Dictionary

def file_model(fildir):
    data= json.load(open(fildir))
    for key,value in data.items():
        dictionary = Dictionary(word = key, definition=value[0])
        dictionary.save()