# -*- coding: utf-8 -*-

from languages import LANGUAGES

"""This is the entry point of the program."""

def detect_language(text, languages):
    """Returns the detected language of given text."""
    # implement your solution here
    words = text.split()
    count_matches = 0
    output = ''
    for lang in languages:
        
        matches = [word for word in words if word.lower() in lang['common_words']]
        if (len(matches) > count_matches):
            output = lang['name']
            count_matches = len(matches)
    return output
    
    
