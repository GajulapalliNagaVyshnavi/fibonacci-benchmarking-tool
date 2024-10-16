import time
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool
import asyncio
import aiohttp
import requests
import matplotlib.pyplot as plt
import psutil
import os


API_URL = 'http://127.0.0.1:8020/api/fibonacci' #please make sure the flask api and this is same 

#Synchronous Call
def normal_api_call(n):
    response = requests.post(API_URL, json={"n": n})
    if response.status_code == 200:
        return response.json()["result"]
    return None

#Batch API Call
def batch_api_call(n, batch_size):
    results = []
    for _ in range(batch_size):
        start_time = time.time()
        response = requests.post(API_URL, json={"n": n})
        end_time = time.time()
        if response.status_code == 200:
            results.append(response.json()["result"])
    return results

#Asynchronous API Call
async def async_api_call(n):
    async with aiohttp.ClientSession() as session:
        async with session.post(API_URL, json={"n": n}) as response:
            if response.status == 200:
                return (await response.json())["result"]

async def benchmark_async_api_call(n, num_calls=100):
    tasks = [async_api_call(n) for _ in range(num_calls)]
    results = await asyncio.gather(*tasks)
    return [result for result in results if result is not None]

def run_async_benchmark(n, num_calls=100):
    return asyncio.run(benchmark_async_api_call(n, num_calls))

#Multithreaded API Call
def threaded_api_call(n):
    response = requests.post(API_URL, json={"n": n})
    if response.status_code == 200:
        return response.json()["result"]

def benchmark_threaded_api_call(n, num_calls=100):
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(threaded_api_call, [n] * num_calls))
    return [result for result in results if result is not None]

#Multiprocessing API Call
def multiprocessing_api_call(n):
    response = requests.post(API_URL, json={"n": n})
    if response.status_code == 200:
        return response.json()["result"]

def benchmark_multiprocessing_api_call(n, num_calls=100):
    with Pool(processes=4) as pool:
        results = pool.map(multiprocessing_api_call, [n] * num_calls)
    return [result for result in results if result is not None]

#Function to measure CPU and memory usage
def measure_resources():
    process = psutil.Process()
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = process.memory_info().rss / (1024 * 1024)  # Convert to MB
    return cpu_usage, memory_usage

def run_benchmark(n, num_calls=100):
    methods = {
        "Normal Call": (normal_api_call, [n]),
        "Batch Call": (batch_api_call, [n, num_calls]),
        "Async Call": (run_async_benchmark, [n, num_calls]),
        "Threaded Call": (benchmark_threaded_api_call, [n, num_calls]),
        "Multiprocessing Call": (benchmark_multiprocessing_api_call, [n, num_calls])
    }
    
    results = {}
    resources = {}
    
    for method_name, (method, args) in methods.items():
        start_cpu, start_mem = measure_resources()
        start_time = time.time()
        result = method(*args)
        end_time = time.time()
        end_cpu, end_mem = measure_resources()
        
        results[method_name] = {
            "total_time": end_time - start_time,
            "cpu_usage": end_cpu - start_cpu,
            "memory_usage": end_mem - start_mem,
            "result": result
        }
    
    return results

def visualize_results(results, save_path='static/benchmark_results.png'):
    methods = list(results.keys())
    total_times = [results[method]['total_time'] for method in methods]
    
    plt.figure(figsize=(10, 5))
    
    plt.bar(methods, total_times, color='blue')
    plt.xlabel('Methods')
    plt.ylabel('Total Time (s)')
    plt.title('Total Time for Each Method')
    
    # Save the figure to the specified path
    plt.savefig(save_path, format='png')
    print(f"Results visualized and saved to {save_path}")
