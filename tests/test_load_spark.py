import pytest
import sys
sys.path.append(".")
from utils import init_spark


def test_load_spark():
	init_s = init_spark.InitSpark()
	#print ("****", str(init_s.sc))
	assert str(init_s.sc) == "<SparkContext master=local[*] appName=pyspark-shell>"

if __name__ == '__main__':
	pytest.main([__file__])
