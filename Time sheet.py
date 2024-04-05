sun=int(input())
mon=int(input())
tue=int(input())
wed=int(input())
thu=int(input())
fri=int(input())
sat=int(input())
rate1=sun*150
rate7=sat*125
if mon<=8:
    rate2=mon*100
else:
    bonus=mon-8
    bonus_rate=bonus*115
    rate2=bonus_rate+800
if tue <=8:
    rate3=tue*100
else:
    bonus=tue-8
    bonus_rate=bonus*115
    rate3=bonus_rate+800
if wed<=8:
    rate4=wed*100
else:
    bonus=wed-8
    bonus_rate=bonus*115
    rate4=bonus_rate+800
if thu<=8:
    rate5=thu*100
else:
    bonus=thu-8
    bonus_rate=bonus*115
    rate5=bonus_rate+800
if fri<=8:
    rate6=fri*100
else:
    bonus=fri-8
    bonus_rate=bonus*115
    rate6=bonus_rate+800
total_rate=rate1+rate2+rate3+rate4+rate5+rate6+rate7
print(total_rate)
    
