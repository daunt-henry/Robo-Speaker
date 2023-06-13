import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.0. Created by Henry")
    while True:
            x = input("Enter what you want me to speak: ")
            if x == "q":
                break
            engine = pyttsx3.init()
            engine.say(x)
            engine.runAndWait()
    '''engine = pyttsx3.init()
     engine.say(x)
     engine.runAndWait() generated using ChatGPT'''


