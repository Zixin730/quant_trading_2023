import pandas as pd
import numpy as np

from plotnine import *
from plotnine.data import *

# line
(
    ggplot(economics, aes(x='date', y='uempmed'))
    + geom_line() # line plot
    + labs(x='date', y='median duration of unemployment')
)

