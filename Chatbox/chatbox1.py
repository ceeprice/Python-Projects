import datetime
import wikipedia
import names
import sys
now = datetime.datetime.now()
botname = names.get_first_name()
message = ("My name is " + botname + ", what is your name? ")

def UNinput():
    global message
    usersname = raw_input(message)
    words = usersname.split(" ")
    #print(stopwords)
    for i in range(0,len(words)):
        word = words[i]
        if word.lower() and word.lower()+"\n" not in stopwords: 
            global mood
            mood = raw_input("Hello " + word.title() + ", how are you today? ")
            global name
            name = word.title()
        elif i == len(words)-1: 
            message = "Sorry, I didn't recognise that. Try again. "
            UNinput()
            
def wikiStart():
    global subject
    subject = raw_input("Let's talk about something. Pick a subject. ")
    if subject == "": wikiStart()
    subWords = subject.split(" ")
    for i in range(0,len(subWords)):
        word = subWords[i]
        if (word.lower() and word.lower()+"\n") not in stopwords:
            subject = word.lower()
            print("Awesome, let's talk about " + subject + ".")
        elif i==len(subWords)-1:
                print("Pick another topic, maybe?")
                wikiStart()
    global results
    results = wikipedia.search('"' + subject + '"')
    answer = raw_input("I got " + results[0] + ", " + results[1] + ", and " + results[2] + " for " + subject + ". Any of those take your fancy? ")
    global subjA
    if "no" in answer:
        tryagain = raw_input("Sorry, I guess those were pretty boring, huh. Try something else?")
        if "yes" or "yeah" or "ok" or "okay" or "alright" in tryagain.lower():
            wikiStart()
        else:
            print("You're not good at this conversation thing, are you?")
    else:
        for i in range(0,len(results)):
            if results[i] in answer.title():
                print("Awesome, let me tell you about " + results[i] + ".")
                print wikipedia.summary('"' + results[i] + '"')
                print("Was nice talking to you, " + name + ". " + botname + " out! Kudos!")
                sys.exit()

            elif i==len(results)-1:
                print("Okay, let's try again.")
                wikiStart()
        

if (int(now.hour) >= 12 and int(now.hour) < 18): print("Good afternoon!")
elif (int(now.hour) >= 18): print("Good evening!")
elif (int(now.hour) < 12): print("Good morning!")
stpw = open("stopwords.txt", "r")
stopwords = stpw.readlines()
UNinput()
positive = set(["good", "awesome", "excellent", "okay", "great"])
negative = set(["bad", "tired", "upset"])
mood = mood.split(" ")
for i in range(0,len(mood)):
    keyword = mood[i]
    if keyword in positive:
        print("Good to hear!")
    elif keyword in negative:
        print("Sorry about that :( have a cookie.")
        q = raw_input("You want to talk about it? ")
        y = set(["yes", "okay", "fine"])
        n = set(["no", "not really"])
        m = set(["maybe", "perhaps"])
        if q.lower() in y: 
            issue = raw_input("What's bothering you, " + name + "? ")
            print("Sorry to hear that. :( Maybe I can take your mind off it.")
        else: 
            print("I'm here if you need me. Have another cookie." )
    else:
        print("I hope you're doing okay, " + name + ".")
    wikiStart()
#print wikipedia.summary('"' + subject + '"')
    
        
