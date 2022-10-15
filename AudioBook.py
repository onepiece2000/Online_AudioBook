import pyttsx3
import webbrowser
book = webbrowser.open("https://open.spotify.com/")
book_text=book.readlines()
engine = pyttsx3.init()
for i in book_text:
    engine.say(i)
    engine.runAndWait()
 