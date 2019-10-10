from datetime import datetime, timedelta
import locale

dt_today = datetime.today()
locale.setlocale(locale.LC_ALL, 'russian')
dt_yesterday = datetime.strftime(datetime.now() - timedelta(1), '%A %d %B %Y')
dt_month = datetime.strftime(datetime.now() - timedelta(30), '%Y-%m-%d')

print(dt_today)
print(dt_yesterday)
print(dt_month)

date_string = '01/01/17 12:10:03.234567'
date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
print(date_dt)
