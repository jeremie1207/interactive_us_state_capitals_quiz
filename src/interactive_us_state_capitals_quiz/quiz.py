import random

from interactive_us_state_capitals_quiz.data import capitals


class Question:
    def __init__(
        self, text: str, answer: str, options: dict[str, str]
    ) -> None:
        self.text = text
        self.answer = answer
        self.options = options
        self.user_answer: str = ""

    def set_user_answer(self, answer: str) -> None:
        """set an answer to the question

        Args:
            answer (str): A, B, C, or D

        Raises:
            ValueError: raise an error when the user provide an invalid answer
        """
        if answer not in {"A", "B", "C", "D"}:
            raise ValueError(
                f"Invalid answer : {answer}, The answer should be A, B, C, or D"
            )
        self.user_answer = answer

    def check_answer(self) -> bool:
        """Check if answer is correct

        Args:
            answer (str): answer

        Returns:
            bool: True if answer is correct otherwise False
        """
        return self.options[self.user_answer] == self.answer


class Quiz:
    def __init__(self, number_of_question: int) -> None:
        self.number_of_question = number_of_question
        self.questions: list[Question] = []
        self.score = 0

    def calculate_score(self) -> None:
        """Calculate quiz score"""
        self.score = 0
        for question in self.questions:
            if question.check_answer():
                self.score += 1

    def get_score_in_percent(self) -> float:
        """Return score in percent"""
        return (self.score / self.number_of_question) * 100


class CapitalQuiz(Quiz):
    def __init__(self, number_of_question: int) -> None:
        if not 1 <= number_of_question <= 50:
            raise ValueError(
            "Invalid input: the number of questions should be between 1 and 50"
            )
        super().__init__(number_of_question)

    def initialize(self) -> None:
        selected_state = random.sample(
            list(capitals.keys()), self.number_of_question
        )
        for state in selected_state:
            text: str = f"What is the capital of {state}?"
            answer: str = capitals[state]

            filtered_capital = [
                cap for cap in list(capitals.values()) if cap != capitals
            ]

            options_list = random.sample(filtered_capital, 3)
            options_list.append(answer)
            random.shuffle(options_list)

            options: dict[str, str] = {
                "A": options_list[0],
                "B": options_list[1],
                "C": options_list[2],
                "D": options_list[3],
            }

            question = Question(text, answer, options)
            self.questions.append(question)

        random.shuffle(self.questions)
