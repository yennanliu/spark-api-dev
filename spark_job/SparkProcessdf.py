import pyspark
from pyspark import SparkContext
from pyspark.sql import SparkSession

class SparkProcessdf:
    def __init__(self):
        self.sc = pyspark.SparkContext.getOrCreate()
        self.sc.setLogLevel("ERROR")
        self.spark = SparkSession \
            .builder \
            .appName("SparkProcessdf") \
            .getOrCreate()

    def loaddf(self):
        df = self.spark.read.format("csv").option("header", "true").load("data/boston.csv")
        return df

if __name__ == '__main__':
    s=SparkProcessdf()
    df=s.loaddf()
    print (df.show())