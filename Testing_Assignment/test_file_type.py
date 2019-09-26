import pytest
import type_pass

def test_type_pass():
    FilesType = "pdf"
    assert type_pass.file_type() == FilesType
