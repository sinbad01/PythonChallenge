# -*- coding: utf-8 -*-
__author__ = "tongzhengyu"

import string

# url = 'http://www.pythonchallenge.com/pc/def/map.html'
# http://www.pythonchallenge.com/pc/def/ocr.html

if __name__ == "__main__":


    word = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

    # 规则是小写字母往后移2位
    frm2 = string.ascii_lowercase
    to2 = string.ascii_lowercase[2:] + string.ascii_lowercase[0:2]
    transSimple = str.maketrans(frm2, to2)
    print(word.translate(transSimple))

    print('map'.translate(transSimple))