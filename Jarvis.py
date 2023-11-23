import pyttsx3
import speech_recognition as sr
from playsound import playsound
import threading
import time

r = sr.Recognizer()
    
def SpeakText(command) :
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.setProperty('rate', 150)
    engine.say(command)
    engine.runAndWait()

#Récuperation de la voix :
def record_text():
    while(1):
        try:
            with sr.Microphone() as source2 :
                r.adjust_for_ambient_noise(source2, duration=0.2)
                print("I'm listening")
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                return MyText
        except sr.RequestError as e :
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("unknown error occured")

def fake_loading(message, duration):
    progress_symbols = "⭐️"
    progress_bar_length = 10
    print(message + " [", end="")

    for _ in range(progress_bar_length):
        print(progress_symbols, end="", flush=True)
        time.sleep(duration / progress_bar_length)

    print("] Done")

def playintro(sound):
    playsound(sound) 

def send_ollama():
    print("coucou")
  
def main(): 
    
    speak_thread = threading.Thread(target=playintro, args=("sounds/Boot.mp3",))
    loading_thread = threading.Thread(target=fake_loading, args=("BOOT of ARC REACTOR Process", 15))

    # Démarre les threads
    speak_thread.start()
    loading_thread.start()

    # Attends que les threads se terminent avant de continuer
    speak_thread.join()
    loading_thread.join()

    SpeakText("Jarvis is now initialized and ready to assist you.")

    while(1):
        response = record_text()
        if "goodbye" in response :
            # Crée deux threads pour exécuter les deux fonctions en parallèle
            speak_thread = threading.Thread(target=SpeakText, args=("Goodbye my lord",))
            loading_thread = threading.Thread(target=fake_loading, args=("Unloading the ARC REACTOR Process", 2))

            # Démarre les threads
            speak_thread.start()
            loading_thread.start()

            # Attends que les threads se terminent avant de continuer
            speak_thread.join()
            loading_thread.join()
            playsound('sounds/Repulsor.mp3')
            exit()
        else :
            print(response)
            SpeakText(response)

if __name__ == "__main__":
    main()


