from interactive_us_state_capitals_quiz.quiz import CapitalQuiz


def main() -> None:
    print("Hello from interactive-us-state-capitals-quiz!")
    qc = CapitalQuiz(5)
    qc.initialize()
    print(qc.questions[0].options)
