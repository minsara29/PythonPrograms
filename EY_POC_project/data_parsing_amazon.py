from pyspark.sql import SparkSession


spark = SparkSession \
    .builder \
    .master("local[3]")\
    .appName("data processing") \
    .getOrCreate()

print("starting pyspark.......")

application = spark.read.format("csv").\
    option("header", "true").\
    load("output/amazon_qa/qa_Appliances.csv")

# application.show()
application_cnt = application.count()
print(application_cnt)

arts_crafts_and_sewing = spark.read.format("csv").\
    option("header", "true").\
    load("output/amazon_qa/qa_Arts_Crafts_and_Sewing.csv")

# arts_crafts_and_sewing.show()
arts_crafts_and_sewing_cnt = arts_crafts_and_sewing.count()
print(arts_crafts_and_sewing_cnt)


df = application.unionByName(arts_crafts_and_sewing)

# df.show()
df_cnt = df.count()
print(df_cnt)


print("stopping pyspark.......")