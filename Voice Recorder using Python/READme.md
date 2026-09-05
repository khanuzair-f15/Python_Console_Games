# 🎙️ Python Audio Recorder

A simple Python project that records audio from the system's default microphone and saves the recording as `.wav` files.

The project demonstrates two different approaches to saving recorded audio:

* 🎵 **SciPy** — saves the NumPy audio array as a WAV file.
* 🎚️ **WAVIO** — provides additional control over audio properties such as sample width.

---

## 📌 Introduction

This project uses Python to capture audio directly from an available recording device.

The program records:

* ⏱️ **Duration:** 5 seconds
* 🎚️ **Sample rate:** 44.1 kHz
* 🔊 **Channels:** 1 (Mono)
* 🔢 **Data type:** `int32`

After recording, the same audio data is saved into two separate WAV files using different libraries.

```text
🎙️ Microphone
      │
      ▼
 sounddevice
      │
      ▼
 NumPy Audio Array
      │
      ├───────────────┐
      ▼               ▼
   SciPy            WAVIO
      │               │
      ▼               ▼
recording-0.wav   recording-1.wav
```

---

## ✨ Features

* 🎙️ Records audio from the default recording device
* ⏱️ Records for a fixed 5-second duration
* 🎚️ Uses a 44.1 kHz sampling frequency
* 🔊 Records in mono
* 💾 Saves audio as WAV
* 🔄 Saves the same recording using two different libraries
* 🧪 Demonstrates NumPy-based audio processing

---

## 🛠️ Tech Stack

| Library           | Purpose                                        |
| ----------------- | ---------------------------------------------- |
| 🐍 Python         | Main programming language                      |
| 🎙️ `sounddevice` | Records audio from the input device            |
| 🔢 NumPy          | Stores the recorded audio samples              |
| 🧪 `scipy`        | Saves the NumPy array as a WAV file            |
| 🎚️ `wavio`       | Saves WAV audio with control over sample width |

---

## 📦 Installation

Install the required libraries using pip:

```bash
pip install sounddevice scipy wavio numpy
```

Or:

```bash
pip install sounddevice scipy wavio
```

`NumPy` is used internally by the recording process and is normally installed as a dependency.

---

## ⚙️ Recording Configuration

The project uses:

```python
frequency = 44100
duration = 5
```

### Sample Rate

```text
44,100 samples / second
```

This is commonly referred to as **44.1 kHz**.

### Recording Duration

```text
5 seconds
```

### Audio Channels

The recording uses:

```python
channels=1
```

which means the recording is **mono**.

---

## 🎙️ Recording Audio

The recording is started with:

```python
rec = sd.rec(
    int(frequency * duration),
    samplerate=frequency,
    channels=1,
    dtype='int32'
)
```

The number of samples is calculated using:

```text
samples = sample rate × duration
```

For this project:

```text
44,100 × 5 = 220,500 samples
```

So the program records 220,500 audio samples for the single channel.

---

## ⏳ Waiting for Recording to Finish

After starting the recording:

```python
sd.wait()
```

is used.

This ensures the program waits until the recording operation has finished before attempting to save the audio.

Without waiting, the program could attempt to save the data before recording has completed.

---

# 💾 Saving the Recording

The recorded audio is stored in the variable:

```python
rec
```

This contains the captured audio samples as a NumPy array.

The project then saves this data in **two different ways**.

---

## 1️⃣ Saving with SciPy

```python
write("recording-0.wav", frequency, rec)
```

The `scipy.io.wavfile.write()` function receives:

| Argument            | Meaning             |
| ------------------- | ------------------- |
| `"recording-0.wav"` | Output filename     |
| `frequency`         | Sample rate         |
| `rec`               | Recorded audio data |

The result is:

```text
recording-0.wav
```

---

## 2️⃣ Saving with WAVIO

The project also uses:

```python
wv.write(
    "recording-1.wav",
    rec,
    frequency,
    sampwidth=4
)
```

This creates:

```text
recording-1.wav
```

The important additional parameter is:

```python
sampwidth=4
```

which specifies a **4-byte sample width**.

Since the recording uses `int32`, this corresponds to 32-bit audio samples.

---

## 🔄 Complete Program Flow

```text
              ┌──────────────┐
              │    Start     │
              └──────┬───────┘
                     │
                     ▼
            Set Sample Rate
              44,100 Hz
                     │
                     ▼
             Set Duration
               5 seconds
                     │
                     ▼
           Start Audio Recording
                     │
                     ▼
              sounddevice
                     │
                     ▼
            NumPy Audio Array
                     │
                     ▼
               sd.wait()
                     │
                     ▼
            ┌────────┴─────────┐
            │                  │
            ▼                  ▼
          SciPy              WAVIO
            │                  │
            ▼                  ▼
    recording-0.wav    recording-1.wav
            │                  │
            └────────┬─────────┘
                     ▼
                    End
```

---

