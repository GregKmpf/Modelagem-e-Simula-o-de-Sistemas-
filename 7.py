#7
import numpy as np
import scipy.stats as stats
antes = np.array([129, 132, 139, 132, 148, 126, 128, 137, 131, 118,
136, 116])
depois = np.array([122, 127, 134, 126, 144, 128, 122, 138, 125, 110,
130, 113])
n = len(antes)
t_crit = stats.t.ppf(0.995, df=n - 1)
# a) Antes
ma, sa = np.mean(antes), np.std(antes, ddof=1)
ic_a = (ma - t_crit * sa / np.sqrt(n), ma + t_crit * sa / np.sqrt(n))
# b) Depois
md, sd = np.mean(depois), np.std(depois, ddof=1)
ic_d = (md - t_crit * sd / np.sqrt(n), md + t_crit * sd / np.sqrt(n))