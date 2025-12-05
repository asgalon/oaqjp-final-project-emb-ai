
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

    def test_project_test_cases(self):
        ''' Task 5 test cases.
            We are testing the correctness of the backend here, which is reduntant
            because what is to be tested is the correctness of ou, code, not theirs.
            just add them all. The test cases above I already did in step 2 to test
            the correctness of the code right from the start. With test-driven development,
            the tests are written first so they can already be used while developing the code.
        '''
        self.emotion_detector_invocation('I am glad this happened', 'joy')
        self.emotion_detector_invocation('I am really mad about this', 'anger')
        self.emotion_detector_invocation('I feel disgusted just hearing about this', 'disgust')
        self.emotion_detector_invocation('I am so sad about this', 'sadness')
        self.emotion_detector_invocation('I am really afraid that this will happen', 'fear')

    def emotion_detector_invocation(self, text, expected_dominant):
        '''Connect to backend to see if request is set up correctly.'''
        response_json = emotion_detector(text)
        self.assertNotEqual(response_json, None)
        self.assertTrue(isinstance(response_json, dict))

        self.assertTrue('dominant_emotion' in response_json)
        self.assertEqual(response_json['dominant_emotion'],expected_dominant)


if __name__ == '__main__':
    unittest.main()
