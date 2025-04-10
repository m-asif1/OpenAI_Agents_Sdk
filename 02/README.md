# 02: Asynchronous & Streaming Agents with OpenAI Agent SDK
This repository contains the code, examples, and project structure for 02 of "OpenAI Agent SDK" In this dive into asynchronous programming concepts, explore streaming data techniques, and demonstrate how to build more responsive and efficient AI agents.
## Introduction
`Project02` introducing asynchronous programming within the context of AI agents. How to leverage asynchronous operations to improve the performance and responsiveness of your agents, as well as techniques for handling streaming data. It's covers:   
- Asynchronous programming fundamentals.
- Implementing asynchronous agents with the OpenAI Agent SDK.
- Understanding and handling streaming data responses.
- Comparing synchronous and asynchronous agent performance.    

## Overview
- **Asynchronous Programming Concepts:**  
An overview of asynchronous programming principles, including the event loop, tasks, and coroutines. This section explains how async functionality can help manage I/O-bound tasks without blocking the execution flow.

- **Async Agent Implementation:**  
Detailed walkthroughs of files such as `3_async_agent.py` and `1_async_concepts.py` demonstrate how to implement asynchronous behaviors in agent operations.

- **Streaming Data with AI Agents:**  
The lecture introduces `3_streaming_agent.py`, which shows how to process streaming data in real time, allowing your agent to output results as they become available.

- **Synchronous vs. Asynchronous Agents:**  
The code in `simple_agent.py` contrasts the basic synchronous agent implementation with the asynchronous approach, highlighting benefits like improved responsiveness and resource efficiency.

## Project Structure
Below is an overview of the repository layout for 02:  
```
02/
├── .env     # Environment configuration file (store secrets and API keys)
├── .gitignore          # Specifies files and directories to be ignored by Git
├── .python-version     # Specifies the Python version to be used for the project
├── pyproject.toml      # Project configuration and dependency management file
├── uv.lock             # Lock file for dependency versions (if applicable)
└── src/
    └── project02/      # Contains the source code for the lecture project
        ├── 3_async_agent.py       # Implements asynchronous agent operations
         ├── 1_async_concepts.py    # Contains core asynchronous programming concepts for agents
         ├── 2_multitasking.py    # Contains asynchronous concepts for agents
         ├── simple_agent.py      # Basic synchronous agent implementation for comparison
         └── 4_streaming_agent.py   # Demonstrates handling of streaming data in agents
```
Each file plays a specific role in demonstrating different aspects of asynchronous and streaming capabilities:

- **3_async_agent.py:** Implements an agent using async operations.
- **1_async_concepts.py:** Explores underlying asynchronous principles applied in our agents.
- **simple_agent.py:** Provides a baseline synchronous agent for performance comparison.
- **4_streaming_agent.py:** Shows how to process and output data as it streams from a data source.


## Prerequisites
Before getting started, make sure you have the following:

- Python 3.8+ installed on your system.
- Basic knowledge of Python programming and asynchronous concepts (e.g., `asyncio`).
- Familiarity with Git for repository cloning and version control.
- Any required API keys or configurations as specified in the `.env` file.

## Installation & Setup
Follow these steps to set up the project on your local machine:
1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd project02
   ```

2. **Create and activate a virtual environment:**
    ```
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
    ```
3. **Install Dependencies:** Use the dependency manager specified in `pyproject.toml:` or install directly with pip:
    ```
    pip install -r requirements.txt
    ```
    Note: If a `requirements.txt` file isn’t provided, refer to `pyproject.toml` for dependency details.   

4. **Configure Environment Variables:**

    - Copy the sample `.env` file if provided or create a new `.env` file.
    - Add your API keys and other sensitive configuration data.

## Usage
To run the different agent implementations, execute the corresponding Python files from the src/project02 directory. For example:

- **Run the Asynchronous Agent:**
    ```
    python src/project02/1_async_agent.py
    ```
- **Run the Simple (Synchronous) Agent:**
    ```
    python src/project02/simple_agent.py
    ```
- **Run the Streaming Agent:**
    ```
    python src/project02/4_streaming_agent.py
    ```
This command will start the agent and demonstrate the functionalities.

## Key Concepts
- **Asynchronous Programming:**   
    - Event loops and coroutines.
    - Non-blocking I/O operations.
    - Task scheduling and management with `asyncio`.

- **Agent Design Patterns:**  
    - How to design agents that can handle multiple tasks concurrently.
    - Practical use cases for async agents in real-time applications.

- **Streaming Data Processing:**  
    - Techniques for processing data streams.
    - Benefits of streaming data for improved responsiveness and user experience.

- **Performance Comparison:**  
    - Evaluating the differences in performance and responsiveness between synchronous and asynchronous implementations.


