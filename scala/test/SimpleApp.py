"""SimpleApp.py"""
from pyspark import SparkContext

logFile = "D:/spark-1.0.2-bin-hadoop2/spark-1.0.2-bin-hadoop2/README.md"  # Should be some file on your system
sc = SparkContext("local", "Simple App")
logData = sc.textFile(logFile).cache()

numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()

print "%s Lines with a: %i, lines with b: %i" % (logFile, numAs, numBs)
