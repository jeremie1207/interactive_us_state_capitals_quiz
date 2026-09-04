# Interactive US State Capitals Quiz

A Python command-line application that generates a randomized US state capitals quiz, lets the user answer each question interactively, calculates the final score, and saves a detailed report of the results to a text file.

This project is a personalized version of **Project 4: Generate Random Quiz Files** from _Automate the Boring Stuff with Python_ by Al Sweigart.

## 📌 Project Overview

The original project focuses on automatically generating multiple quiz files with randomized questions and answer choices.

For this version, I redesigned the project as an **interactive command-line quiz application**.

Instead of generating a fixed number of quiz and answer-key files, the program allows the user to choose the number of questions and complete the quiz directly in the terminal.

The program:

1. Asks the user how many questions they want.
2. Randomly selects the requested number of states.
3. Generates four possible answers for each question.
4. Randomizes the order of the answer choices.
5. Lets the user answer each question.
6. Validates the user's input.
7. Checks each answer against the correct capital.
8. Calculates the final score.
9. Displays the score and percentage in the terminal.
10. Generates a results file containing the questions, user's answers, correct answers, and results.

The goal is to transform a simple automation exercise into a small, reusable command-line application while practicing good Python development practices.

## ✨ Features

- Interactive command-line interface.
- User chooses the number of questions.
- Randomly selects questions.
- Randomizes multiple-choice answers.
- Provides one correct answer and three incorrect answers.
- Accepts answers using `A`, `B`, `C`, or `D`.
- Validates user input.
- Calculates the final score.
- Displays the score and percentage in the terminal.
- Generates a detailed results file.
- Shows the user's answer alongside the correct answer.
- Uses Python's standard library.
- Includes automated tests.
- Uses static type checking with Mypy.
- Uses Ruff for linting and formatting.
- Uses `uv` for project and dependency management.

## 🛠️ Technologies and Tools

### Language

- **Python 3**

### Development Tools

- **uv** — Python project and dependency management
- **Pytest** — automated testing
- **Ruff** — linting and code formatting
- **Mypy** — static type checking

The project does not require external runtime dependencies.

## 📂 Project Structure

```text
interactive-state-capitals-quiz/
│
├── src/
│   ├── __init__.py
│   ├── data.py
│   └── quiz.py
│
├── tests/
│   ├── __init__.py
│   └── test_quiz.py
│
├── output/
│   └── quiz_results.txt
│
├── .gitignore
├── README.md
├── pyproject.toml
├── uv.lock
└── ...
```

> The exact structure may vary depending on the implementation.

## ▶️ How the Program Works

### 1. Choose the Number of Questions

When the program starts, the user is asked how many questions they would like to answer.

```text
=================================
     US State Capitals Quiz
=================================

How many questions would you like? 5
```

The program validates the input before starting the quiz.

### 2. Generate the Quiz

The program randomly selects states from the available state/capital data.

For each question, it generates four possible answers:

- One correct capital.
- Three randomly selected incorrect capitals.

The answer choices are then shuffled.

### 3. Answer the Questions

The user answers each question by entering `A`, `B`, `C`, or `D`.

Example:

```text
Question 1/5

What is the capital of California?

A. Phoenix
B. Sacramento
C. Denver
D. Austin

Your answer: B
```

The program validates the answer before continuing to the next question.

### 4. Calculate the Score

After the final question, the program calculates the user's score.

```text
=================================
            RESULTS
=================================

Score: 4/5
Percentage: 80%
```

### 5. Generate the Results File

The program creates a text file containing a detailed review of the completed quiz.

Example:

```text
US State Capitals Quiz - Results
================================

Score: 4/5
Percentage: 80%

Question 1:
What is the capital of California?

Your answer: Sacramento
Correct answer: Sacramento
Result: Correct

--------------------------------

Question 2:
What is the capital of Texas?

Your answer: Houston
Correct answer: Austin
Result: Incorrect

--------------------------------
```

