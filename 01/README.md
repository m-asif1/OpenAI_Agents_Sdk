# 01: Introduction to OpenAI Agent SDK
This repository contains the code, examples, and project structure for 01 of the course "OpenAI Agent SDK: Learn from Scratch." In this introduced the OpenAI Agent SDK, its core concepts, and setting up first AI agent project.
## Overview
`Project1` is a Python-based application that leverages OpenAI's generative language models to create conversational agents. The project demonstrates how to build and run agents using OpenAI's SDK with support for synchronous operations.

- **What is an AI Agent?**  
An AI agent is a software entity that uses artificial intelligence to perform tasks autonomously. We discussed the importance of agents in automating processes, decision-making, and interactive systems.

- **OpenAI Agent SDK Introduction:**  
A high-level overview of the SDK’s capabilities, including how it simplifies integrating AI functionalities into your projects.

- **Project Setup & Environment Configuration:**  
We reviewed how to configure your Python environment, set up required environment variables, and use the provided .env file to manage sensitive data.

- **Code Walkthrough:**  
A step-by-step explanation of the repository structure, including key files such as .gitignore, pyproject.toml, and the project source code in the src/project01 folder.

- **Practical Example:**  
Demonstration of a basic AI agent in action, showcasing how to initialize and run the agent using the SDK.

## Features
- **Agent Creation**: Build custom agents with specific instructions.
- **Model Integration**: Uses OpenAI's `gemini-2.0-flash-exp` model for generating responses.
- **Environment Configuration**: Securely manage API keys and model configurations using a `.env` file.

## Project Structure
Below is an overview of the repository layout for 01:  
```
01/
├── .env                # Environment configuration file (store secrets and API keys)
├── .gitignore          # Specifies files and directories to be ignored by Git
├── .python-version     # Specifies the Python version to be used for the project
├── pyproject.toml      # Project configuration and dependency management file
├── uv.lock             # Lock file for dependency versions (if applicable)
└── src/
    └── project01/      # Contains the source code for the lecture project
```
- **.env:**
Ensure you add your API keys and configuration settings here.

- **.gitignore:**
Lists files that should not be tracked by Git (e.g., sensitive information, compiled files).

- **pyproject.toml:**
This file manages project dependencies and settings. It is essential for building and running your project correctly.

- **src/project01:**
Contains the main project code that demonstrates how to set up and run your AI agent.

## Prerequisites
Before getting started, make sure you have the following:

- Python 3.8+ installed on your system.
- Basic knowledge of Python programming.
- Familiarity with virtual environments and dependency management.
- Git installed to clone the repository.

## Installation & Setup
Follow these steps to set up the project on your local machine:
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd project1
   ```

2. Create and activate a virtual environment:
```
python -m venv .venv
source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
```
3. Install Dependencies: If using a dependency manager like Poetry or pip, install the requirements specified in `pyproject.toml:`
```
pip install -r requirements.txt
```
(If a requirements file is not available, check `pyproject.toml` for dependency instructions.)

4. Configure Environment Variables:

    - Set up the `.env file:` Create a `.env` file in the src directory with the following content:
    ```
    GEMINI_API_KEY=your_api_key_here
    MODEL=gemini/gemini-2.0-flash-exp
    ```
## Usage
After setting up the project, you can run the AI agent by executing the main script in the src/project01 directory. For example:
```
python src/project05/main.py
```
This command will start the agent and demonstrate the basic functionalities.

## Key Concepts
- **AI Agent Fundamentals:**   
An introduction to AI agents and their potential applications.

- **SDK Utilization:**  
How the OpenAI Agent SDK abstracts and simplifies complex AI functionalities.

- **Environment Setup:**  
Importance of proper environment configuration, managing dependencies, and security (using .env files).

- **Project Architecture:**  
Understanding the structure of an AI project for maintainability and scalability.

- **Practical Implementation:**  
A live coding example showing how to initialize, configure, and run a basic AI agent.

