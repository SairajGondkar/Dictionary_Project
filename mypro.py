import json
from difflib import get_close_matches
data=json.load(open("data.json"))
def translate(w):
    w=w.lower()
    if w in data:
        return(data[w])
    elif(w.title() in data):
        return(data[w.title()])
    elif(w.upper() in data):
        return(data[w.upper()])
    elif(len(get_close_matches(w,data.keys()))>0):
        yn=input("Did you mean the word {s}? {d} ".format(s=get_close_matches(w,data.keys())[0],d="Enter Y if yes and N if no: "))
        yn=yn.lower()
        if(yn=="y"):
            c=get_close_matches(w,data.keys())[0]
            return(data[c])
        elif(yn=="n"):
            return("Word does not exist!")
        else:
            return("Wrong choice entered")
    else:
        return("Word does no exist")
word=input("Enter the word: ")
output=translate(word)
if(isinstance(output,list)==True):
    cnt=0
    for i in output:
        cnt+=1
        print("{s}. {d}".format(s=cnt,d=i))
else:
    print(output)