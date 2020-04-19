import os 
import pyspark 
from pyspark import SparkContext

class SparkWordCount:

    def __init__(self):
        self.sc = pyspark.SparkContext.getOrCreate()
        self.sc.setLogLevel("ERROR")

    def WordCount(self):
        filenames = "README.md"
        data = self.sc.textFile(filenames)
        counts = data.flatMap( lambda line : line.split(" "))\
                     .map(lambda word : (word, 1))\
                     .collect() #.reduceByKey(lambda a,b : a+b)\
        print ("*"*30)
        print (counts)
        for count in counts:
            print (count)
        print ("*"*30)

if __name__ == '__main__':
    s = SparkWordCount()
    s.WordCount()