## 🧩 Important Functions

| Function     | Purpose                       |
| ------------ | ----------------------------- |
| `sd.rec()`   | Starts audio recording        |
| `sd.wait()`  | Waits for recording to finish |
| `write()`    | Saves audio using SciPy       |
| `wv.write()` | Saves audio using WAVIO       |

---

## 🧠 Concepts Practiced

This project provides practice with:

* 🎙️ Audio recording
* 🔢 NumPy arrays
* 🎚️ Sample rates
* 🔊 Mono audio
* 💾 WAV files
* 📦 External Python libraries
* ⏱️ Audio duration calculation
* 🔄 Converting/storing raw audio data
* 🧪 Comparing different libraries for the same task

---

## 💻 Complete Code

```python
"""
libraries we will use

~ sounddevice = use to directly interact with hardware
  to record or play sound

~ scipy = used to convert NumPy array into .wav file

~ wavio = used to provide better precision
  and bit-depth control
"""

import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

frequency = 44100  # 44.1 kHz frequency
duration = 5       # recording time

# Start recorder with the given duration
# and sample frequency
rec = sd.rec(
    int(frequency * duration),
    samplerate=frequency,
    channels=1,
    dtype='int32'
)

# Wait for the recording to finish
sd.wait()

# Convert the NumPy array to an audio file
# with the given sampling frequency
write("recording-0.wav", frequency, rec)

# Convert the NumPy array to an audio file
wv.write(
    "recording-1.wav",
    rec,
    frequency,
    sampwidth=4
)
```

---

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone <repository-url>
```

### 2. Navigate to the Project

```bash
cd <project-folder>
```

### 3. Install Dependencies

```bash
pip install sounddevice scipy wavio numpy
```

### 4. Run the Program

```bash
python main.py
```

The program will immediately start recording from the default audio input device.

After approximately **5 seconds**, the recording will be saved.

---

## 📁 Output Files

The program generates two WAV files:

```text
📁 Project
│
├── recording-0.wav
└── recording-1.wav
```

### `recording-0.wav`

Created using:

```python
scipy.io.wavfile.write()
```

### `recording-1.wav`

Created using:

```python
wavio.write()
```

Both files contain the same recorded audio data but are written using different libraries.

---

## ⚠️ Known Limitations

There are **no major errors** in the current implementation, but there are some limitations:

### 1. Fixed Recording Duration

The recording duration is hardcoded:

```python
duration = 5
```

Every execution records for exactly 5 seconds.

### 2. Fixed Sample Rate

The sample rate is hardcoded to:

```python
frequency = 44100
```

### 3. Mono Recording

The program uses:

```python
channels=1
```

so it records a single audio channel.

### 4. Default Recording Device

The code doesn't explicitly select a microphone or input device.

It relies on the default device configured by the system.

### 5. No User Interface

There is currently no interface for starting, stopping, or configuring the recording.

### 6. No Recording Error Handling

The program does not currently catch errors such as:

* 🎙️ No microphone available
* 🔒 Microphone permission denied
* ⚙️ Invalid audio device
* 🎚️ Unsupported recording configuration

---

## 🚀 Future Improvements

Possible improvements include:

* 🎙️ Allow users to select their microphone.
* ⏱️ Let users choose the recording duration.
* 🎚️ Allow users to select the sample rate.
* 🔊 Add stereo recording support.
* 🛑 Add a manual stop button.
* ▶️ Add audio playback.
* 📊 Display recording levels in real time.
* 🎛️ Add volume/gain controls.
* 🖥️ Build a graphical user interface.
* 📁 Allow users to choose the output filename.
* 🎵 Add support for additional audio formats.

---

## 📊 Project Structure

```text
Audio-Recorder/
│
├── main.py
├── recording-0.wav
├── recording-1.wav
└── README.md
```

The WAV files are generated when the program is executed.

---

## 📌 Project Status

🟢 **Completed**

Current version successfully:

* ✅ Records audio
* ✅ Uses a 44.1 kHz sample rate
* ✅ Records mono audio
* ✅ Stores audio in a NumPy array
* ✅ Saves the recording using SciPy
* ✅ Saves the recording using WAVIO
* ✅ Generates two WAV files

---

## 🎓 What I Learned

This project demonstrates how Python can interact with audio hardware and process recorded sound.

The key pipeline is:

```text
🎙️ Audio Input
      ↓
sounddevice
      ↓
NumPy Array
      ↓
┌──────────────┬──────────────┐
↓              ↓
SciPy          WAVIO
↓              ↓
WAV File       WAV File
```

It provided practical experience with **audio sampling, NumPy arrays, WAV files, sample rates, bit depth, and Python libraries for working with hardware**.

---

## 👨‍💻 Author

**Uzair Khan**

GitHub: `khanuzair-f15`

Email: `khanuzair.f15@gmail.com`

---

⭐ If you found this project useful, consider giving the repository a star!
