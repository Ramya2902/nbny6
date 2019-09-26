import pytest
import test_course

def test_courseid():
    cou=test_course.test_course()
    assert cou==7050
    assert cou==4250
    cou2=test_course.test_course()
    assert cou2==10109



