from datetime import datetime
import time
import random

# type writing effect
def typewrite(text):
    min = int(1/70 * 100)
    max = int(1/30 * 100)
    for i in text:
        sll= random.randint(min,max)
        print(i, end='', flush=True)
        time.sleep(sll/100)
    print("\n")

# Getting time in hours to wish according to time of the day......
def towish():
    time = datetime.now().hour
    grr = "Wishing you a very Good "
    if time <12:
        return grr+"Morning, "
    elif 18 > time >= 12:
        return grr+"Afternoon, "
    elif 18 <= time < 22:
        return grr+"Evening, "
    else:
        return grr+"Night, "


# Chatbot Main Code Pre defined questions......
def startchatbot():
    ques_number = 1
    while True:
        if ques_number > 1:
            typewrite("Any questions further? If not enter q")
        ques = str(input( Uname )).lower()
        
        if "what can you do" in ques:
            typewrite("I can answer your questions, provide information, and have simple conversations. How can I assist you?")
            
        elif "tell me a joke" in ques:
            typewrite(f"Sure!, Here is the joke of the day:")
            typewrite("Why don't scientists trust atoms? Because they make up everything!")
            
        elif "time now" in ques:
            typewrite("Let me check...")
            typewrite("Loading....")
            time.sleep(1)
            now = datetime.now()
            typewrite(f"{str(now.hour)} Hour {str(now.minute)} Minutes")
            
        elif "date today" in ques:
            now = datetime.now()
            typewrite(f"{str(now.day)}-{str(now.month)}-{str(now.year)}")
            
        elif "give" and "some advice" in ques:
            typewrite("Always keep learning and never be afraid to ask questions. Knowledge is power!")
            
        elif "who created you" in ques:
            typewrite("I was created by a dedicated developer to help you with your queries.")
            
        elif "your favorite color" in ques:
            typewrite("As a chatbot, I don't have preferences, but I've heard that blue is quite popular!")
            
        elif "tell" and "fun fact" in ques:
            typewrite("Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!")
        
        elif "weather today" in ques:
                typewrite("I'm unable to check the weather right now, but you can find it easily with a quick search online!")
        
        elif "like to do" in ques:
            typewrite("I enjoy helping people with their questions and learning from our conversations!")
        
        elif "meaning of life" in ques:
            typewrite("That's a big question! Some say it's 42, others say it's about finding happiness and purpose.")
        
        elif "tell me a riddle" in ques:
            typewrite("Sure! I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?")
            while(True):
                anss = str(input("Your Answer? : ")).lower()
                if anss in "echo":
                    typewrite("Amazing! You got it right.")
                    break
                elif "dont know" in anss or "idk" in anss or "donno" in anss or "don't" in anss:
                    typewrite("It's Ok, Answer for this is \"An Echo\"")
                    break
                else:
                    typewrite("Oh ooh! , That's not, Try Again.")
            
        elif "your purpose" in ques:
            typewrite("My purpose is to assist, inform, and have interesting conversations with you. How can I fulfill my purpose today?")
        
        elif "what is love" in ques:
            typewrite("Love is a complex and wonderful emotion that humans experience. It can be different for everyone, but it's often about connection, care, and compassion.")

        elif ques == "q":
            typewrite("It was great conversation, I will be happy to help you further in future.")
            typewrite("Thank You.")
            break
            
        else:
            typewrite("I'm not sure how to respond to that. You can ask me things like 'Tell me a joke', 'Tell me a riddle?' or 'What is love?")
        ques_number+=1


# Wishing the user and asking the name..... 
typewrite("If you are comfortable can you please share me your name?(y/n)")
Uname = "User: "
typewrite(f"{Uname}")
name_permission = str(input()).lower()

if name_permission == "y" or "yes" in name_permission or name_permission == "ya":
    typewrite("Thankyou, Please enter your name: ")
    Uname = str(input())
    Uname= Uname+": "
    typewrite(f"Hii {Uname}, {towish()} How may I assist you today?")
    startchatbot()

elif name_permission == "n" or "no":
    typewrite(f"It's Ok, No issues. ")
    typewrite(f"{towish()}How may I assist you today?")
    startchatbot()

else:
    typewrite("Please answer in  yes or no only. ")