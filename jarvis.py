import pyttsx3 #for audio speak
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5') # microsoft speech api sapi5
voices = engine.getProperty('voices') #windows inbuilt voice api
engine.setProperty('voice',voices[0].id) #  change 0 or 1 for make femalee voices



def speak(audio):
	"""function to speak a given string"""
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	""" calling speak function to speak"""
	hour = int(datetime.datetime.now().hour)
	if  hour>=0 and hour < 12:
		speak("Good morning!")
	if  hour>=12 and hour < 18:
		speak("Good afternoon!")
	else:
		speak("Good evening!")		
	speak("I am Friday Sir. How may i help you" )	

def takeCommand():
	#takes microphone input from the user and returns string output
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		# r.energy_threshold = 20
		# r.adjust_for_ambient_noise(source,duration=1)
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language='en-in')
		print(f"User said: {query}\n")
	except Exception as e:
		print(e)
		print("Say that again please...")
		return "None"	
	return query	
		
def sendEmail(to, content): # enable less secure app in gmail from which we wanna send mail
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login('sureshmoharana40@gmail.com','password')
	server.sendmail('sureshmoharana40@gmail.com',to,content)
	server.close()

if __name__ == '__main__':
	wishMe()
	# speak("Hi suresh")
	while True:
	# if 1:
		query = takeCommand().lower()
		#Logic for executing tasks based on query
		if 'wikipedia' in query:
			speak("searching wikipedia")
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences=2) # how many sentences to read out
			speak("According to wikipedia")
			speak(results)

		elif 'open youtube' in query:
			webbrowser.open("youtube.com")

		elif 'open google' in query:
			webbrowser.open("google.com")	

		elif 'open stackoverflow' in query:
			webbrowser.open("stackoverflow.com")

		elif 'play music' in query:
			music_dir = 'D:\\songs'
			songs = os.listdir(music_dir)
			print(songs)
			os.startfile(os.path.join(music_dir,songs[0]))

		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:S%")
			speak(f"Sir the time is {strTime}")

		elif 'open sublime_code' in query:
			sublime_code_path = ""
			os.startfile(sublime_code_path)

		elif 'email to suresh' in query:
			try:
				speak("what should i say")
				content = takeCommand()	
				to = "suresh@gmail.com"
				sendEmail(to, content)
				speak("Email has been sent")
			except Exception as e:
				print(e)	
				speak("Sorry unable to send email at the moment")

