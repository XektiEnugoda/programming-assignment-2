"""Module for the base Question class in the Adaptive Review System."""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, optional
import uuid


class Question(ABC):
    def __init(self, id, question, answer, last_asked):
        self._id = uuid.UUID4
        self._question = _question
        self._answer = _answer
        self._last_asked = datetime.now()
    
    @property
    
    def id()