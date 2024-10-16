from tool import fibonacci_tool  # Import the Fibonacci function from tool.py
from flask import Flask, render_template, request, jsonify
import os
from benchmarking_tool import run_benchmark, visualize_results

app = Flask(__name__)

# Homepage route to trigger benchmarking
@app.route('/')
def index():
    return render_template('index.html')

# API route to calculate Fibonacci number
@app.route('/api/fibonacci', methods=['POST'])
def fibonacci_api():
    data = request.get_json()  # Get the data from the POST request
    n = data.get('n', 0)  # Get 'n' from the JSON request body
    result = fibonacci_tool(n)  # Call the Fibonacci function from tool.py
    return jsonify({"result": result})  # Return the result as JSON

# API to run the benchmarking tool and return results
@app.route('/run_benchmark', methods=['POST'])
def run_benchmark_api():
    n = int(request.form['n'])
    num_calls = int(request.form['num_calls'])

    # Run the benchmark and create visualizations
    results = run_benchmark(n, num_calls)
    visualize_results(results)

    # Send results and path to visualization image to the frontend
    return jsonify({
        'results': results,
        'visualization': '/static/benchmark_results.png'  # Path to saved image
    })

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8020)



# from flask import Flask, render_template, request, jsonify
# import os
# from benchmarking_tool import run_benchmark, visualize_results

# app = Flask(__name__)

# # Homepage route to trigger benchmarking
# @app.route('/')
# def index():
#     return render_template('index.html')

# # API to run the benchmarking tool and return results
# @app.route('/run_benchmark', methods=['POST'])
# def run_benchmark_api():
#     n = int(request.form['n'])
#     num_calls = int(request.form['num_calls'])

#     # Run the benchmark and create visualizations
#     results = run_benchmark(n, num_calls)
#     visualize_results(results)

#     # Send results and path to visualization image to the frontend
#     return jsonify({
#         'results': results,
#         'visualization': '/static/benchmark_results.png'  # Path to saved image
#     })

# # Run the Flask app
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=8010)
