import requests

# Upload a multilingual voice
with open("mono_44100_165187__blaukreuz__global-village-hochdeutsch.wav", "rb") as voice_file:
    response = requests.post(
        "http://localhost:4123/voices",
        data={
            "voice_name": "german_speaker",
            "language": "de"
        },
        files={
            "voice_file": ("mono_44100_165187__blaukreuz__global-village-hochdeutsch.wav", voice_file, "audio/wav")
        }
    )

# print(f"Upload status: {response.status_code}")

# Generate German speech
response = requests.post(
    "http://localhost:4123/v1/audio/speech",
    json={
        "input": "Und es hat auch ein paar Parameter mehr, wie zum Beispiel exaggeration und Temperatur! So, jetzt erstmal pennen!",
        # "input": "Guten Tag! Wie geht es Ihnen?",
        "voice": "german_speaker",
        "exaggeration": 0.8,
        "temperature": 1.0
    }
)

# with open("german_output.wav", "wb") as f:
#     f.write(response.content)

from pydub import AudioSegment
import io
wav_buf = io.BytesIO(response.content)
audio = AudioSegment.from_file(wav_buf, format="wav")

audio.export(
    "german_output.mp3",
    format="mp3",
    bitrate="192k"
)

print("✓ Saved german_output.mp3")