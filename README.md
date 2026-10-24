### Introduction to Git
#### Basic git commands
`git add` used to add changes into staging
`git commit` used to commit changes
`git push` used to sync local changes to github

# Body Mass Index &#40;BMI&#41; Calculator – Git Assignment

## Introduction

This project was developed as part of the Statistical Computing course to practice the fundamentals of Git and GitHub\. It features a simple **Body Mass Index &#40;BMI&#41; Calculator** implemented in Python\.

The program accepts the user’s weight and height as inputs, calculates the BMI, and displays the resulting value\.

This assignment also provides practical experience with version control, including creating a Git repository, tracking changes, committing updates, and pushing changes to GitHub\.

## Features

- Accepts the user’s height and weight through keyboard input\.
- Converts the input values from strings to floating\-point numbers\.
- Calculates BMI using the following formula:
  **BMI = Weight &#40;kg&#41; / Height &#40;m&#41;²**
- Rounds the calculated BMI to two decimal places\.
- Displays the calculated BMI in the console\.
- Demonstrates basic Python input, output, and mathematical operations\.

## Prerequisites

Before running the project, ensure that Python and Git are installed on your computer\.

- **Python:** Check the installation by running:
  ```bash
  python --version
  ```
- **Git:** Check the installation by running:
  ```bash
  git --version
  ```

## Clone the Repository

To download the project to your local computer, follow these steps:

1. Create a folder named `git-assignment` and navigate to it in your terminal\.
2. Clone the repository using the following command:
   ```bash
   git clone https://github.com/tigiyeee/git-assignment.git
   ```
3. Navigate to the cloned repository:
   ```bash
   cd git-assignment
   ```

## How to Run the Program

Save the following code in a file named `SampleData.py`:

```python
height = input("Enter your height in metres: ")
weight = input("Enter your weight in kilograms: ")

h = float(height)
w = float(weight)

bmi = w / (h ** 2)

print("Your BMI is:", round(bmi, 2))
```

Run the Python script using the following command:

```bash
python SampleData.py
```

Follow the prompts to enter your height in metres and weight in kilograms\. The program will calculate and display your BMI rounded to two decimal places\.

## Python Input and Output

This project uses two fundamental Python functions:

- `input()` — collects input from the user\.
- `print()` — displays output in the console\.

The program also uses `float()` to convert the input values into numbers and performs the BMI calculation using mathematical operations\.

## Project Structure

The repository contains the following files:

- `README.md` — provides documentation about the project, its features, and instructions for use\.
- `SampleData.py` — contains the Python script used to calculate BMI\.
- `screenshot of commits.png` — shows the Git commit commands and changes applied to the online repository\.

## Learning Outcomes

Through this assignment, I practiced:

- Creating and cloning a Git repository\.
- Understanding the fundamentals of version control\.
- Tracking and committing changes\.
- Pushing local changes to GitHub\.
- Writing Python code using input, output, type conversion, and mathematical operations\.
- Documenting a project using Markdown\.

## Author

**Tigist K\.**
