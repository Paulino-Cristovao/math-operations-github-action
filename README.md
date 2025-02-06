# math-operations-github-action
# Math Operations

## Project Overview
This project demonstrates how to use GitHub Actions to automate testing and code quality checks for a Python project. The project includes simple mathematical operations such as addition, subtraction, multiplication, and division.

## Folder Structure
- `.github/workflows`: Contains GitHub Actions workflow files.
- `src`: Contains the source code for the mathematical operations.
- `tests`: Contains test files for the mathematical operations.
- `requirements.txt`: Lists the dependencies required for the project.
- `mypy.ini`: Configuration file for Mypy.
- `setup.cfg`: Configuration file for Flake8 and Pylint.

## How to Run the Project
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/math-operations.git
    ```
2. Navigate to the project directory:
    ```sh
    cd math-operations
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Run the tests:
    ```sh
    pytest tests
    ```

## GitHub Actions CI/CD
The project includes a GitHub Actions workflow (`.github/workflows/ci.yml`) that runs the tests and code quality checks automatically on each push and pull request.
