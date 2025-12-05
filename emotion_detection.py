''' emotion_detection module - provide emotion_detector method '''
import requests

# python does not have real constants, this is just a naming convention...
# split up url to make pylint happy.
EMD_SERVER = 'https://sn-watson-emotion.labs.skills.network'
EMD_PATH = '/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
EMD_URL = EMD_SERVER + EMD_PATH
EMD_HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
EMD_BLANK_RESPONSE = '{ "error": "Please enter text" }'
EMD_ERROR_RESPONSE = '{ "error": "Backend can\'t process input" }'

def emotion_detector(text_to_analyze):
    ''' Call backend for emotion prediction '''
    if (text_to_analyze is None or not isinstance(text_to_analyze, str)
        or len(text_to_analyze.strip()) == 0):
        return EMD_BLANK_RESPONSE
    request_body = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url=EMD_URL, headers=EMD_HEADERS, json=request_body, timeout=180)

    if response.status_code != 200:
        return EMD_ERROR_RESPONSE

    return response.text
