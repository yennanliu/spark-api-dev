# spark-api-dev
// run spark job via API call


## Quick start
```bash
# launch flask server
python api/app.py

# run spark demo job
curl http://0.0.0.0:8000/REST/api/v1.0/spark_demo_job
curl http://0.0.0.0:8000/REST/api/v1.0/spark_word_count
curl http://0.0.0.0:8000/REST/api/v1.0/spark_info
```