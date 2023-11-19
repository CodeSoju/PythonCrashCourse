'''
Testing proves that your code works as it's supposed to in response to all the input types 
it's designed to receive. When you write tests, you can be confident that your code will work
correctly as more peolpe begin to use your programs. 
Every programmer makes mistakes, so every programmer must test their code often, catching 
problems bfore users encounter them. 

Test your code using tools in Python's unittest module. 

TESTING A FUNCTION:
--------------------
look at name_function.py


UNIT TESTS AND TEST CASES:
-----------------------
The module unittest from the Python standard library provides tools for testing your code. 
A unit test verfies that one specific aspect of a function's behavior is correct. 
A test case is a collection of unit tests that together prove that a function behaves 
as expected, within the full range of situations you expect it to handle. 

A good test case considers all the possible kinds of input a function could recieve and includes 
tests to represent each of these situations. A test case with full converge includes a full range
of unit tests covering all the possible ways  you can use a function. 
It's often good enough to write tests for your code's critical behaviors and then aim for full 
coverage only if the project starts to see widespread use. 


PASSING TEST:
-----------
To write a test case for a function, import the unittest module and the function you 
want to test. Then create a class that inherits from unittest.TestCase, and write 
a series of methods to test different aspects of your function's behavior. 

See test_name_function.py

First, we import unittest and the function we want to test, get_formatted_name().
At (1) we create a class called NamesTestCase, which will contain a series of unit tests for 
get_formatted_name(). You can name the class anything you want, but it's best to call it something
related to the function you're about to test and to use the word Test in the class name. 
This class must inherit from the class unittest.TestCase so Python knows how to run the tests
you write. 

NameTestCase contains a single method that tests one aspect of get_formatted_name(). 
We call this method test_first_last_name(). 
Any method that starts with test_ will run automatically when we run test_name_function.py
Within this test method, we call the function we want to test

Assert methods verify that a result you received matches the result you expected to receive. 
In this case, because we know get_formatted_name() is supposed to return a capitalized, 
properly spacced full name, we expect the value of formatted name to be Janis Joplin. 
To check if this is true, we use unittest's asserEqual() method and pass it 
formatted_name and 'Janis Joplin' . The line 

self.assertEqual(formatted_name, 'Janis Joplin')

says "Compare the value in formatted_name to the string 'Janis Joplin'. If they are equal 
as expected, fine. But if they don't match, let me know!"

It's important to know that many testing frameworks import your test fies before running them. 
When a file is imported, the interpreter executes the file as it's being imported. The if block 
at (4) looks at a special variable, __name__, which is set when the program is executed.
If this file is being run as the main program, the value of __name__ is set to '__main__'. 
In this case, we call unittest.main(), which rus the test case. When a testing framework import 
this file, the value of __name__ won't be '__main__' and this block will not be executed. 

A Failing Test:
----------------
See the change in the file

Responding to a Failed Test:
--------------------------
What do you do when a test fails? Assuming you're checking the right conditions, 
a passing test means the function is behaving correctly and a failing test means there's an error in the new code 
you wrote. So when a test fails, don't change the test. Instead, fix the code that caused the 
test to fail. Examine the changes you just made to the function, annd figure out how those changes 
broke the desired behavior. 


Adding New Tests:
----------------
Now that we know get_formatted_name() works for simple names again, let's wirte a second test 
for people who include a middle name. We do this by adding another method to the class NamesTestCase


Testing a Class:
----------------

A variety of Assert Methods:
----------------------------
Python provides a number of assert methods in the unittest.TestCase class. 

assertEqual(a, b) ---> Verify that a == b
assertNotEqual(a. b) ---> Verify that a != b
assertTrue(x)   ---> Verify that x is True
assertFalse(x)    ----> Verify that x is False
assertIn(item, list)    ----> Verify that item is in list
assertNotIn(item, list) ----> Verify that item is not in list


Implementing such changes would risk affecting the current behavior of the class
AnonymousSurvey. For example, it's possible that while trying to allow each user to enter 
multiple responses, we could accidentally change how single responses are handled. To 
ensure we don't break existing behavior as we develop this module, we can write tests for the class. 

Let's wrtie a test to verify that a single response to the survey question is stored properly. 
We'll use the assertIn() method to verify that the response is in the list of responses after it's 
been stored:


The setUp() Method:
-----------------
In test_survey.py we created a new instance of AnonymousSurvey is each test method, and we 
created new responses in each method. The unittest.TestCase class has a s setUp() method that
allows you to create these objects once and then use them in each of your test methods. 

When you include setUp() method in a TestCase class, Python runs the setUp() method before running 
each method starting with test_. Any objects created in the setUp() method are then available in 
each test method you write. 

The method setUp() does two things: it creates a survey instance (1), and it creates a list 
of responses (2). Each of these is prefixed by self, so they can be used anywhere in the class. 
This makes the two test methods simpler, because neither one has to make a survey instance or a response. 

The method test_score_single_response() verifies that the first response in 
self.responses -- self.responses[0] -- can be stored correctly, and test_store _three_responses() 
verfies that all three responses in self.responses can be stored correctly. 

When we run test_survey.py again, both tests still pass. These tests would be 
particularly useful when trying to expand AnonymousSurvey to handle multiple responses 
for each person. After modifying the code to accept multiple responses, you could run these tests 
and ake sure you haven't affected the ability to store asingle response or a series of 
individual responses. 

When you're testing your own classes, the setUp() method can make your test methods easier 
to write. You make one set of instances and attributes in setUp() and then use these instances 
and attributes in each test method. 
'''