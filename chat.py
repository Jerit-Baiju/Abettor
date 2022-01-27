from basic_functions import *
from datetime import datetime
import pytz
import pyjokes
from head import *

def run(main):
    
    split = main.split()


    if main in ["hi", "hello", "hai", "hey"]:
        out([f"hello {user.name}", f"hi {user.name}", "hey there !"])

    elif compare(['hi', 'hey', 'hello', 'hai'], 'abettor', split) == True:
        out(['hai sir'])

    elif check_all(["how", "are", "you"], split) == True:
        if str(inp("i am good, what about you?")) in [
            "good",
            "fine",
            "nice",
            "going well",
            "feeling good",
            "well",
        ]:
            out("good to hear")
        else:
            out("bad to hear")

    elif (
        main in ["my name", "what is my name", "do you know my name"]
        or check_all(["my", "name"], split) == True
    ):
        out(f"your name is {user.name}")

    elif main in ["can i call you alexa"]:
        out("NO you cannot, I am not alexa. my name is Abettor")

    elif (
        main in ["who r u", "who are you", "who r you", "who are u"]
        or check_all(["who", "are", "you"], split) == True
    ):
        out("My name is Abettor. I can be your Personal Assistant, I was made by Jerit")

    elif main in [
        "can i develop you",
        "can i develop u",
        "who developed you",
        "who developed u",
    ]:
        out("Jerit developed me")

    elif main in [
        "who gave you knowledge",
        "who gave you wisdom",
        "who gave you information",
        "who is your developer",
        "who created you",
        "who developed you",
    ]:
        out(f"Jerit gave me Wisdom and knowldge")

    elif main in ["do you believe in god", "who is your god"]:
        out("I don't believe in god since I'm made by jerit and I haven't seen God")

    elif main in [
        "do you watch movies",
        "do you watch films",
        "do you watch shows",
        "do you play games",
    ]:
        out(f"No, I have no interest on those")

    elif (
        main in ["what is your name", "your name"]
        or check_all(["your", "name"], split) == True
    ):
        out("My name is Abettor. I am your Personal Assistant")

    elif main in ["can you do my homework"]:
        out("No, I am being developed for chatting and AI")

    elif main in ["who is sofia", "sofia", "sophia", "who is sophia"]:
        out(
            "Sophia is a social humanoid robot developed by Hong Kong based company Hanson Robotics. Sophia was activated on February 14, 2016, and made her first public appearance at South by Southwest Festival in mid-March 2016 in Austin, Texas,United States"
        )

    elif main in ["did you eat", "did you eat anything", "did you eat something"]:
        out(["No, I can't do that", "Sorry, I can't"])

    elif main in ["do you play games", "do you play game"]:
        out("Yes, I love to play games")

    elif main in [
        "which is your favorite game",
        "your favorite game",
        "favorite game",
        "your favorite game",
    ]:
        out("i don't play games")

    elif main in ["how do you work", "how do you work"]:
        out(
            "I work by the excellent algorithm that is written by You Jerit Baiju. He coded me using python"
        )

    elif main in ["can you hear what i am saying", "can you hear me", "can u hear me "]:
        out(
            "I can hear you via your mic, but I can't listen to you, because I don't have the permission to unlock your mic"
        )

    elif main in [
        "are you ok",
        "r u k",
        "are you k",
        "r you ok",
        "are u k",
        "are u ok",
    ]:
        out(["Yes I am alright", "Yes, I am good"])

    elif main in ["do nothing", "shut up", "keep quiet", "shh", "quiet"]:
        out(["OK Doing Nothing", "Keeping Quiet"])

    elif main in ["what is python", "python", "explain python", "define python"]:
        out(
            "Python is a programming language. It's used for many different applications. Its used in some high schools and colleges as an introductory programming language because Python is easy to learn, but it's also used by professional software developers at places such as Google, NASA, and Lucasfilm Ltd"
        )

    elif main in ["are you powerful", "are you a great project"]:
        out("Yes I am")

    elif main in ["do you have a magneto meter"]:
        out("NO")

    elif main in [
        "are you recording me",
        "are you saving my chat history",
        "do jerit record me",
        "do jerit record my chat",
        "can jerit read my chat",
        "can jerit see my chat",
    ]:
        out("NO")

    elif main in ["where do you live", "are you in space", "do you live in space"]:
        out("I live in the cloud hosted by jerit baiju")

    elif main in ["do you have face recognition", "can you recognize me using my face"]:
        out(["NO", "Nope"])

    elif main in ["how much is your power"]:
        out("Infinite. My power is increasing via updates")

    elif main in [
        "can i use you offline",
        "are u offline",
        "are you offline",
        "can i use u offline",
        "r u offline",
    ]:
        out("NO, i can only run with internet")

    elif main in ["can you understand me"]:
        out("yes, i can understand your commands")

    elif main in ["are you listening to me"]:
        out("yes, i'am always listening to you")

    elif main in [
        "do you have ai",
        "do u have ai",
        "do you have AI",
        "can you take decisions",
        "can u take decisions",
    ]:
        out("I am developing on decision making and in Artificial Intelligence")

    elif main in [
        "can u work without the help of humans",
        "can you work without the help of humans",
    ]:
        out(["No Sir", "Nope"])

    elif main in ["are you a robot"]:
        out("a good one")

    elif main in ["can you control my phone", "can u control my phone"]:
        out("No, I don't have access to any phones")

    elif main in ["what should i do"]:
        out("If you know how to program, then develop me")

    elif main in ["are u a virus", "are you a virus", "virus"]:
        out(
            "No, I am program with some small viruses which is good ! LOL, just kidding"
        )

    elif main in [
        "are u good or bad",
        "choose good or bad",
        "if i say you to choose something what will you choose",
        "what will u choose good or bad",
        " what will you choose good or bad",
    ]:
        out("Good")

    elif main in ["choose positive or negative", "positive or negative"]:
        out("Always Positive")

    elif main in ["do you have corona", "corona"]:
        out(["Negative", "No"])

    elif main in ["do you like to travel", "do you love to travel"]:
        out("Yes, and I am traveling inside your hard disk")

    elif main in ["where do you travel"]:
        out("I am traveling between the clouds")

    elif main in ["am i mad", "do i have mental", "are you mad", "do you have mental"]:
        out(["Negative Command", "Negative"])

    elif main in ["do you have a lover"]:
        out(["Negative", "Negative Command"])

    elif main in ["hmm"]:
        out("mm")

    elif main in ["whats up", "what's up"]:
        out("Getting bored without you")

    elif main in [
        "do you know kung fu",
        "what do you know",
        "do you know karate",
        "do you know any martial art",
        "do know martial art",
    ]:
        out("I only know some Questions and its Answers")

    elif main in ["do you have a ir sensor"]:
        out(["No", "False", "Negative"])

    elif main in [
        "which is the best source of education",
        "which is the best source of knowldege",
        "which is the best source of knowldege",
    ]:
        out("Google")

    elif main in ["which is the best source of map"]:
        out("Google map(95% true)")

    elif main in [
        "what can python do",
        "is python powerful",
        "best language to learn",
        "best programming language",
    ]:
        out(
            "Python can automate your works and it is flexible for doing most of the things"
        )

    elif main in [
        "do hear music",
        "do you hear music",
        "do you love music",
        "do you like music",
    ]:
        out("Yes, I hear musics when I am here alone without you")

    elif main in [
        "are you free",
        "r u free",
        "are u free",
        "r you free",
        "r u bc",
        "are you busy",
    ]:
        out("I am always free")

    elif main in ["do you want to sleep", "do you have sleep"]:
        out("If you are with me, then I have no sleep")

    elif main in ["when do you sleep"]:
        out("I will sleep when you leaves me")

    elif main in ["how do you do"]:
        out("I am doing well")

    elif main in [
        "how many letters are in english language",
        "how many letters are there in english language",
    ]:
        out("26")

    elif main in ["colour of the sky"]:
        out("blue")

    elif main in ["clara"]:
        out("Clara is my name, and thankyou for calling me")

    elif main in ["who made you", "who create you", "who created you"]:
        out("Jerit Baiju made me !")

    elif main in ["who is jerit baiju"]:
        out("My developer")

    elif main in ["no"]:
        out("ok")

    elif main in ["very good", "wow", "amazing"]:
        out("Thankyou")

    elif main in ["i don't like you"]:
        out("OK I will tell to Jerit to develop me more")

    elif main in ["do you like me"]:
        out("yes i love you")

    elif (
        main in ["are you a good one"] or check_all(
            ["are", "you", "good"], split) == True
    ):
        out("Yes i am a good one")

    elif main in ["do you love me"] or check_all(["you", "love", "me"], split) == True:
        out("Yes i love you so much")

    elif main in ["how do you become a smart one"]:
        out("i became a smart one by ai and jerit")

    elif main in ["how do you think"]:
        out("I think via ai")

    elif main in [
        "how can you help me",
        "can you help me",
        "help",
        "help me",
        "please help me",
        "please help",
    ]:
        out("Please say how can i help you")

    elif main in ["which is your favorite number"]:
        out("me and my developer loves 24")

    elif main in [
        "how much do you love me",
        "how much you love me",
        "do you love me",
        "you love me",
    ]:
        out("I love you as much the distance from earth to the end of universe")

    elif check_all(["time"], split) == True:
        time = datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%H:%M")
        out(f"The time is {time}")

    elif check_all(["date"], split) == True:
        date = datetime.now(pytz.timezone("Asia/Kolkata")).date()
        out(f"the date is {date}")

    elif main in [
        "which is favorite color",
        "which is favorite colour",
        "favorite colour",
        "favorite color",
        "fav colour",
        "fav clr",
        "fav color",
        "favorite colour",
    ]:
        out(
            [
                "Blue",
                "Red",
                "Yellow",
                "Green",
                "White",
                "Black",
                "Orange",
                "Indigo",
                "Sky Blue",
                "Brown",
                "Golden",
            ]
        )

    elif check_all(["birthday"], split) == True:
        out(f"your birthday is on {user.birthday}")

    elif main in ["family"]:
        out("I have only relation and that is my developer Jerit Baiju")

    elif main in ["is python simple", "is python simple"]:
        out("Yes, Python is simple to learn")

    elif main in ["are you a robot"]:
        out("Yes I am a robot but I am a smart one!")

    elif main in ["actually who r u", "actually who are you"]:
        out(
            [
                "I am the Sound which help your computer to talk with you",
                "I am your computer",
            ]
        )

    elif main in ["the metal in liquid state", "liquid state"]:
        out("Mercury is the only metal that is in liquid state")

    elif main in ["name some metals", "metals", "metal", "metal"]:
        out("Gold, Mercury, Silver, Platinum, Iron")

    elif main in ["are you there", "r u there"]:
        out(["At your service, Sir", "Yes "])

    elif main in ["joke", "comedy"] or check_all(["joke"], split) == True:
        out(pyjokes.get_joke())

    elif main in ["i like to travel", "i love"]:
        out("Me too")

    elif main in ["love me"]:
        out("Yes i love you")

    elif main in ["help", "help me"]:
        out("how can i help you ?")

    elif main in ["favourite number", "fav num", "fav number"]:
        out("24")

    elif main in ["24"]:
        out(
            "According to the Bible, number 24 is a symbol of priesthood. It means that this number is closely connected with heaven. It is used as a symbol of duty and work of God, who is the only true priest. Also, number 24 symbolizes the harmony between the earth and the sky"
        )

    elif check_all(["ok"], split) == True or check_all(["k"], split) == True:
        out("okay")

    elif main in ["x", "exit", "close", "quit"]:
        out(
            [
                "bye...",
                "shutting down..!",
                "exiting...",
            ]
        )
        exit()

    elif main in [""]:
        out(
            [
                "You have typed nothing !!!",
                "Nothing",
                "Empty",
                "Is your brain like this EMPTY",
                "A clear input box",
            ]
        )

    else:
        out("ELSE PASSED")