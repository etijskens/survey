# -*- coding: utf-8 -*-

"""
## Python package survey
"""

__version__ = '0.0.0'

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import numpy as np

# import pandas lib as pd
import pandas as pd
from pathlib import Path


p = Path(__file__).parent.parent / 'survey.xlsx'
# read by default 1st sheet of an excel file
df = pd.read_excel(p)

# print(df.columns)

# filter uantwerpen responses
Q2 = df['Q2'][1:].tolist()
# print(f'{Q2=}')
Q2ua = []
Q2ua_plus = []
for i,a in enumerate(Q2):
    # print(i,a)
    if isinstance(a,str):
        if 'UA' in a:
            # print(i,a)
            Q2ua.append(i)
            if ',' in a:
                Q2ua_plus.append(i)
# print(f'{Q2ua=}')
ua = df.loc[Q2ua]
print(f'{len(ua)} questions answered by "UAntwerpen affiliated".')
# print(ua)

def process_question(Q):
    question = df[Q][0]
    answers_set = list(set(ua[Q]))
    # print(f"{question}: {answers_set=}")
    n = len(ua[Q])
    frequencies = [0] * len(answers_set)
    for a in ua[Q]:
        i = answers_set.index(a)
        frequencies[i] += 1
    print(f"\n{Q}. {question}")
    for i,f in enumerate(frequencies):
        print(f"{100*f/n:6.1f}% : {answers_set[i]}")

for q in range(3,11):
    for i in range(1,8):
        process_question(F'Q{q}_{i}')

for q in [11,13]:
    process_question(f'Q{q}')

for i in range(1,5):
    process_question(f'Q14_{i}')

for q in range(15,27):
    process_question(f'Q{q}')

