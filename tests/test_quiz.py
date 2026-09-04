import pytest

from src.interactive_us_state_capitals_quiz.quiz import (
    CapitalQuiz,
    Question,
    Quiz,
)


@pytest.fixture
def sample_question() -> Question:
    return Question(
        "What is the capital of California?",
        "Sacramento",
        {
            'A':"Phoenix",
            'B': "Sacramento",
            'C': "Denver",
            'D': "Austin"
        }
    )

@pytest.fixture
def sample_quiz() -> Quiz:
    return Quiz(1)

def test_set_user_answer_question(sample_question: Question) -> None:
    expected_result: str = 'B'

    sample_question.set_user_answer(expected_result)

    assert sample_question.user_answer == expected_result

def test_set_user_answer_question_error(sample_question: Question) -> None:
    with pytest.raises(ValueError,
        match=r"Invalid answer : F, The answer should be A, B, C, or D"):
            sample_question.set_user_answer('F')

def test_check_answer_question_correct(sample_question: Question) -> None:
    sample_question.set_user_answer('B')

    assert sample_question.check_answer()

def test_check_answer_question_incorrect(sample_question: Question) -> None:
    sample_question.set_user_answer('D')

    assert not sample_question.check_answer()

def test_calculate_score_quiz(sample_quiz: Quiz,
                            sample_question: Question) -> None:
    sample_question.set_user_answer('B')
    sample_quiz.questions = [sample_question]
    expected_score = 1

    sample_quiz.calculate_score()

    assert sample_quiz.score == expected_score

def test_get_score_in_percent_quiz(sample_quiz: Quiz,
                            sample_question: Question) -> None:
    sample_question.set_user_answer('B')
    sample_quiz.questions = [sample_question]
    expected_percent = 100

    sample_quiz.calculate_score()

    assert sample_quiz.get_score_in_percent() == expected_percent
