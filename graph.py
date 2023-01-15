import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
from exchange_rate import ExchangeRate

rate = ExchangeRate()

d, r = rate.get_data_between_dates("2022-08-01", "2022-12-20","INR")
d2, r2 = rate.get_data_between_dates("2022-10-01", "2022-12-20","EUR")

plt.plot(d, r, color = 'red', label='inr')
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=10))
plt.gcf().autofmt_xdate()
for i in range(len(r)):
    plt.bar(d[i], r[i], width=2)
# plt.plot(d2, r2, color='blue', label='eur')

plt.show()