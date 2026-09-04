# Interactive US State Capitals Quiz

A Python command-line application that generates a randomized US state capitals quiz, lets the user answer each question interactively, calculates the final score, and saves a detailed report of the results to a text file.

This project is a personalized version of **Project 4: Generate Random Quiz Files** from *Automate the Boring Stuff with Python* by Al Sweigart.

## 📌 Project Overview

The original project focuses on automatically generating multiple quiz files with randomized questions and answer choices.

For this version, I redesigned the project as an **interactive command-line quiz application** using **Click**.

The number of questions is provided as a command-line argument. The application then randomly generates the quiz, presents the questions in the terminal, validates the user's answers, calculates the final score, and generates a detailed results file.

The program:

1. Accepts the number of questions as a command-line argument.
2. Randomly selects the requested number of states.
3. Generates four possible answers for each question.
4. Randomizes the order of the answer choices.
5. Lets the user answer each question.
6. Validates the user's answer.
7. Checks each answer against the correct capital.
8. Calculates the final score.
9. Displays the score and percentage in the terminal.
10. Generates a detailed `quiz_results.txt` file.

The goal is to transform a simple automation exercise into a small, reusable command-line application while practicing good Python development practices.

## ✨ Features

* Interactive command-line interface.
* Uses **Click** for command-line argument handling.
* User specifies the number of questions.
* Randomly selects questions.
* Randomizes multiple-choice answers.
* Provides one correct answer and three incorrect answers.
* Accepts answers using `A`, `B`, `C`, or `D`.
* Validates user input.
* Calculates the final score.
* Displays the score and percentage in the terminal.
* Generates a detailed results file.
* Shows the user's answer alongside the correct answer.
* Uses Python's standard library for most functionality.
* Includes automated tests.
* Uses static type checking with Mypy.
* Uses Ruff for linting and formatting.
* Uses `uv` for project and dependency management.
* Uses Python logging for application diagnostics.

## 🛠️ Technologies and Tools

### Language

* **Python 3**

### Libraries

* **Click** — command-line interface

### Development Tools

* **uv** — Python project and dependency management
* **Ruff** — linting and code formatting
* **Mypy** — static type checking
* **Pytest** — automated testing

## 📂 Project Structure

```text
interactive-state-capitals-quiz/
│
├── src/
│   └── interactive_us_state_capitals_quiz/
│       ├── __init__.py
│       ├── data.py
│       └── quiz.py
│
├── tests/
│   ├── __init__.py
│   └── test_quiz.py
│
├── .gitignore
├── README.md
├── pyproject.toml
├── uv.lock
└── ...
```

## ▶️ How the Program Works

### 1. Provide the Number of Questions

The number of questions is provided as a command-line argument.

For example:

```bash
uv run interactive-us-state-capitals-quiz 5
```

The `5` tells the application to generate a quiz containing five questions.

The CLI argument is defined using Click:

```python
@click.command()
@click.argument("n", type=int, help="number of question")
def create_quiz(n: int) -> None:
    ...
```

### 2. Generate the Quiz

The application creates a `CapitalQuiz` instance using the requested number of questions:

```python
quiz = CapitalQuiz(n)
```

The quiz is then initialized:

```python
quiz.initialize()
```

The quiz randomly selects states and creates the corresponding multiple-choice questions.

For each question, the program generates:

* One correct capital.
* Three incorrect capitals.
* Four answer choices in total.

The answer choices are randomized so that the correct answer does not always appear in the same position.

### 3. Answer the Questions

The questions and available options are displayed directly in the terminal.

Example:

```text
==================================================================
                    US State Capitals Quiz
==================================================================

Question 1/5

What is the capital of California?

A. Phoenix
B. Sacramento
C. Denver
D. Austin

Your answer: B
```

The user's answer is passed to the question object:

```python
question.set_user_answer(user_answer)
```

If the answer is invalid, a `ValueError` is raised.

### 4. Calculate the Score

After all questions have been answered, the application calculates the final score:

```python
quiz.calculate_score()
```

The score and percentage are then displayed in the terminal.

Example:

```text
==================================================================
                            RESULTS
==================================================================

Score: 4/5
Percent: 80%
```

### 5. Generate the Results File

After calculating the score, the application generates a detailed results file:

```text
quiz_results.txt
```

The file is created in the **current working directory** where the command is executed.

The report contains:

* Final score.
* Percentage.
* Each question.
* User's answer.
* Correct answer.
* Result of each question.

Example:

```text
US State Capitals Quiz - Results
================================

Score: 4/5
Percent: 80%

Question 1

What is the capital of California?

Your answer: Sacramento
Correct answer: Sacramento
Result: Correct

----------------------------------------------------------------
```

This provides a permanent record of the completed quiz.

## 🎲 Randomization

Randomization is an important part of the project.

The quiz logic randomly:

* Selects states.
* Selects incorrect answers.
* Arranges the available answer choices.

This means that different quiz sessions can produce different questions and different answer positions.

The randomization is handled by the quiz implementation in the `CapitalQuiz` class.

## 🧠 Data Structure

The state capitals are stored in a Python dictionary.

```python
capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    # ...
}
```

The **state** is used to generate the question, while the corresponding **capital** is used as the correct answer.

The dictionary also provides the data needed to generate incorrect answers.

## 📝 Command-Line Interface

The application uses **Click** to define its command-line interface.

The command accepts one positional argument:

```text
N
```

where `N` represents the number of questions.

For example:

```bash
uv run interactive-us-state-capitals-quiz 10
```

generates a quiz containing ten questions.

### Example CLI Usage

