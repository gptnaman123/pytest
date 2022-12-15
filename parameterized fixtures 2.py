import pytest

person_lst = ['person1', 'person2', 'person3', 'person4', 'person5']
@pytest.fixture(params=[i for i in person_lst], scope='function')
def demo_fixture(request):
    print(request.param)
    yield
    print("Logout Successful")

def test_login(demo_fixture):
    print("Login successful")
