import os 
import pyspark 
from pyspark import SparkContext

sc = SparkContext.getOrCreate()

RDD1 = sc.parallelize([1,2,3,4,5])
RDD2 = sc.parallelize(["abc", "def", "ghi", "abc", "xyz"])
RDD3 = sc.parallelize([{"foo": 1, "bar": 2}, {"foo": 3, "baz": -1, "bar": 5}])

print ("*"*30)
print (RDD1)
print (RDD1.collect())
print ("*"*30)
