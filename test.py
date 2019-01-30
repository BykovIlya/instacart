import matplotlib
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns #visualization
import matplotlib.pyplot as plt

color = sns.color_palette()

%matplotlib inline

pd.options.mode.chained_assignment = None  # default='warn'

from subprocess import check_output
print(check_output(["ls", "../input"]).decode("utf8"))