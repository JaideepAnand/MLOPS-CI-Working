import pytest

#Function to return square 
def square(n):
    return n**2

#Function to return cube
def cube(n):
    return n**3

#Function to return fifth power
def fifth_power(n):
    return n**5

def test_square():
    assert square(2) == 4 , "Test failed: square(2) should be 4" 
    assert square(3) == 9 , "Test failed: square(3) should be 9"

def test_cube():
    assert cube(2) == 8 , "Test failed: cube(2) should be 8"
    assert cube(3) ==27 , "Test failed: cube(3) should be 27"

def test_fifth_power():
    assert fifth_power(2) == 32 , "Test failed: fifth_power(2) should be 32"
    assert fifth_power(3) == 243,"Test failed: fifth_power(3) should be 243"

#Test for valid input
def test_valid_input():
    with pytest.raises(TypeError):
        square('string')
