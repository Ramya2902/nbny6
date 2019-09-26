import pytest
import test_fail

def test_type_pass():
    FilesType = "pdf"
    assert test_fail.file_type() == FilesType
