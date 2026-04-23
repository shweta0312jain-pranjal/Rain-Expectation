import scipy.stats as stats

prob1 = stats.poisson.pmf(6, 10)
print("The probability of exactly 6 rainy days in a 10-day period is:", prob1)

prob2 = stats.poisson.cdf(12, 14) + stats.poisson.cdf(13, 10) + stats.poisson.cdf(14, 10)
print("The probability of having at most 12 rainy days in a 14-day period is:", prob2)