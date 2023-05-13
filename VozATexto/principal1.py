import speech_recognition as sr
filename = "C:/Users/Jairo/Documents/Sound recordings/record.wav"
# initialize the recognizer
r = sr.Recognizer()

# open the file
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data, language='es-ES')
    print(text)