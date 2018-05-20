# -*- coding: utf-8 -*-
import pytest
from passwdgen import PasswordGenerator

@pytest.fixture
def passwd_gen():
    return PasswordGenerator()

def test_generate(passwd_gen):
    actual = passwd_gen.generate()
    expected = None
    assert actual == expected

def test_validate(passwd_gen):
    actual = passwd_gen.validate()
    expected = False
    assert actual == expected
