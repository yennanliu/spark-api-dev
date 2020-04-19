import os, json 
from flask import Flask, jsonify, make_response, request, render_template
import sys
#sys.path.append(".")
#from utils import SparkTestJob
 
app = Flask(__name__)


# API hello world 
@app.route('/')
def hello_world():
    return "API Hello World!", 200

# Run spark demo job
@app.route('/REST/api/v1.0/spark_demo_job')
def run_spark_hello_world():
    try:
        os.system("spark-submit spark_job/SparkTestJob.py")
        return jsonify(job_status=True)
    except Exception as e:
        print (e)
        return jsonify(job_status=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)