#!/usr/bin/env python2
#Time-stamp: <2016-12-30 22:35:36 hamada>
import time
import glob
import logging
import Queue
import sys
import os.path
import logging as LG

# create logger
logger = LG.getLogger(os.path.basename(__file__))
logger.setLevel(LG.DEBUG)

# create console handler and set level to debug
ch = LG.StreamHandler()
ch.setLevel(LG.DEBUG)

# create formatter
formatter = LG.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

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
        sys.exit(0)
    logger.info('Processing file with list of quotes: %s', quotes_list)
except:
    logger.error('Pass file path to list of quotes!')
    sys.exit(0)


lines  = [line.strip() for line in open(quotes_list)]

for txt in lines:
    print txt

 
