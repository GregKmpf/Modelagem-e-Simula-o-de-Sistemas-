import numpy as np
import scipy.stats as stats
n = 18
media = 3.2
sigma = np.sqrt(4)
z = stats.norm.ppf(0.99)
erro = z * (sigma / np.sqrt(n))
ic_inf = media - erro
ic_sup = media + erro
print(f"IC 98%: [{ic_inf:.4f}, {ic_sup:.4f}] uV")