# The Gallup organization released the results of poll comparing the lifestyle today with yesterday. Thesurvey based ontelephone interviewed of 1030 adultsand it found that 450 adults spend less than 3 hours watching TV on average weekday

# a Construct 95 percent confidence interval for adults who spend less than 3 hours watching TV on average weekday

# b Construct 95 percent confidence interval for adults who spend higher than 3 hourswatching TV on average weekday

from statsmodels.stats.proportion import proportion_confint

Less_three_hour = proportion_confint(450, 1030, method = 'normal')
more_three_hour = proportion_confint(1030 - 450, 1030, method = 'normal')

print(Less_three_hour)
print(more_three_hour)