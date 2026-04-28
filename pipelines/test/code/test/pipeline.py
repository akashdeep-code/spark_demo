from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from test.config.ConfigStore import *
from test.functions import *
from prophecy.utils import *
from test.graph import *

def pipeline(spark: SparkSession) -> None:
    df_source = source(spark)
    df_Filter_1 = Filter_1(spark, df_source)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("test").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/test")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/test", config = Config)(pipeline)

if __name__ == "__main__":
    main()
