from Insurance.logger import logging
from Insurance.exception import InsuranceException
import os
import sys
from Insurance.utils import get_collection_as_dataframe
from Insurance.entity.config_entity import DataIngestionConfig
from Insurance.entity import config_entity


# def test_logger_and_exception():

# try:
#logging.info('Starting test logger and exception')
# result=3/0
# print(result)
#logging.info('Finished test logger and exception')
# except Exception as e:
# logging.debug(str(e))
#raise InsuranceException(e,sys)


if __name__=="__main__":
    try:
          #start_training_pipeline()
          #test_logger_and_expection()
       # get_collection_as_dataframe(database_name ="INSURANCE", collection_name = 'INSURANCE_PROJECT')
        training_pipeline_config = config_entity.TrainingPipelineConfig()
       
      #data ingestion
        data_ingestion_config  = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        print(data_ingestion_config.to_dict())
    except Exception as e:
        print(e)