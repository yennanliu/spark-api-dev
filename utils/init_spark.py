import os 
import pyspark 
from pyspark import SparkContext

class InitSpark:

    def __init__(self):
        self.sc = pyspark\
                  .SparkContext\
                  .getOrCreate()
        self.sc.setLogLevel("ERROR")
