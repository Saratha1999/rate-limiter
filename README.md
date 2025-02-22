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

### 4. Install Dependencies
Install all required packages using pip:
```bash
pip install -r requirements.txt
```

Required packages:
```
annotated-types==0.7.0
anyio==4.8.0
click==8.1.8
fastapi==0.115.8
h11==0.14.0
idna==3.10
pydantic==2.10.6
pydantic_core==2.27.2
redis==5.2.1
sniffio==1.3.1
starlette==0.45.3
typing_extensions==4.12.2
uvicorn==0.34.0
```


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
├── requirements.txt    # Project dependencies
└── main.py             # Main application file

