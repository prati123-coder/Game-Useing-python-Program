import speech_recognition as sr 
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com)")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com)")
                
if __name__=="__main__":
    speak("Initializing Jarvin....")
    while True:
        # listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        


        print("recognizing...")
        try:
           with sr.Microphone() as source:
               print("Listening...")
               audio = r.listen(source, timeout=2, phrase_time_limit=1)
               word = r.recognize_google(audio)
               if(word.lower() == "jarvis"):
                speak("ya")
                #lisen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen()
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))

