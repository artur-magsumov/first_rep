import random
import datetime
import string

def random_date():
    stime = 1483228800
    etime = 1483228800+31535900
    ran_date = random.randint(stime, etime)

    date = datetime.datetime.fromtimestamp(ran_date).strftime('%d.%m.%Y')
    return date


a = random.randint(0, 1000000)
before = random.randint(0, 5)
after = random.randint(0, 3)
random1 = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation ) for _ in range(before)])
random3 = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation ) for _ in range(after)])
print(random)
##def random_ref():
##    
