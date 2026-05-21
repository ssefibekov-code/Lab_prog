#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Тесты для задания 07_secret.py"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from tasks import task07_secret as task


def test_message_length():
    """Проверка, что расшифрованное сообщение состоит из 5 слов."""
    task.run()
    words = task.decoded_message.split()
    assert len(words) == 5


def test_first_word():
    """Проверка первого слова (4-я буква)."""
    task.run()
    assert task.word1 == task.secret_message[0][3]