#!/usr/bin/env python2
#Time-stamp: <2016-12-31 00:25:58 hamada>
import time
import glob
import logging
import Queue
import sys
import os.path
import logging as LG
import commands


def gen_code(quotes):
    c = '''#!/usr/bin/env python2
import os
import logging as LG
import random
import commands

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

def get_quotes():
    result = [ ]
    result.append("There is always light behind the clouds. -- Louisa May Alcott")
    result.append("Change before you have to. -- Jack Welch")
    result.append("If you can dream it, you can do it. -- Walt Disney")
    result.append("Love the life you live. Live the life you love. -- Bob Marley")
    result.append("My life didn't please me, so I created my life. -- Coco Chanel")
    result.append("It always seems impossible until it's done -- Nelson Mandela")
    result.append("Peace begins with a smile. -- Mother Teresa")
    result.append("Love dies only when growth stops. -- Pearl S. Buck")
    result.append("There is more to life than increasing its speed. -- Mahatma Gandhi")
    return result

if __name__ == "__main__":

    qs = get_quotes()
    qs.sort()
    msg = random.choice(qs)
    cmd = 'git commit -m "' + msg + '"; git push origin master;'
    print cmd
'''
    return c

'''
!! What a Wonderful World. !!
'''
if __name__ == "__main__":


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
        quotes_file = sys.argv[1]
        if not os.path.isfile(quotes_file):
            logger.error('File with list of quotes not found!: %s', quotes_file)
            sys.exit(0)
        logger.info('Processing file with list of quotes: %s', quotes_file)
    except:
        logger.error('Pass file path to list of quotes!')
        sys.exit(0)
    
    
    quotes  = [line.strip() for line in open(quotes_file)]
    
    code = gen_code(quotes)
    
    print code
    