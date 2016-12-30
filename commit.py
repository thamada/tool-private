#!/usr/bin/env python2
#Time-stamp: <2016-12-30 16:09:58 hamada>
import time
import glob
import logging
import Queue
import sys
import os.path
import logging

# create logger
logger = logging.getLogger('commit')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
## logger.debug('debug message')
## logger.info('info message')
## logger.warn('warn message')
## logger.error('error message')
## logger.critical('critical message')

# Get list of quates from arguments
try:
    quotes_list = sys.argv[1]
    if not os.path.isfile(quotes_list):
        logger.error('File with list of quotes not found!: %s', quotes_list)
        print 
        sys.exit(0)
    logger.info('Processing file with list of quotes: %s', quotes_list)
except:
    logger.error('Pass file path to list of quotes!')
    print 
    sys.exit(0)


lines  = [line.strip() for line in open(quotes_list)]

for txt in lines:
    print txt

 
