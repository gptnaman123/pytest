#Fixtues are functions which are executed when they are passed to a test case which needs to be executed

import pytest

@pytest.fixture(scope="module")   #scope: tells us how often we want to invoke fixture(default= "function")
def connect_db():
    print("I need to connect to employee database")
    yield    #yield executes all test cases
    print("I need to disconnect from employee database")

def test_first(connect_db):
    print("I am first test to verify employee name against id")

def test_second(connect_db):
    print("I am second test to verify employee id against dept.")

def test_third(connect_db):
    print("I am third test to verify employee name against supervisor")

def test_fourth():  #Fixture not passed to test case, so fixture not executed, test case executes only
    print("I do not need db connection")