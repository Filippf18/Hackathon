#proiect hackathon 
#pip install SpeechRecognition pyaudio
import speech_recognition as sr
# Initialize recognizer

recognizer = sr.Recognizer()

# Use the default microphone as the audio source

with sr.Microphone() as source:

    print("🎤 Please speak something...")

    recognizer.adjust_for_ambient_noise(source)

    audio = recognizer.listen(source)

    print("🧠 Recognizing...")

    try:

        # Recognize speech using Google Web Speech API

        text = recognizer.recognize_google(audio)

        print("📝 You said:", text)

    except sr.UnknownValueError:

        print("😕 Sorry, I could not understand the audio.")

    except sr.RequestError as e:

        print("Could not request results; {e}")
        