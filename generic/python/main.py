#!/usr/bin/env python3
import os
import sys

try:
    print("hello 130/10 is ", 130/0)
except Exception as E:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    # print(exc_type, )
    # print( fname)
    # print(exc_tb.tb_lineno)
    print(f'Python error: filename: "{fname}". line number: {exc_tb.tb_lineno}') 