
''' Testing emotion_detection module '''
import json
import unittest
from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    ''' emotion detection test cases '''
    def test_emotion_detector_regular(self):
        '''Connect to backend to see if request is set up correctly.'''
        text = emotion_detector("I am happy")
        self.assertNotEqual(text,None)
        self.assertTrue(isinstance(text,str))
        response_json = json.loads(text)

        self.assertTrue('emotionPredictions' in response_json)

    def test_emotion_detector_empty(self):
        ''' Empty text parameter should return error entry.'''
        text = emotion_detector("")
        self.assertNotEqual(text,None)
        self.assertTrue(isinstance(text,str))
        response_json = json.loads(text)

        self.assertTrue('error' in response_json)
        self.assertEqual(response_json['error'], "Please enter text")

if __name__ == '__main__':
    unittest.main()