```bash
$ uv run state-capitals 5

==================================================================
                    US State Capitals Quiz
==================================================================

Question 1/5

What is the capital of Texas?

A. Austin
B. Phoenix
C. Denver
D. Atlanta

Your answer: A
```

The application continues until all requested questions have been answered.

## 📄 Results

Each completed quiz generates:

```text
quiz_results.txt
```

The file contains:

```text
US State Capitals Quiz - Results
================================

Score: 4/5
Percent: 80%

Question 1

What is the capital of Texas?

Your answer: Austin
Correct answer: Austin
Result: Correct
```

The results file is overwritten each time a new quiz is completed.

## 📋 Logging

The application uses Python's built-in `logging` module.

Logging is configured to display messages in the terminal:

```python
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    stream=sys.stdout
)
```

The application logs important events such as:

* Quiz creation.
* Quiz initialization.
* Quiz start.
* Results file generation.
* Invalid answer errors.

This provides useful diagnostic information while running the application.

## 🚀 Getting Started

### Prerequisites

This project uses [`uv`](https://docs.astral.sh/uv/) for Python project and dependency management.

Python 3 is required.

Check your Python version:

```bash
python --version
```

Check that `uv` is installed:

```bash
uv --version
```

### Clone the Repository

```bash
git clone <repository-url>
cd interactive-state-capitals-quiz
```

### Install the Project

Install the project and its dependencies using:

```bash
uv sync
```

`uv sync` creates the virtual environment if necessary and installs the project dependencies.

## ▶️ Running the Quiz

If the project defines the following command-line entry point in `pyproject.toml`:

```toml
[project.scripts]
state-capitals = "interactive_us_state_capitals_quiz.main:main"
```

the application can be executed with:

```bash
uv run interactive-us-state-capitals-quiz 5
```

Replace `5` with the desired number of questions.

For example:

```bash
uv run interactive-us-state-capitals-quiz 10
```

generates a ten-question quiz.

### Alternative

The application can also be executed through the Python module if the package exposes the appropriate module entry point:

```bash
uv run python -m interactive_us_state_capitals_quiz.main 5
```

Using a package entry point such as:

```bash
uv run interactive-us-state-capitals-quiz 5
```

is preferred for a command-line application because users do not need to know where the source files are located.

## 🧪 Testing

The project uses **Pytest** for automated testing.

Run the complete test suite:

```bash
uv run pytest
```

## 🔍 Code Quality

### Ruff

Ruff is used for linting and formatting.

Check the code for linting issues:

```bash
uv run ruff check .
```

Automatically fix supported linting issues:

```bash
uv run ruff check . --fix
```

Format the project:

```bash
uv run ruff format .
```

Check formatting without modifying files:

```bash
uv run ruff format . --check
```

### Mypy

Mypy is used for static type checking.

Run Mypy:

```bash
uv run mypy .
```

The project uses type annotations to improve code reliability and maintainability.

## 🛠️ Development Workflow

Before committing changes, run the project's quality checks:

```bash
uv run ruff format .
uv run ruff check .
uv run mypy .
uv run pytest
```

These checks help ensure that the project is:

* Properly formatted.
* Free from common linting issues.
* Statically type-checked.
* Checked for common security vulnerabilities.
* Covered by automated tests.

## 🔄 Original Project vs. My Version

| Original Project                 | Interactive Version                                                     |
| -------------------------------- | ----------------------------------------------------------------------- |
| Generates 35 quizzes             | Generates one quiz per session                                          |
| Fixed number of questions        | User specifies the number of questions                                  |
| Generates quiz text files        | User interacts with the quiz in the terminal                            |
| Generates answer keys            | Calculates the score automatically                                      |
| No user interaction              | Interactive user input                                                  |
| Quiz and answer key are separate | Generates a detailed results file                                       |
| Primarily designed for a teacher | Designed as a reusable CLI application                                  |
| Basic Python automation          | Uses Click, testing, typing, linting, formatting, and security analysis |

## 🎯 Learning Objectives

This project provides practice with several important Python concepts:

* Working with dictionaries.
* Working with lists.
* Writing reusable classes and functions.
* Using loops.
* Generating random data.
* Shuffling collections.
* Handling user input.
* Validating user input.
* Raising and handling exceptions.
* Reading and writing text files.
* Managing application state.
* Separating application logic into modules.
* Building command-line applications with Click.
* Using Python logging.
* Writing automated tests.
* Adding type annotations.
* Running static type checking.
* Applying linting and formatting.
* Performing basic security analysis.
* Managing a Python project with `uv`.
* Creating a Python package and command-line entry point.

## 💡 Future Improvements

Possible improvements for future versions include:

* Validate that the requested number of questions is within the available number of states.
* Add different categories of questions.
* Add difficulty levels.
* Allow the user to restart the quiz.
* Add a timer.
* Store previous scores.
* Add a high-score system.
* Support multiple quiz attempts.
* Add colored terminal output.
* Improve the Click CLI with additional options.
* Add command-line options such as `--output`.
* Export results to CSV or JSON.
* Add more geographic data.
* Improve the CLI interface.

## 📚 Reference

Inspired by:

*Automate the Boring Stuff with Python*
by Al Sweigart.

Original exercise:

**Project 4: Generate Random Quiz Files**

This implementation modifies the original exercise to create an interactive command-line quiz rather than generating a fixed collection of quiz and answer-key files.

The project also extends the original exercise with:

* Command-line arguments.
* Interactive user input.
* Answer validation.
* Score calculation.
* Result generation.
* Python logging.
* Automated testing.
* Static type checking.
* Linting.
* Formatting.
* Security analysis.
* Python package management with `uv`.
