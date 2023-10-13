#Testing Your Code
#file name_function.py
def get_formated_name(first, last):
    full_name = first + ' ' + last
    return full_name.title()

#file names.py
from name_function import get_formated_name

print("Enter q at any point to quit: ")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("\nGive me a last name: ")
    if last == 'q':
        break
    formated_name = get_formated_name(first, last)
    print("Neatly formated name: " + formated_name +".")

#file test_names_function.py
import unittest
from name_function import get_formated_name

class NamesTestCase(unittest.TestCase):
    def test_names(self):
        formated_name = get_formated_name("Janis", "Joplin")
        self.assertEqual(formated_name, "Janis Joplin") #verifies that the output is correct, returns an error otherwise

    #other test cases can be made
    def test_middle_name(self):
        formated_name = get_formated_name("Aubrey", "Drake", "Graham")
        self.assertEqual(formated_name, "Aubrey Drake Graham")

unittest.main() #will run both tests

#The different assert methods
assertEqual(a,b) #checks if a==b
assertNotEqual(a,b) #checks if a != b
assertTrue(x) #checks if x is true
assertFalse(x) #checks if x is false
assertIn(item, list) #verify that item is in list
assertNotIn(item, list) #verify that item is not in list

#the setUp() method

import unittest
from survey import AnonymousSurvey

class TestAnoymousSurvey(unittest.TestCase):
    def setUp(self):
        question = input("What language did you first learn to speak: ")
        self.my_survey = AnonymousSurvey(question)
        self.responses = ["English", "Spanish", "Mandarin"]

    def test_score_single_response(self):
        self.my_survey.store_response(self.reponses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_responses(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.response)

