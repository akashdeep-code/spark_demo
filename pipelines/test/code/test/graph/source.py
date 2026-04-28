from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from test.config.ConfigStore import *
from test.functions import *

def source(spark: SparkSession) -> DataFrame:
    return spark.read.table("`akash_demos`.`demos`.`customers`")
