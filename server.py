''' Flask server app '''
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask('Emotion Detector')

@app.get('/emotionDetector')
def fetch_backend_result():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using the emotion_detector())
        function. The output returned lists the emotion scores and the 
        dominant emotion for the given text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    # well, of course I do not send the request if the text is missing...
    if text_to_analyze is None or len(text_to_analyze.strip()) == 0:
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyze)

    dominant = result.get('dominant_emotion','./.')

    if dominant is None:
        return 'Invalid text! Please try again!'

    anger = result.get('anger','./.')
    disgust = result.get('disgust','./.')
    fear = result.get('fear','./.')
    joy = result.get('joy','./.')
    sadness = result.get('sadness','./.')

    return f"""
    For the given statement, the system response is 
    'anger': {anger}, 
    'disgust': {disgust}, 
    'fear': {fear}, 
    'joy': {joy} and 
    'sadness': {sadness}. 
    The dominant emotion is {dominant}.
    """

@app.get('/')
def index():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
