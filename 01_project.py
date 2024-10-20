import speech_recognition as sr 
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    if "open google" in command.lower():
        webbrowser.open("https://google.com")
        speak("Opening Google")
    elif "open facebook" in command.lower():
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook")
    elif "open youtube" in command.lower():
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")
    else:
        speak("I did not understand the command.")

if __name__ == "__main__":
    speak("Initializing Jarvin....")
    while True:
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=5)
                word = recognizer.recognize_google(audio)
                if word.lower() == "jarvis":
                    speak("Yes?")
                    # Listen for command
                    with sr.Microphone() as source:
                        recognizer.adjust_for_ambient_noise(source)
                        print("Jarvis Active...")
                        audio = recognizer.listen(source, timeout=5)
                        command = recognizer.recognize_google(audio)
                        print(f"Command: {command}")
                        process_command(command)
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error: {e}")

        # Add a condition to break the loop, for example, if "exit" is said
        if word.lower() == "exit":
            speak("Goodbye!")
            break