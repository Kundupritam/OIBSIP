#importing modules
import google.generativeai as genai
import speech_recognition as sr
import pyttsx3
import datetime

#configureing api key
genai.configure(api_key="AIzaSyCt9Fdk-AGhg3bR454MiHZbo0Lz3MagtaI")

#for listening the user command
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query.lower()
    except:
        speak("Sorry, I didn’t catch that.")
        return ""

#generating answers from gemini
def ask_gemini(text):
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(text)
    reply = response.text
    speak(reply)
    print(f"assistent:{reply}")
    return reply

#this is the assistents voice
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

#for time information
def tell_time():
    time_now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {time_now}")
    print(f"time is:{time_now}")

#for date information
def tell_date():
    date_now = datetime.datetime.now().strftime("%A, %d %B %Y")
    speak(f"Today is {date_now}")
    print(f"time is:{date_now}")

#main function for manageing answers
def main():
    active=True
    while active:
        
        text=listen()
        if 'stop' in text :
            speak("bye!")
            active=False
        else:
            if "hello" in text or "hi" in text:
                speak("hi! i am here to help you")
            elif "time" in text:
               tell_time()
            elif "date" in text:
                tell_date()
            else:
               text=text+"answer in 2 or 3 lines"
               ask_gemini(text)

if __name__=="__main__":
    main()

