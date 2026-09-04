import click
import logging
import sys

from pathlib import Path
from interactive_us_state_capitals_quiz.quiz import CapitalQuiz




logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    stream=sys.stdout
)

logger = logging.getLogger(__name__)


def generate_output_file(quiz: CapitalQuiz) -> None:
    """Generate a detailed results file"""
    result_file = Path('quiz_results.txt')

    with result_file.open(mode='w', encoding='utf-8') as file:
        file.write("""
US State Capitals Quiz - Results
================================
        """
        )

        file.write("\n\n")

        file.write(f"Score: {quiz.score}/{quiz.number_of_question}\n")
        file.write(f"Percent: {int(quiz.get_score_in_percent())}%\n")

        file.write("\n\n")

        for index, question in enumerate(quiz.questions):
            file.write(f"Question {index + 1}\n")
            file.write("\n")
            file.write(f"{question.text}\n")

            file.write(f"Your answer: {question.options[question.user_answer]}\n")
            file.write(f"Correct answer: {question.answer}\n")
            file.write(f"Result: {'Correct' if question.check_answer() else 'Incorrect'}\n")
            file.write("----------------------------------------------------------------")
            file.write("\n\n")




@click.command()
@click.argument("n", type=int)
def create_quiz(n: int) -> None:
    

    logger.info(f"Create a us state capitals quiz with {n} questions")
    quiz = CapitalQuiz(n)

    logger.info("Initialize the question...")
    quiz.initialize()

    logger.info("Quiz start...")

    click.echo("""
==================================================================
                    US State Capitals Quiz
==================================================================
    """)

    for index, question in enumerate(quiz.questions):
        click.echo(f"Question {index + 1}/{quiz.number_of_question}")

        click.echo(f"{question.text}")

        for letter, option in question.options.items():
            click.echo(f"{letter}. {option}")

        user_answer = input("Your answer: ")

        try:
            question.set_user_answer(user_answer)
        except ValueError as e:
            logger.debug(f"Error : {e}")
            raise

    click.echo(
        """
==================================================================
                            RESULTS
==================================================================
        """
    )

    quiz.calculate_score()

    click.echo(f"Score: {quiz.score}/{quiz.number_of_question}")
    click.echo(f"Percent: {int(quiz.get_score_in_percent())}%")

    logger.info("Generate a detailed results file")
    generate_output_file(quiz)

def main() -> None:
    create_quiz()
