"""libraries we will use
~ sounddevice = use to directly intract with hardware to record or play sound
~ scipy is used to convert numpy array into .wav file
~ wavio is use to increase better precison and bit depth control

"""
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

frequency = 44100  # 44.1 khz frequency
duration = 5  # recording time

# Start recorder with the given values of
# duration and sample frequency
rec = sd.rec(int(frequency * duration), samplerate=frequency, channels=1, dtype='int32')
# Record audio for the given number of seconds
sd.wait()

# This will convert the NumPy array to an audio
# file with the given sampling frequency
write("recording-0.wav", frequency, rec)

# Convert the NumPy array to audio file
wv.write("recording-1.wav", rec, frequency, sampwidth=4)
