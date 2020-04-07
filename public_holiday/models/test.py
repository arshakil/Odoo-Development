from datetime import datetime, timedelta

d1 = datetime(2021,2,15)
d2 = datetime(2021,3,15)

# this will give you a list containing all of the dates
dd = [d1 + timedelta(days=x) for x in range((d2-d1).days + 1)]
t_date=2021-02-15
count=0
for d in dd:
    print d


# you can't join dates, so if you want to use join, you need to
# cast to a string in the list comprehension:
# ddd = [str(d1 + timedelta(days=x)) for x in range((d2-d1).days + 1)]
# now you can join
# print "\n".join(ddd)


