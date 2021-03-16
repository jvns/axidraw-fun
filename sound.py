import sounddevice as sd

fs = 44100  # Sample rate
seconds = 1  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
print(myrecording)
