#!/usr/bin/env python3
import os
import sys
import random


try:
    seed = 130/0
    print("Seed #", seed)
    random.seed(seed)
    print("random number between 0 100 is ", random.randint(0, 100))
except Exception as E:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(f'Python error occurred. Unable to generate random number: filename: "{fname}". line number: {exc_tb.tb_lineno}', flush=True)
    os._exit(1)