This allows the user to review their answers after completing the quiz.

## 🎲 Randomization

Randomization is an important part of the project.

The program uses Python's `random` module to:

- Select random questions.
- Select incorrect answers.
- Shuffle the answer choices.

For example:

```python
random.shuffle(options)
```

This ensures that the correct answer does not always appear in the same position.

A different quiz session can therefore produce a different sequence of questions and answer choices.

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

The **state** is used as the question, while the corresponding **capital** is used as the correct answer.

The dictionary also provides the data needed to generate incorrect answers.

## 📄 Results

Each completed quiz produces a results file.

The results contain:

- Number of questions.
- Final score.
- Percentage.
- Each question.
- User's answer.
- Correct answer.
- Whether the answer was correct.

The results file provides a permanent record of the completed quiz.

## 🚀 Getting Started

### Prerequisites

This project uses [`uv`](https://docs.astral.sh/uv/) for Python version management, dependency management, and running development tools.

Python 3 is required. The project recommends Python 3.10 or newer.

Check your Python version:

```bash
python --version
```

Check that `uv` is installed:

```bash
uv --version
```

If `uv` is not installed, follow the official installation instructions:

https://docs.astral.sh/uv/getting-started/installation/

### Clone the Repository

```bash
git clone <repository-url>
cd interactive-state-capitals-quiz
```

### Install Dependencies

Install the project's dependencies and development tools using:

```bash
uv sync
```

`uv sync` creates the virtual environment if necessary and installs the dependencies defined in `pyproject.toml`.

## ▶️ Running the Quiz

Run the application with:

```bash
uv run python src/quiz.py
```

Follow the instructions displayed in the terminal.

Example:

```text
=================================
     US State Capitals Quiz
=================================

How many questions would you like? 5
```

## 🧪 Testing

The project uses **Pytest** for automated testing.

Run the complete test suite:

```bash
uv run pytest
```

For more detailed output:

```bash
uv run pytest -v
```

## 🔍 Code Quality

### Ruff

Ruff is used for both linting and formatting.

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

- Properly formatted.
- Free from common linting issues.
- Statically type-checked.
- Checked for common security vulnerabilities.
- Covered by automated tests.

## 🔄 Original Project vs. My Version

| Original Project                 | Interactive Version                          |
| -------------------------------- | -------------------------------------------- |
| Generates 35 quizzes             | Generates one quiz per session               |
| Fixed number of questions        | User chooses the number of questions         |
| Generates quiz text files        | User interacts with the quiz in the terminal |
| Generates answer keys            | Calculates the score automatically           |
| No user interaction              | Interactive user input                       |
| Quiz and answer key are separate | Generates a detailed results file            |
| Designed primarily for a teacher | Designed as an interactive CLI application   |

## 🎯 Learning Objectives

This project provides practice with several important Python concepts:

- Working with dictionaries.
- Working with lists.
- Writing reusable functions.
- Using loops.
- Generating random data.
- Shuffling collections.
- Handling user input.
- Validating user input.
- Using conditional statements.
- Reading and writing text files.
- Managing application state.
- Separating application logic into functions and modules.
- Writing automated tests.
- Adding type annotations.
- Running static type checking.
- Applying linting and formatting.
- Performing basic security analysis.
- Managing a Python project with `uv`.

## 💡 Future Improvements

Possible improvements for future versions include:

- Add difficulty levels.
- Add a timer.

## 📚 Reference

Inspired by:

_Automate the Boring Stuff with Python_
by Al Sweigart

Original exercise:

**Project 4: Generate Random Quiz Files**

This implementation modifies the original exercise to create an interactive command-line quiz rather than generating a fixed collection of quiz and answer-key files.

The project also extends the original exercise with user input, answer validation, score calculation, result generation, automated testing, static type checking, linting, formatting, and security analysis.
