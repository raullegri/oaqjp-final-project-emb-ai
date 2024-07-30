import requests
import json

def emotion_detector(text_to_analyze):

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    myobj = { "raw_document": { "text": text_to_analyze } }

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json = myobj, headers = header)

    json_response = json.loads(response.text)

    if response.status_code == 200:

        scores = {
            'anger': json_response['emotionPredictions'][0]['emotion']['anger'],
            'disgust': json_response['emotionPredictions'][0]['emotion']['disgust'],
           'fear': json_response['emotionPredictions'][0]['emotion']['fear'],
            'joy': json_response['emotionPredictions'][0]['emotion']['joy'],
            'sadness': json_response['emotionPredictions'][0]['emotion']['sadness']
        }

        dominant_emotion = max(scores, key=scores.get)

        result = {
        **scores,
        'dominant_emotion': dominant_emotion
        }
    
    elif response.status_code == 400:

        result = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    return result


