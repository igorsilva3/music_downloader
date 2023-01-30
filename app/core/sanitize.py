import string
import unidecode

def sanitize_string(input_string):
    input_string = unidecode.unidecode(input_string)
    input_string = input_string.translate(str.maketrans('', '', string.punctuation)).lower()
    
    input_string = " ".join(input_string.split())
    input_string = input_string.replace(" ", "-")
    
    return input_string