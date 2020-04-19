import os 
import pyspark 
from pyspark import SparkContext

class SparkInfo:

    def __init__(self):
        self.sc = pyspark.SparkContext.getOrCreate()
        self.sc.setLogLevel("ERROR")

    def GetVersion(self):
        return sc.version