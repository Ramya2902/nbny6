import pytest
import test_pass
from test_pass import Studentid, existing

def test_student():
    if existing in Studentid:
        exists=1
    else:
        exists=0
        assert exists==1
length = len(str(existing))
assert length == 5
