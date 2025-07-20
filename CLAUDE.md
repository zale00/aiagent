# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an AI coding agent built as part of the Boot.dev course "Build an AI agent in Python". The agent uses Google's Gemini API (gemini-2.0-flash-001) to provide a command-line interface for code assistance with function calling capabilities.

## Architecture

### Core Components

1. **main.py** - Entry point that handles CLI arguments and orchestrates the Gemini API interaction
2. **call_functions.py** - Function routing system that maps Gemini function calls to actual Python implementations
3. **prompts.py** - System prompt configuration
4. **config.py** - Constants including MAX_CHARS (10000) and WORKING_DIR ("./calculator")

### Function Tools

The agent provides four core functions (all in `functions/` directory):
- `get_files_info` - Lists files in directories (constrained to working directory)
- `get_file_content` - Reads file contents (with character limit)
- `run_python_file` - Executes Python files with optional arguments
- `write_file` - Creates or overwrites files

All functions include security constraints to prevent access outside the working directory.

### Calculator Sample Project

The `calculator/` directory contains a sample project the agent can manipulate:
- `main.py` - CLI calculator entry point
- `pkg/calculator.py` - Calculator implementation
- `pkg/render.py` - Output formatting
- `tests.py` - Unit tests using unittest

## Key Commands

### Running the Agent
```bash
# Basic usage
python main.py "your prompt here"

# With verbose output (shows token counts and function details)
python main.py "your prompt here" --verbose

# Example
python main.py "How do I fix the calculator?"
```

### Development Dependencies
```bash
# Using uv (preferred)
uv pip install -e .

# The project uses:
# - google-genai==1.12.1
# - python-dotenv==1.1.0
# - Python >=3.13
```

### Testing
```bash
# Run the agent's test suite
python tests..py

# Run calculator tests
python calculator/tests.py

# Run a single test
python -m unittest calculator.tests.TestCalculator.test_1
```

## Environment Setup

Create a `.env` file with:
```
GEMINI_API_KEY=your-api-key-here
```

## Security Constraints

- All file operations are sandboxed to the configured WORKING_DIR
- Path traversal attempts are blocked
- File content reading is limited to MAX_CHARS (10000)
- Python execution has a 30-second timeout

## Function Calling Flow

1. User provides a prompt via CLI
2. System prompt + user prompt sent to Gemini with available function declarations
3. Gemini responds with function calls
4. `call_function()` routes to appropriate Python implementation
5. Function results are collected and could be sent back to Gemini for further processing
6. Final response is printed to console

Note: The current implementation collects function responses but doesn't send them back to Gemini for a follow-up response.