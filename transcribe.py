import os
from dotenv import load_dotenv
from openai import OpenAI
from pytube import YouTube
import json

load_dotenv(".env")

client = OpenAI()

def ensure_folder(folder):
    """
    This function ensures that the folder exists. If it doesn't, it creates
    the folder.

    Args:
        folder (str): The folder to be created if it doesn't exist.
    """
    if not os.path.exists(folder):
        os.makedirs(folder)

def download_audio(video_url, audio_folder="audio"):
  print(f"Downloading audio for video: {video_url}")
  yt=YouTube(video_url)
  t=yt.streams.filter(only_audio=True)
  ensure_folder(audio_folder)
  return t[0].download(audio_folder)

def transcribe_audio(audio_file_path):
  print(f"Transcribing audio file: {audio_file_path}")
  file = open(audio_file_path, "rb")

  return client.audio.transcriptions.create(
    model="whisper-1", 
    file=file,
    response_format="verbose_json",
    timestamp_granularities=["word"]
  )

audio_file = download_audio("https://www.youtube.com/watch?v=hkgLxhrjfUE&t=3s")
print(f"Saved to: {audio_file}")

transcript = transcribe_audio(audio_file)

# re-create the full transcript using the words as the transcript returned
# from openai is not the same as the list of words
text_from_words = " ".join([entry['word'] for entry in transcript.words])

transcript_obj={}
transcript_obj['original_text'] = transcript.text
transcript_obj['text'] = text_from_words
transcript_obj['words'] = transcript.words

ensure_folder("transcripts")

# Get the file name from the audio file path
file_name = os.path.basename(audio_file)
transcript_file = f"transcripts/{file_name}.json"
with open(transcript_file, "w") as file:
    json.dump(transcript_obj, file)
