''' emotion_detection module - provide emotion_detector method '''
import json
import logging
import requests

# python does not have real constants, this is just a naming convention...
# split up url to make pylint happy.
EMD_SERVER = 'https://sn-watson-emotion.labs.skills.network'
EMD_PATH = '/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
EMD_URL = EMD_SERVER + EMD_PATH
EMD_HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
EMD_ERROR_RESPONSE = {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
}
EMD_EMOTION_PREDICTIONS = 'emotionPredictions'
EMD_EMOTION = 'emotion'

DOMINANT = 'dominant_emotion'

LOG = logging.getLogger(__name__)

def emotion_detector(text_to_analyze):
    ''' Call backend for emotion prediction '''
    if (text_to_analyze is None or not isinstance(text_to_analyze, str)
        or len(text_to_analyze.strip()) == 0):
        return EMD_ERROR_RESPONSE
    request_body = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url=EMD_URL, headers=EMD_HEADERS, json=request_body, timeout=180)

    # This is for status codes 400 - 599
    if response.status_code >= 400:
        return EMD_ERROR_RESPONSE

    response_json = json.loads(response.text)

    LOG.debug(response_json)

    if EMD_EMOTION_PREDICTIONS not in response_json:
        return EMD_ERROR_RESPONSE

    #
    # Sample output:
    #
    # { 'emotionPredictions': [
    #    {
    #        'emotion': {
    #            'anger': 0.0043079085,
    #            'disgust': 0.00041127237,
    #            'fear': 0.0037504788,
    #            'joy': 0.9918804,
    #            'sadness': 0.014091322},
    #        'target': '',
    #        'emotionMentions': [
    #            {
    #                'span': {
    #                    'begin': 0,
    #                    'end': 10,
    #                    'text': 'I am happy'
    #                },
    #                'emotion': {
    #                    'anger': 0.0043079085,
    #                    'disgust': 0.00041127237,
    #                    'fear': 0.0037504788,
    #                    'joy': 0.9918804,
    #                    'sadness': 0.014091322
    #                }
    #            }
    #        ]
    #    }
    #   ],
    #   'producerId': {
    #       'name': 'Ensemble Aggregated Emotion Workflow',
    #       'version': '0.0.1'
    #   }
    # }
    #
    # for this service, all that is of interest are the entries in
    # result['emotionPredictions'][0]['emotion']
    #

    emotion_predictions = response_json[EMD_EMOTION_PREDICTIONS]

    LOG.debug(emotion_predictions)

    if not isinstance(emotion_predictions,list or len(emotion_predictions) == 0):
        return EMD_ERROR_RESPONSE

    LOG.debug(emotion_predictions[0])

    if EMD_EMOTION not in emotion_predictions[0]:
        return EMD_ERROR_RESPONSE

    emotions = response_json[EMD_EMOTION_PREDICTIONS][0][EMD_EMOTION]

    LOG.debug(emotions)

    # after checking for a sane structure, we can now extract the 'emotion' entries
    # adding the dominant emotion

    dominant = None
    highest_score = 0.0
    return_values = {}

    for name,score in emotions.items():
        return_values[name] = score
        if score > highest_score:
            highest_score = score
            dominant = name

    return_values[DOMINANT] = dominant
    return return_values
