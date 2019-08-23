# -*- coding: utf-8 -*-
"""
    tests.my_test
"""
import os
import pkgutil
import sys
import textwrap

import pytest

import formula

def test_magic_number():
    assert formula.magicNumber() == 42