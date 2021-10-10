import pyttsx3
import os
import datetime
import webbrowser


def chat():
  jarvis = pyttsx3.init()
  text = input("How can i help you  :  ")
  jarvis.say(text)
  jarvis.runAndWait()
  chat=text.lower()
  if chat == "date":
      date()
  elif chat == "help":
      help()      
  elif chat == "time":
      time()
  elif chat == "name":
      name()
  elif chat == "yt":
      yt()
  elif chat == "google":
      google()
  elif chat == "wiki":
      wikipedia()
  elif chat == "news":
      news()
  elif chat == "chess":
      chess()         
  elif chat == "notepad":
      notepad()                   
  elif chat == "shutdown":
      shutdown()
  elif chat == "stop":
      stop()          
  else:
      unable()

      
     
  
def unable():
  jarvis = pyttsx3.init()
  jarvis.say("Sorry sir i am Unable to understand that")
  print("Sorry sir i am Unable to understand that")
  jarvis.runAndWait() 
  chat()


def help():
          print(" \n All Available Commands which you can use :       \n")
          print(" name     : Type name     for asking me my name.     \n")
          print(" date     : Type date     for finding date           \n")
          print(" time     : Type time     for finding time           \n")
          print(" yt       : Type yt       for Opening Youtube        \n")
          print(" google   : Type google   for Opening Google         \n")
          print(" wiki     : Type wiki     for Opening Wikipedia      \n")
          print(" news     : Type news     for Opening Google News    \n")
          print(" chess    : Type chess    for Opening Chess          \n")
          print(" notepad  : Type notepad  for Opening Notepad        \n")
          print(" shutdown : Type shutdown for shutting down pc       \n")
          print(" stop     : Type stop     for closing the jarvis bot \n")
          chat()


def name():
  jarvis = pyttsx3.init()
  jarvis.say("Hello sir I am Jarvis nice to meet you")
  print("Hello sir I am Jarvis nice to meet you")
  jarvis.runAndWait()
  chat()  





def notepad():
  np = pyttsx3.init()
  np.say("Opening Notepad")
  print("Opening Notepad")
  np.runAndWait()
  os.system("Notepad")
  chat()  





def date():
  day = pyttsx3.init()
  x = datetime.datetime.now()
  today = x.strftime("%d %B %Y")
  day.say("Today is "+ today +"")
  print("Today is "+ today +"")
  day.runAndWait()
  chat()





def time():
  date = pyttsx3.init()
  x = datetime.datetime.now()
  time = x.strftime("%X %p")
  date.say("Time is "+ time +"")
  print("Time is "+ time +"")
  date.runAndWait()
  chat()




def yt():
  youtube = pyttsx3.init()
  youtube.say("Opening Youtube")
  print("Opening Youtube")
  youtube.runAndWait()
  webbrowser.open('https://www.youtube.com/')
  chat()




def news():
  news = pyttsx3.init()
  news.say("Opening News site")
  print("Opening News Site")
  news.runAndWait()
  webbrowser.open('https://news.google.com/')
  chat()




def google():
  google = pyttsx3.init()
  google.say("Opening Google")
  print("Opening Google")
  google.runAndWait()
  webbrowser.open('https://www.google.com/')
  chat()



def chess():
  chess = pyttsx3.init()
  chess.say("Opening Chess")
  print("Opening Chess.")
  chess.runAndWait()
  webbrowser.open('https://www.chess.com/')
  chat()




def wikipedia():
  wiki = pyttsx3.init()
  wiki.say("Opening Wikipedia")
  print("Opening Wikipedia")
  wiki.runAndWait()
  webbrowser.open('https://www.wikipedia.org/')
  chat()




def stop():
   stop = pyttsx3.init()
   stop.say("Sir Do you want to close me?")
   stop.runAndWait()
   ask = input("Do you want to close me ? (y / n): ")
   if ask == 'n':
       nostop = pyttsx3.init()
       nostop.say("Closing Process Aborted")
       print("Closing Process Aborted.")
       nostop.runAndWait()
       chat()
   else:
       stop = pyttsx3.init()
       stop.say("Bye Bye sir Hope to see you again")
       print("Bye Bye sir  Hope to see you again")
       stop.runAndWait()
       exit()

 
    
   
def shutdown():
   shut = pyttsx3.init()
   shut.say("Sir Do you want to shutdown your computer ?")
   shut.runAndWait()
   ask = input("Do you want to shutdown your computer ? (y / n): ")
   if ask == 'n':
       noshut = pyttsx3.init()
       noshut.say("Shut down Process Aborted")
       print("Shut down Process Aborted.")
       noshut.runAndWait()
       chat()
   else:
       shut = pyttsx3.init()
       shut.say("Shutting Down Pc Have a nice day")
       print("Shutting Down Pc .Have a nice day")
       shut.runAndWait()
       os.system("shutdown /s /t 1")
