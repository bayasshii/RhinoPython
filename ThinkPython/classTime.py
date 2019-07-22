import datetime

class Time:
    """
    """
    def __int__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return (seconds)
        

    
time = Time()
time.hour = 11
time.minute = 59
time. second = 5

def print_time(time):
    """
    receives:
        time   class object
    works:
        print time (hour,minute,second)
    return:
        None
    """
    hh = "%.2d" % time.hour
    mm = "%.2d" % time.minute
    ss = "%.2d" % time.second
    hh_mm_ss = "%s:%s:%s" % (hh, mm, ss)
    print(hh_mm_ss)
    # print(hour,minute,second)

t1 = Time()
t1.hour = 1
t1.minute = 30
t1.second = 3

t2 = Time()
t2.hour = 7
t2.minute = 30
t2.second = 3


def is_after(t1,t2):
    """
    receives:
        t1,t2   class objects
    works:
        judge whether t1 is later than t2.
        if t1 is later than t2, print "True".
        if not, print "Fause".
    return:
        None
    """
    a = (t1.hour)*3600 + (t1.minute)*60 + (t1.second)
    b = (t2.hour)*3600 + (t2.minute)*60 + (t2.second)
    print( a > b )


def increment(time,seconds):
    """
    receives:
        time      class object
        second    second > 0
    works:
        add second to time.
    return:
        None
    """
    time.second += seconds
    if time.second >= 60:
        s = time.second // 60
        time.second -= 60*s
        time.minute += s
    if time.minute >= 60:
        m = time.minute // 60
        time.minute -= 60*m
        time.hour += m

def weekday(day):
    week = ["月","火","水","木","金","土","日"]
    wd = day.weekday()
    print(week[wd] + "曜")

def birthday(your_birthday):
    now = datetime.datetime.now()
    delta = now - your_birthday
    how_old =  delta.days//366
    how_long = datetime.timedelta(days = (how_old+1)*366) - delta
    hour, l_seconds = divmod(how_long.seconds,3600)
    minute, second = divmod(l_seconds, 60)
    print("わたしは%s歳！！" % (how_old), "わたしの誕生日まであと{0}日と{1}時間{2}分{3}秒だよーん！！".format(how_long.days, hour, minute, second))

your_birthday = datetime.datetime(1997, 2, 11, 11, 15, 30, 2000)
#birthday(your_birthday)


def twice(day1,day2):
    """
    receives:
        day1,day2      two birthday (person who was bone in day1 is older.)
    works:
        curicurate twice day ! 
    return:
        None
    """
    delta = day2 - day1
    d_years, d_days = divmod(delta.days*2, 366)
    
    twice_day =  day1 + datetime.timedelta(days = d_days)
    twice_year = day1.year + d_years
    
    print(twice_year, twice_day.month, twice_day.day)

day1 = datetime.date(1997, 5, 11)
day2 = datetime.date(2007, 5, 15)

#twice(day1,day2)

def n_times(day1,day2,n):
    """
    receives:
        day1,day2      two birthday (person who was bone in day1 is older.)
    works:
        curicurate n times day ! 
    return:
        None
    """
    delta = (day2 - day1)/(n-1)
    d_years, d_days = divmod(delta.days, 365)
    
    twice_day =  day2 + datetime.timedelta(days = d_days)
    twice_year = day2.year + d_years
    
    print(twice_year, twice_day.month, twice_day.day)

n_times(day1, day2, 4)
