# -*- coding: utf-8 -*-
# @author: Kennnycyq
# @time: 2020/11/16 9:58 PM


import pytest

from pytest01 import calculator


@pytest.fixture(autouse=True)
def init_cal():
     yield calculator.Calculator()
