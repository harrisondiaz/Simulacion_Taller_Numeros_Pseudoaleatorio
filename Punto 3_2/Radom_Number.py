import numpy as np
from scipy import stats


class PruebasEstadisticas:
    def __init__(self, data):
        self.data = data

    def prueba_media(self, mu):
        t_stat, p_value = stats.ttest_1samp(self.data, mu)
        return t_stat, p_value

    def prueba_varianza(self, sigma_sq):
        chi2_stat = ((len(self.data) - 1) * np.var(self.data)) / sigma_sq
        p_value = 1 - stats.chi2.cdf(chi2_stat, df=len(self.data) - 1)
        return chi2_stat, p_value

    def prueba_ks(self, dist_name, alpha=0.05):
        _, p_value = stats.kstest(self.data, dist_name)
        return p_value < alpha

    def prueba_chi2(self, observed, expected):
        chi2_stat, p_value = stats.chisquare(f_obs=observed, f_exp=expected)
        return chi2_stat, p_value

    def prueba_poker(self, alpha=0.05):
        poker_classes = ['Diferente', 'Un par', 'Dos pares', 'Tercia', 'Full', 'Poker', 'Quintilla']
        frequencies = [self.data.count(i) for i in range(7)]
        expected_frequencies = [len(self.data) * 0.3024, len(self.data) * 0.504, len(self.data) * 0.108,
                                len(self.data) * 0.072, len(self.data) * 0.009, len(self.data) * 0.0045,
                                len(self.data) * 0.0001]
        chi2_stat, p_value = stats.chisquare(f_obs=frequencies, f_exp=expected_frequencies)
        return chi2_stat, p_value, poker_classes