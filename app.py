import speech_recognition as sr
import os
import openai
import pyttsx3
from flask import  Flask , request, jsonify
import pymongo

app = Flask(__name__)
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[0].id)

@app.route('/text', methods=['GET', 'POST'])
def text():
    print('working here')

    if (request.method == 'GET'):
        #query = request.json['query']
        query = 'i wnat ot kill my self'
        print(query)
        os.environ['OPENAI_API_KEY'] = #API le liyo
        openai.api_key = os.getenv("OPENAI_API_KEY")
        prompt="act as a therapist and talk naturally to the query : hi /n mentalse: Hi menatalse this side how are you query:" + query + '\n mentalse:'
        response = openai.Completion.create(
            model="davinci:ft-personal-2023-03-30-06-00-49",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        print(response)

        res = response['choices'][0]['text']
        res = res.split('\n')[0]
        res = res.split('query:')[0]
        prompt=prompt+res
        print(res)
        # return render_html('workin')
        return jsonify(res)



if __name__=='__main__':
    app.run()