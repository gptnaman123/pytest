import pytest

@pytest.fixture(params=["a", "b"]) #a,b are the 2 parameters/arguments passed to fixture
def demo_fixture(request):         #object "request" is passed to access these parameters
    print(request.param)
    yield
    print("finish")

def test_login(demo_fixture):
    print("Login successful")

'''
Parameterizing the fixtures help in executing the test cases as many no. of times as the no. of 
parameters passed. For ex, in this case, there are 2 parameters passed, so test case is executed 
2 times.
'''

