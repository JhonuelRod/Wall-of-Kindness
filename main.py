from flask import Flask, render_template, jsonify,request
from better_profanity import profanity
import random

app = Flask(__name__)

def filtered_messages1():
    with open("Messages.txt") as file:
        read = [line.strip() for line in file.readlines()]
        
    with open("CleanMessages.txt") as file:
        contents = set(line.strip() for line in file.readlines())

    with open("profanity_wordlist.txt","r") as file:
        badwords = file.read().splitlines()
        
    profanity.add_censor_words(badwords)

    modified2 = []

    for line in read:
        val = line.find("\t")
        if val == -1:
            continue

        qoute = line[val+1:].strip()
        if qoute not in contents:
            if(profanity.contains_profanity(line) == False):
                modified2.append(line[val+1:])

    return modified2

            
def messages():
    messages = filtered_messages1()
    return messages

def getRandom():
    with open("CleanMessages.txt","r") as file:
        list = file.readlines()
    length = len(list)

    x = random.randint(1, length-1)
    return list[x]

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
@app.route("/")
def public_page():
    return render_template(
        "index.html",
        message1=getRandom(), 
        message2=getRandom(), 
        message3=getRandom(), 
        message4=getRandom(), 
        message5=getRandom(), 
        message6=getRandom())

@app.route("/dev-page")
def dev_page():
    quotes = messages()
    length = len(quotes)
    print(quotes)
    return render_template("DevPage2.html", q=quotes, length=length)

@app.route("/add-q", methods=['POST'])
def add_q():
    fq = request.get_json()
    with open("CleanMessages.txt","a") as file:
        file.write(fq["fq"]+"\n")
    #list.append(fq["fq"])
    return jsonify(fq)

if __name__ == "__main__":
    app.run(debug=True)
