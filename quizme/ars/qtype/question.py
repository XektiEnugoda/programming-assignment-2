"""Module for the base Question class in the Adaptive Review System."""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, Optional
import uuid


class Question(ABC):
    """Abstract base class for quiz questions in the Adaptive Review System."""
    def __init__(self, question: str, answer: Any):
        """
        Initialize a new Question instance.

        Args:
        question (str): The text of the question.
        answer (object): The correct answer to the question.
        """
        self._id = uuid.uuid4()

        self._question = question

        self._answer = answer

        self._last_asked = datetime.min
    

    @property
    def id(self) -> uuid.UUID:
        """Get the unique identifier of the question."""
        return self._id


    @property
    def question(self) -> str:

        return self._question
    

    @property
    def answer(self) -> Any:

        return self._answer
    

    @property
    def last_asked(self) -> datetime:
        """Get the timestamp of when the question was last asked."""
        return self._last_asked

    
    def ask(self) -> str:
        """
        Return the question as a string and update the last asked time.

        Returns:
            str: The text of the question.
        """
        _last_asked = datetime.now()
        return self._question

    @abstractmethod
    def check_answer(self, answer: Any) -> bool:
        """
        Check if the provided answer is correct.

        Args:
            answer (object): The answer to check.

        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        if (self.answer != answer):
            return False
        else:
            return True
    
    @abstractmethod
    def incorrect_feedback(self) -> str:
        """
        Return feedback for an incorrect answer.

        Returns:
            str: Feedback message for an incorrect answer.
        """
        if check_answer(self, answer) == False:
            return "Incorrect Answer!"

    
    def reset(self):

        reset 

    def __eq__(self, other: object) -> bool:
        """
        Define equality based on the question's unique id.

        Args:
            other (object): The object to compare with.

        Returns:
            bool: True if the other object is a Question with the same id, False otherwise.
        """
        if not isinstance(other, Question):
            return False
        return self.id == other.id

    def __hash__(self) -> int:
        """
        Define a hash value based on the question's unique id.

        Returns:
            int: Hash value of the question's unique id.
        """

        return hash(self._id)
    
    def __repr__(self) -> str:
        return str(_question)
