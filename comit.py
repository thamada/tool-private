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

config_term_encode = 'euc-jp'       # set encode for your terminal
config_db_filename = './gitcount' # set filename for your database

def get_logger():
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

def get_shelve(fname):
    keyname = 'count'
    pickle_protocol = pickle.HIGHEST_PROTOCOL
    dic = shelve.open(fname, protocol=pickle_protocol)
    keys = dic.keys()

    if keyname not in keys: 
        dic[keyname] = 0
        dic.close()
        dic = shelve.open(fname, protocol=pickle_protocol)

    count = dic[keyname]
    dic[keyname] = count + 1
    dic.close()
    return count

def do_uncompress(filename):
    return True

def do_compress(filename):
    return True

if __name__ == "__main__":
    msg = ''
    logger = get_logger()
    qs = get_quotes()
    do_uncompress(config_db_filename)
    count = get_shelve(config_db_filename)
    do_compress(config_db_filename)
    msg = ("%d: %s" % (count+1, qs[count % len(qs)]))
    logger.info('### %s', msg.encode(config_term_encode))
    cmd = 'git commit -m "' + msg + '"; git push origin master;'
    print cmd.encode(config_term_encode)

