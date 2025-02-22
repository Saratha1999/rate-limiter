# Rate Limiter using Redis & FastAPI

Project Setup Guide

## Prerequisites
- Python 3.x
- pip (Python package installer)

## Setting Up the Development Environment

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/rate-limiter.git
cd rate-limiter
```

### 2. Create a Virtual Environment
Create a new virtual environment in a local folder named `.venv`:
```bash
python3 -m venv .venv
```

### 3. Activate the Virtual Environment
#### On Unix or MacOS:
```bash
source .venv/bin/activate
```

#### On Windows:
```bash
.venv\Scripts\activate
```
Once activated, your terminal prompt should change to indicate you're working in the virtual environment.


## Running the Application
Start the FastAPI server:
```bash
uvicorn main:app --reload
```
The application will be available at `http://127.0.0.1:8000/`

## Development
- The virtual environment must be activated whenever you're working on the project
- To deactivate the virtual environment when you're done, simply run:
  ```bash
  deactivate
  ```

## Project Structure
```
project/
├── .venv/              # Virtual environment directory
└── main.py            # Main application file
```

