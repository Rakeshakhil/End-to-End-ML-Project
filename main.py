from Insurance.logger import logging
from Insurance.exception import InsuranceException
import os
import sys
from Insurance.utils import get_collection_as_dataframe


#def test_logger_and_exception():

    # try:
    #logging.info('Starting test logger and exception')
    # result=3/0
    # print(result)
    #logging.info('Finished test logger and exception')
    # except Exception as e:
    # logging.debug(str(e))
    #raise InsuranceException(e,sys)


if __name__ == '__main__':
    try:
        # start_training_pipelining()
        get_collection_as_dataframe(database_name='Insurance', collection_name='Insurance_Project')
    except Exception as e:
        print('e')
