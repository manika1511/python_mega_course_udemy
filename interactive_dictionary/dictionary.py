import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))

def meaning(word):
    word = word.lower()
    if word in data.keys():
        return data[word]
    else:
        close_matches = get_close_matches(word,data.keys(), n=3, cutoff=0.8)
        if len(close_matches) == 0:
            return ("No such word exists. Please check it again.")
        else:
            resp = input("Did you mean " + close_matches[0] + " intead? Enter Y if yes, else N if no: ")
            if resp.lower() == 'y':
                return data[close_matches[0]]
            elif resp.lower() == "n":
                return ("No such word exists. Please check it again.")
            else:
                return ("Please enter the valid response.")

word = input("Enter a word: ")
output = meaning(word)

if type(output) == list:
    for item in output:
        print (item)
else:
    print (output)
