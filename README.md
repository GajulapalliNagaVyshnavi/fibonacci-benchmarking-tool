# Fibonacci API & Benchmarking Tool

This repository contains a Flask-based API that calculates Fibonacci numbers and a benchmarking tool that compares different methods (Normal, Batch, Async, Multithreading, and Multiprocessing) for calling the API. The project visualizes the performance of each method, including time taken, CPU, and memory usage.

## Features
- Fibonacci number calculation via API.
- Benchmarking of different API call methods.
- Resource usage tracking and visualization (Time taken, CPU and Memory).
- Performance graphs automatically generated.

## Prerequisites
- Python 3.11 (recommended)
- Flask
- Requests
- Aiohttp
- Psutil
- Matplotlib

## Setup Guide

### 1. Clone the repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/your-username/fibonacci-benchmarking-tool.git
cd fibonacci-benchmarking-tool
```

### 2. Creating a Conda environment
It's recommended to use **Conda** to create a virtual environment for this project. Run the following commands:

```bash
conda create --name <env_name> python=3.11
conda activate <env_name>
```

### 3. Install the required dependencies
To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file yet, you can generate it with:

```bash
pip freeze > requirements.txt
```

### 4. Running the Flask App
Run the app using:

```bash
python app.py
```

The app will run at `http://127.0.0.1:8020/`. You can now access the API and the homepage by navigating to this URL in your browser.

### 5. API Endpoints
#### 5.1. Fibonacci API
- **URL**: `/api/fibonacci`
- **Method**: POST
- **Body**: JSON with key `n` (integer).
- **Response**: JSON with the Fibonacci result.

Example:
```bash
curl -X POST http://127.0.0.1:8020/api/fibonacci -H "Content-Type: application/json" -d '{"n": 10}'
```

#### 5.2. Benchmarking API
- **URL**: `/run_benchmark`
- **Method**: POST
- **Form data**: 
  - `n`: Fibonacci number to calculate.
  - `num_calls`: Number of API calls to benchmark.
  
Example:
```bash
curl -X POST http://127.0.0.1:8020/run_benchmark -F "n=10" -F "num_calls=100"
```

### 6. Benchmarking Methods
- **Normal API Call**: Synchronous calls.
- **Batch API Call**: A group of synchronous calls.
- **Async API Call**: Asynchronous calls using `aiohttp`.
- **Multithreading API Call**: Concurrent calls using threading.
- **Multiprocessing API Call**: Concurrent calls using multiple processes.

The benchmarking results, including the total time, CPU, and memory usage, are displayed on the frontend. Visualizations are saved to the `static/` directory.

### 7. Visualization
Performance visualizations are saved to `static/benchmark_result.png` and accessible via the frontend.

### Project Structure

```
fibonacci-benchmarking-tool/
│
├── experiment/
│   ├── pycache/
│   ├── static/
│   │   └── benchmark_result.png
│   ├── templates/
│   │   └── index.html
│   ├── app.py
│   ├── benchmarking_tool.py
│   └── tool.py
├── requirements.txt
└── readme.md

```

### Example Usage

1. Visit `http://127.0.0.1:8020/` in your browser.
2. Input the desired Fibonacci number (`n`) and the number of API calls to benchmark.
3. View the results and performance visualizations directly on the webpage.

## Contributing
Feel free to open issues or submit pull requests to contribute to this project. All feedback is welcome!

## Acknowledgment
This project was created by:
- **HARIPREETH AVARUR** (HARI.AVARUR@GMAIL.COM)
- **GAJULAPALLI NAGA VYSHNAVI** (nvyshnavi36@gmail.com) (https://github.com/gajulapallinagavyshnavi)
