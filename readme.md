Python Data Types and Structures Assessment

This repository contains exercises designed to assess your understanding and mastery of Python’s data types and data structures. The assessment is divided into three parts, each focusing on tasks involving basic data types, list operations, tuples, sets, dictionaries, and error handling.
Structure Overview

The project is organized as follows:

.
├── part1.py
├── part2.py
├── part3.py
├── tests/
│   ├── test_part1.py
│   ├── test_part2.py
│   └── test_part3.py
├── requirements.txt

Getting Started
1. Clone the Repository

To start working on the exercises, clone the repository to your local machine:

git clone <repository_url>

2. Install Dependencies

If the project has any dependencies, they are listed in the requirements.txt file. Install them using pip:

pip install -r requirements.txt

3. Implement the Functions

Each file (part1.py, part2.py, part3.py) contains a set of function stubs. Your task is to implement the logic for each function, following the instructions provided in the docstrings.
4. Run the Tests

Once you have implemented the functions, you can run the tests to verify your solutions.
Run Unit Tests for Each Part

To run the unit tests for any part, use the following commands:

    Part 1 Test:

python -m unittest tests.test_part1

Part 2 Test:

python -m unittest tests.test_part2

Part 3 Test:

    python -m unittest tests.test_part3

Run All Tests at Once

You can also run all tests at once using:

python -m unittest discover tests/

5. Review the Test Results

If your implementation is correct, you will see output similar to this:

...
Ran 7 tests in 0.001s
OK

Contribution

If you want to contribute improvements, fixes, or additional exercises, feel free to fork this repository and submit a pull request. Any contributions are welcome!