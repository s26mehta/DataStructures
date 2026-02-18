"""
Robinhood Interview:
    Given an input of prices and relevant timestamp in sorted order
    print out the following for each interval {start_time, first_price, last_price, max_price, min_price}

    If there is an interval with no price, use the prev interval's last price for all the prices
    If there is no previous interval, skip the interval
"""


import math
class TimeInterval:
    def __init__(self, start_time, first_price, last_price, max_price, min_price):
        self.start_time = start_time
        self.first_price = first_price
        self.last_price = last_price
        self.max_price = max_price
        self.min_price = min_price

def solution(prices_to_parse):
    # Please write your code here.
    intervals = prices_to_parse.split(",")

    time_intervals = [] # [[10, 3,3,3,3]]

    max_interval_size = 10
    next_interval_close = 10 # 20

    for interval in intervals:
        price, timestamp = interval.split(":")
        price = int(price)
        timestamp = int(timestamp)

        if len(time_intervals) == 0 or timestamp >= next_interval_close:
            while len(time_intervals) != 0 and timestamp >= next_interval_close + max_interval_size:
                last_interval_last_price = time_intervals[-1].last_price
                time_intervals.append(
                    TimeInterval(
                        next_interval_close, 
                        last_interval_last_price,
                        last_interval_last_price,
                        last_interval_last_price,
                        last_interval_last_price
                    )
                )
                next_interval_close += max_interval_size
            new_time_interval = TimeInterval(
                start_time=next_interval_close,
                first_price=price,
                last_price=price,
                max_price=price,
                min_price=price
            )
            next_interval_close += max_interval_size
            time_intervals.append(new_time_interval)
        else:
            existing_interval = time_intervals[-1]
            existing_interval.last_price = price
            existing_interval.max_price = max(existing_interval.max_price, price)
            existing_interval.min_price = min(existing_interval.min_price, price)
        
    result = []
    for interval in time_intervals:
        result.append("{%s,%s,%s,%s,%s}" % (interval.start_time, interval.first_price, interval.last_price, interval.max_price, interval.min_price))
    
    return "".join(result)

prices_to_parse = "3:12,1:15,4:18,1:30,5:40,9:47,2:101,6:103,5:105,3:107,5:108,8:120,9:121,7:122,9:124,3:125,2:126,3:127,8:128,4:129"
print(solution(prices_to_parse))



import math
def sol(prices_to_parse):
    data = {}

    intervals = prices_to_parse.split(",")
    max_interval = 0

    for interval in intervals:
        price, timestamp = interval.split(":")
        price = int(price)
        timestamp = int(timestamp)

        start_timestamp = math.floor(timestamp/10) *10
        end_timestamp = math.ceil(timestamp/10) *10 - 1 if timestamp != start_timestamp else start_timestamp+9

        if (start_timestamp, end_timestamp) not in data:
            data[(start_timestamp, end_timestamp)] = TimeInterval(start_timestamp, price, price, price, price)
        else:
            existing_interval = data[(start_timestamp, end_timestamp)]
            existing_interval.last_price = price
            existing_interval.max_price = max(existing_interval.max_price, price)
            existing_interval.min_price = min(existing_interval.min_price, price)
            
        max_interval = start_timestamp

    cur_interval = 0
    interval_size = 9
    
    result = []
    while cur_interval <= max_interval:
        if (cur_interval, cur_interval+interval_size) in data:
            interval = data[(cur_interval, cur_interval+interval_size)]
            result.append(interval)

        else:
            if len(result) != 0:
                last_interval_last_price = result[-1].last_price
                result.append(TimeInterval(cur_interval, last_interval_last_price, last_interval_last_price, last_interval_last_price, last_interval_last_price))
        cur_interval += interval_size + 1

    output = []
    for i in result:
        output.append("{%s,%s,%s,%s,%s}" % (i.start_time, i.first_price, i.last_price, i.max_price, i.min_price))

    
    return "".join(output)

prices_to_parse = "3:12,1:15,4:18,1:30,5:40,9:47,2:101,6:103,5:105,3:107,5:108,8:120,9:121,7:122,9:124,3:125,2:126,3:127,8:128,4:129"
print(sol(prices_to_parse))