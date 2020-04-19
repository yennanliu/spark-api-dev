import os 
import pyspark 
from pyspark import SparkContext

class SparkInfo:

    def __init__(self):
        self.sc = pyspark.SparkContext.getOrCreate()
        self.sc.setLogLevel("ERROR")

    def GetVersion(self):
        version = self.sc.version
        return version


if __name__ == '__main__':
    s= SparkInfo()
    v = s.GetVersion()
    print (v)
    
