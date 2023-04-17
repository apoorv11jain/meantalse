import speech_recognition as sr
import os
import openai
import pyttsx3

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[0].id)

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    r.pause_threshold = 1
    audio = r.listen(source)
os.environ['OPENAI_API_KEY'] = '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'
query = r.recognize_google(audio, language='en-in')
print(query)
openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.Completion.create(
  model="davinci:ft-personal-2023-03-30-06-00-49",
  prompt="act as a therapist and talk naturally to the query : hi i am apoorv jain /n mentalse: Hi apoorv menatalse this side how are you query:"+query+'\n mentalse:',
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
res = response['choices'][0]['text']
res=res.split('\n')[0]
res =res.split('query:')[0]
print(res)
engine.say(res)
engine.runAndWait()