import pytest
import string
from count_punct_marks import count_punct_marks


def test_empty_string():
   assert count_punct_marks("") == 0


def test_no_punctuation():
    assert count_punct_marks("Hello World") == 0


def test_single_punctuation():
    assert count_punct_marks("Hello World!") == 1


def test_multiple_punctuation():
    assert count_punct_marks("Hello, World! How are you?") == 3


def test_edge_case():
    assert count_punct_marks("!!!") == 3


def test_all_punctuation():
    assert count_punct_marks(".,:;!?") == 6
