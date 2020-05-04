import os, json 
from flask import Flask, jsonify, make_response, request, render_template
import subprocess
import sys
sys.path.append(".")
#from script import GetSparkInfo

 
app = Flask(__name__)

# API hello world 
@app.route('/')
def hello_world():
    return "API Hello World!", 200

# spark server info
@app.route('/REST/api/v1.0/spark_info')
def get_spark_server_info():
    pyspark_info = subprocess.check_output('which pyspark', shell=True).decode("utf-8").strip("\n")
    java_info = subprocess.check_output('which java', shell=True).decode("utf-8").strip("\n")
    #java_version = subprocess.check_output('java -version 2>&1 | awk '/version/ {print $3}'', shell=True).decode("utf-8").strip("\n")
    #g = GetSparkInfo.SparkInfo()
    #version = g.GetVersion()
    return jsonify(pyspark=pyspark_info, 
                   java=java_info)

# Run spark demo job
@app.route('/REST/api/v1.0/spark_demo_job')
def run_spark_hello_world():
    try:
        os.system("spark-submit spark_job/SparkTestJob.py")
        return jsonify(job_status=True)
    except Exception as e:
        print (e)
        return jsonify(job_status=False)

# Run spark word count job
@app.route('/REST/api/v1.0/spark_word_count')
def run_spark_word_count():
    try:
        os.system("spark-submit spark_job/SparkWordCountJob.py")
        return jsonify(job_status=True)
    except Exception as e:
        print (e)
        return jsonify(job_status=False)

# Run spark load df job
@app.route('/REST/api/v1.0/spark_process_df')
def run_spark_process_df():
    try:
        os.system("spark-submit spark_job/SparkProcessdf.py")
        return jsonify(job_status=True)
    except Exception as e:
        print (e)
        return jsonify(job_status=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)