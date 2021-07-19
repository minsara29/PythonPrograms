#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing libraries 
import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence
import azure.cognitiveservices.speech as speechsdk
import io
from google.cloud import speech
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="E:\Jupyter_work\speechtotextcheck-ead4c264c839.json"
import glob
import subprocess
import sys
from IPython.display import Audio
import speech_recognition as sr
from moviepy.editor import *
import pandas as pd
import numpy as np

# create a speech recognition object
r = sr.Recognizer()



#Azure License Key
speech_config = speechsdk.SpeechConfig(subscription="01cbd52d8d30422db14ac6201c2c8a21", region="eastus")

#Folder for broken down audio chunks
folder_name = "audio-chunks"


# In[ ]:



# In[2]:
# a function that splits the audio file into chunks

def Audio_Chunk_Maker(path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    # open the audio file using pydub
    sound = AudioSegment.from_wav(path)  
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
        # experiment with this value for your target audio file
        min_silence_len = 500,
        # adjust this per requirement
        silence_thresh = sound.dBFS-14,
        # keep the silence for 1 second, adjustable as well
        keep_silence=500,
    )
    #folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
        
    return chunks

    


# In[3]:


def get_large_audio_transcription_google(path):
    chunks = Audio_Chunk_Maker(path)
    
    whole_text = ""
    # process each chunk 
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav", bitrate ='192k')
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            try:
                text = r.recognize_google(audio_listened)
                text = f"{text.capitalize()}. "                
            except:
                text = "Error:"
            whole_text += text
    # return the text for all chunks detected
    print("-" * 20)        
    print(whole_text)
    print("-" * 20)        
    return whole_text


# In[4]:


def get_large_audio_transcription_azure(path):
       
    chunks = Audio_Chunk_Maker(path)
    
    whole_text = ""
    # process each chunk 
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav", bitrate ='192k')
        # recognize the chunk
        audio_input = speechsdk.AudioConfig(filename=chunk_filename)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)
        result = speech_recognizer.recognize_once_async().get()
        whole_text += result.text

    print("-" * 20)        
    print(whole_text)
    print("-" * 20)        

    return whole_text


# In[5]:


def get_large_audio_transcription_google_enhanced(path):
     
        
    chunks = Audio_Chunk_Maker(path)
    
    whole_text = ""
    #Google Client
    client = speech.SpeechClient()
    # process each chunk 
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav", bitrate ='192k')
        # recognize the chunk
        path = chunk_filename
        with io.open(path, "rb") as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            #encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            #sample_rate_hertz=8000,
            language_code="en-US",
            use_enhanced=True,
            audio_channel_count=2,
            # A model must be specified to use enhanced model.
            model="video",
            # Enable automatic punctuation
            enable_automatic_punctuation=True,
        )

        response = client.recognize(config=config, audio=audio)

        for i, result in enumerate(response.results):
            alternative = result.alternatives[0] 
            whole_text += format(alternative.transcript)
    print("-" * 20)        
    print(whole_text)
    print("-" * 20)
    return whole_text


# In[6]:


def Video_Audio_Converter(dir):
    
    video_filelist = [i for i in os.listdir(dir) if '.mp4' in i]
    
    for filename in video_filelist:
        
        video_filepath = """{}/{}""".format(dir,filename)
        audio_filepath = """{}/{}""".format(dir,filename.replace('.mp4','.wav'))
        
        videoclip = VideoFileClip(video_filepath)

        audioclip = videoclip.audio
        audioclip.write_audiofile(audio_filepath)

        audioclip.close()
        videoclip.close()


# In[7]:


def Batch_Audio_Speech_Google_Enhanced(dir):
    
    audio_filelist = [i for i in os.listdir(dir) if '.wav' in i]
    result_dict = []
    for filename in audio_filelist:
        audio_filepath = """{}/{}""".format(dir,filename)
        transcription = get_large_audio_transcription_google_enhanced(audio_filepath)
        result_dict.append(transcription)
    return result_dict


# In[8]:


def Batch_Audio_Speech_Google_Regular(dir):
    
    audio_filelist = [i for i in os.listdir(dir) if '.wav' in i]
    result_dict = []
    for filename in audio_filelist:
        audio_filepath = """{}/{}""".format(dir,filename)
        transcription = get_large_audio_transcription_google(audio_filepath)  
        result_dict.append(transcription)
    return result_dict


# In[9]:


#Function to transcribe all the video files with Azure in the folder and return a list of transcripts, you can edit this code to add parsing time if needed
def Batch_Audio_Speech_Azure(dir):
    
    audio_filelist = [i for i in os.listdir(dir) if '.wav' in i]
    result_dict = []
    for filename in audio_filelist:
        audio_filepath = """{}/{}""".format(dir,filename)
        transcription = get_large_audio_transcription_azure(audio_filepath)
        result_dict.append(transcription)
    return result_dict


# In[ ]:


#Converting all the video files in the folder to WAV
video_dir = r'E:\Jupyter_work'
os.listdir(video_dir)
Video_Audio_Converter(video_dir)


# In[ ]:


#get_large_audio_transcription('E:\Jupyter_work/Testfile3.wav')


# In[ ]:


#get_large_audio_transcription_google_enhanced('E:\Jupyter_work/Testfile1.wav')


# In[ ]:


#get_large_audio_transcription('E:\Jupyter_work/Testfile1.wav')


# In[ ]:


#get_large_audio_transcription_azure('E:\Jupyter_work/Testfile3.wav')


# In[10]:


result_google_regular_data = Batch_Audio_Speech_Google_Regular('E:\Jupyter_work')
#print(result_google_regular_data)


# In[11]:


result_azure_data = Batch_Audio_Speech_Azure('E:\Jupyter_work')
#print(result_azure_data)


# In[12]:


result_google_enhanced_data = Batch_Audio_Speech_Google_Enhanced('E:\Jupyter_work')
#print(result_google_enhanced_data)


# In[22]:


audio_filelist = [i for i in os.listdir('E:\Jupyter_work') if '.wav' in i]
transcripts = pd.DataFrame({
    'Filelist': audio_filelist,
    'Google regular Transcription': result_google_regular_data,
    'Google Enhanced Transcriptions': result_google_enhanced_data,
    'Azure Transcription ': result_azure_data,
})
transcripts.to_csv('transcripts.csv', index=False, encoding='utf-8-sig')

print("Program ended and all the transcripts are saved to transcripts.csv")