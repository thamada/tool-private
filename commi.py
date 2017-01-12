#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
#
# Copyright (c) 2017 by Tsuyoshi Hamada. All rights reserved.
#
import os
import logging as LG
import random
import commands
import shelve
import pickle
import sys
import hashlib
import re as REGEXP

# -- set encode for your terminal --
config_term_encode = 'euc-jp'

# -- set filename for your database --
config_db_filename = '/t m p/g i t  commit-  ' 


def get_logger(str_position = ''):

    log_basename = __file__

    # Don't use Python's hasattr()
    #     unless you're writing Python 3-only code 
    #     and understand how it works.
    if getattr(get_logger, "__count_called", None) is not None:
        log_basename = "%s @%s" % (__file__, str_position)
        get_logger.__count_called = get_logger.__count_called + 1
        '''
        print "----------------- %d times called!!" % (get_logger.__count_called)
        '''
    else:
        get_logger.__count_called = 1
        '''
        print "----------------- first time called!!"
        '''

    # create logger
    logger = LG.getLogger(os.path.basename(log_basename))

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
    return logger

def get_quotes():
    result = [ ]
    result.append(u"生きる -- 谷川俊太郎")
    # -- 
    result.append(u"生きているということ")
    result.append(u"いま生きているということ")
    result.append(u"それはのどがかわくということ")
    result.append(u"木漏れ日がまぶしいということ")
    result.append(u"ふっと或るメロディを思い出すということ")
    result.append(u"くしゃみをすること")
    result.append(u"あなたと手をつなぐこと")
    # -- 
    result.append(u"生きているということ")
    result.append(u"いま生きているということ")
    result.append(u"それはミニスカート")
    result.append(u"それはプラネタリウム")
    result.append(u"それはヨハン・シュトラウス")
    result.append(u"それはピカソ")
    result.append(u"それはアルプス")
    result.append(u"すべての美しいものに出会うということ")
    result.append(u"そして")
    result.append(u"かくされた悪を注意深くこばむこと")
    # --
    result.append(u"生きているということ")
    result.append(u"いま生きているということ")
    result.append(u"泣けるということ")
    result.append(u"笑えるということ")
    result.append(u"怒れるということ")
    result.append(u"自由ということ")
    # --
    result.append(u"生きているということ")
    result.append(u"いま生きているということ")
    result.append(u"いま遠くで犬が吠えるということ")
    result.append(u"いま地球が廻っているということ")
    result.append(u"いまどこかで産声があがるということ")
    result.append(u"いまどこかで兵士が傷つくということ")
    result.append(u"いまぶらんこがゆれているということ")
    result.append(u"いまいまがすぎてゆくこと")
    # --
    result.append(u"生きているということ")
    result.append(u"いま生きてるということ")
    result.append(u"鳥ははばたくということ")
    result.append(u"海はとどろくということ")
    result.append(u"かたつむりははうということ")
    result.append(u"人は愛するということ")
    result.append(u"あなたの手のぬくみ")
    result.append(u"いのちということ")
    result.append(u":-)                            ;-)")
    return result

def get_shelve(fname, logger=None):
    if logger is None: logger = get_logger('get_shelve()')

    keyname = 'count'
    pickle_protocol = pickle.HIGHEST_PROTOCOL
    try :
        dic = shelve.open(fname, protocol=pickle_protocol)
    except Exception as e:
        logger.error(e)
        logger.error(fname)
        sys.exit(-1)

    keys = dic.keys()

    if keyname not in keys: dic[keyname] = 0

    count = dic[keyname]
    dic[keyname] = count + 1
    dic.close()
    return count

def do_uncompress(filename, logger=None):
    if logger is None: logger = get_logger('do_uncompress()')
    check = commands.getoutput("hostname;time bzip2 -d %s.db.bz2" % filename )
    # logger.debug("%s", check)
    return True

def do_compress(filename, logger=None):
    if logger is None: logger = get_logger('do_compress()')
    check = commands.getoutput("hostname;time bzip2 -9 %s.db" % filename )
    # logger.debug("%s", check)
    return True

def get_id_git(logger=None):
    if logger is None: logger = get_logger('get_id_git()')
    check = commands.getoutput("git remote -v")
    # logger.debug(check)
    md5 = hashlib.md5()
    md5.update(check)
    md5sum = md5.hexdigest()
    # logger.debug(md5sum)
    return md5sum

def cut_space_str(str):
    return REGEXP.sub(r' +', '', str)

if __name__ == "__main__":
    msg = ''
    logger = get_logger()
    md5sum = get_id_git()
    db_filename = cut_space_str(config_db_filename + md5sum)

    do_uncompress(db_filename)
    count = get_shelve(db_filename)
    do_compress(db_filename)

    qs = get_quotes()
    msg = ("%d: %s" % (count+1, qs[count % len(qs)]))
    logger.info('# %s', db_filename.encode(config_term_encode))
    logger.info('# %s', msg.encode(config_term_encode))
    cmd = 'git commit -m "' + msg + '"; git push origin master;'
    print cmd.encode(config_term_encode)
