import speech_recognition as sr
import webbrowser
import requests
from gtts import gTTS
import os
import pygame

# Initialize the recognizer
recognizer = sr.Recognizer()
newsapi = "06edd8964486438ab846af0ab0cb34ec"

# Music library
music = {
    "heeriye": "https://www.youtube.com/watch?v=RLzC55ai0eo",
    "sathiya": "https://www.youtube.com/watch?v=9J_isuHe8bw",
    "arijit": "https://www.youtube.com/watch?v=kXHiIxx2atA",
    "ve": "https://www.youtube.com/watch?v=QXJyMpxd210"
}

# Function to convert text to speech using gTTS and play using pygame
def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue  # Wait for the speech to finish playing

    pygame.mixer.music.stop()  # Stop the music playback
    pygame.mixer.quit()  # Uninitialize the mixer

    os.remove("output.mp3")  # Now safely remove the file

if __name__ == "__main__":
    speak("Initializing Jarvis.......")

# Main loop to listen for the wake word and commands
while True:
    try:
        with sr.Microphone() as source:
            # Listen for the wake word with reduced timeout
            print("Listening for wake word...")
            audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)
            
        print("Recognizing wake word...")
        wake_word = recognizer.recognize_google(audio).lower()
        
        if "jarvis" in wake_word:
            speak("Yes, Please Speak User..")
            print("Listening for command...")
            with sr.Microphone() as source:
                # Listen for the command with reduced timeout
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=5)
            
            print("Recognizing command...")
            command = recognizer.recognize_google(audio).lower()
            print(f"Command: {command}")
            
            # Execute the corresponding action based on the command
            if "open google" in command:
                webbrowser.open("https://www.google.com")
                speak("Opening Google")

            elif "open linkedin" in command:
                webbrowser.open("https://www.linkedin.com")
                speak("Opening LinkedIn")

            elif "open youtube" in command:
                webbrowser.open("https://www.youtube.com")
                speak("Opening YouTube")
        
            elif "play" in command:
                # Play a song from the music library
                for song in music:
                    if song in command:
                        webbrowser.open(music[song])
                        speak(f"Playing {song}")
                        break
                else:
                    speak("Sorry, I couldn't find the song in the music library.")

            elif "news" in command:
                # Fetch news headlines from the NewsAPI
                response = requests.get(f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={newsapi}")
                news_data = response.json()

                if news_data["status"] == "ok":
                    speak("Here are the top headlines.")
                    for i, article in enumerate(news_data["articles"][:5], 1):
                        print(f"Headline {i}: {article['title']}")
                        speak(f"Headline {i}: {article['title']}")
                else:
                    speak("Sorry, I couldn't fetch the news.")
                    

    except sr.WaitTimeoutError:
        print("Listening timed out while waiting for phrase to start")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
