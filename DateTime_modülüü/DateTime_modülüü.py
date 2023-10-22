from datetime import date, datetime

bugün=date.today()
print(bugün)
print(type(bugün))
print(bugün.day)
print(bugün.month)
print(bugün.year)

print(bugün.isoweekday())

geçmiş_tarih=date(2015,8,14)
print(geçmiş_tarih)
print(geçmiş_tarih.weekday())

geçen_zzaman=bugün-geçmiş_tarih
print(geçen_zzaman)
print(type(geçen_zzaman))

şuan= datetime.now()
print(type(şuan))

print(bugün.strftime("%d- %m- %Y"))
print(datetime.strftime(bugün,"%d-%m-%y"))

from datetime import timedelta
tdelta=timedelta(days=7,hours=5,seconds=62) #belirtilen değerler için tarih vb.değiştirir.
print(şuan+timedelta)
print(şuan-timedelta)
