
''' Testing emotion_detection module '''
import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    ''' emotion detection test cases '''
    def test_emotion_detector_regular(self):
        '''Connect to backend to see if request is set up correctly.'''
        response_json = emotion_detector("I am happy")
        self.assertNotEqual(response_json, None)
        self.assertTrue(isinstance(response_json, dict))

        self.assertTrue('dominant_emotion' in response_json)
        self.assertEqual(response_json['dominant_emotion'],'joy')

    def test_emotion_detector_empty(self):
        ''' Empty text parameter should return error entry.'''
        response_json = emotion_detector("")
        self.assertNotEqual(response_json, None)
        self.assertTrue(isinstance(response_json, dict))

        self.assertTrue('error' in response_json)
        self.assertEqual(response_json['error'], "Please enter text")

if __name__ == '__main__':
    unittest.main()
