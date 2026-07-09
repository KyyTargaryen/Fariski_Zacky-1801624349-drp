import os

os.environ["PYSPARK_PYTHON"] = r"C:\Users\DELL\AppData\Local\Programs\Python\Python314\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = r"C:\Users\DELL\AppData\Local\Programs\Python\Python314\python.exe"

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Membuat Spark Session
spark = SparkSession.builder \
    .appName("Mood Tracker Analysis") \
    .master("local[2]") \
    .getOrCreate()

# Membaca file JSON
df = spark.read.option("multiline", "true").json("mood_dummy.json")

# Menampilkan schema
print("=== Schema Data ===")
df.printSchema()

# Menampilkan 5 data pertama
print("\n=== Contoh Data ===")
df.show(5)

# Jumlah seluruh data
print("\n=== Total Data ===")
print(df.count())

# Menghitung jumlah setiap kategori mood (DataFrame API)
print("\n=== Jumlah Tiap Mood (DataFrame) ===")
df.groupBy("result").count().show()

# Filter hanya Mood Positif
print("\n=== Data Mood Positif ===")
df.filter(col("result") == "Mood Positif").show(10)

# ==========================
# Implementasi MapReduce (RDD)
# ==========================

print("\n=== MapReduce (RDD) ===")

rdd = df.rdd.repartition(2)

hasil = (
    rdd
    .map(lambda row: (row["result"], 1))
    .reduceByKey(lambda a, b: a + b)
    .collect()
)

for mood, jumlah in hasil:
    print(f"{mood} : {jumlah}")

# Menghentikan Spark
spark.stop()
