#!/usr/bin/env python

# coding: utf-8

# In[8]:


import boto3
import time
import urllib
import json

# In[9]:


transcribe_client = boto3.client('transcribe',
                                 aws_access_key_id='AKIASIOCBXZYGMIOP24P',
                                 aws_secret_access_key='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',
                                 region_name="us-east-2")


# In[10]:


def transcribe_file(job_name, file_uri, transcribe_client):
    transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': file_uri},
        MediaFormat='wav',
        LanguageCode='en-US'
    )

    max_tries = 60
    while max_tries > 0:
        max_tries -= 1
        job = transcribe_client.get_transcription_job(TranscriptionJobName=job_name)
        job_status = job['TranscriptionJob']['TranscriptionJobStatus']
        if job_status in ['COMPLETED', 'FAILED']:
            print(f"Job {job_name} is {job_status}.")
            if job_status == 'COMPLETED':
                response = urllib.request.urlopen(job['TranscriptionJob']['Transcript']['TranscriptFileUri'])
                data = json.loads(response.read())
                text = data['results']['transcripts'][0]['transcript']
                print("========== below is output of speech-to-text ========================")
                print(text)
                print("=====================================================================")
            break
        else:
            print(f"Waiting for {job_name}. Current status is {job_status}.")
        time.sleep(10)


def check_job_name(job_name):
    job_verification = True
    # all the transcriptions
    existed_jobs = transcribe_client.list_transcription_jobs()
    for job in existed_jobs['TranscriptionJobSummaries']:
        if job_name == job['TranscriptionJobName']:
            job_verification = False
            break
        if job_verification == False:
            command = input(job_name + " has existed. \nDo you want to override the existed job (Y/N): ")
            if command.lower() == "y" or command.lower() == "yes":
                transcribe_client.delete_transcription_job(TranscriptionJobName=job_name)
            elif command.lower() == "n" or command.lower() == "no":
                job_name = input("Insert new job name? ")
                check_job_name(job_name)
            else:
                print("Input can only be (Y/N)")
                command = input(job_name + " has existed. \nDo you want to override the existed job (Y/N): ")
    return job_name


# In[11]:


def main():
    file_uri = 's3://recordedwavfile/Kevin25.wav'
    transcribe_file('Kevin25-job', file_uri, transcribe_client)


# In[12]:


if __name__ == '__main__':
    main()

# In[ ]:


# In[ ]:
