'''
/**
 * Problem Description
 * 
 * As a backend engineer building a scalable API platform, you need to implement a simple
 * rate limiter for a critical endpoint. The rule is:
 *    A user (identified by their unique user_id) is allowed a maximum of R
 *    requests within any rolling $T$ second window.
 * 
 * Write a function, isRequestAllowed(user_id, R, T), that takes the user ID,
 * the maximum requests allowed (R), and the time window in seconds (T), and
 * returns true if the request should be processed, or false if it should be
 * blocked due to rate limiting.
 * 
 * You can assume you have access to a function that returns the current time
 * in milliseconds, e.g., Date.now().
 * 
 * Constraints and Considerations
 *  - The function should be called for every incoming API request.
 *  - The system must track the request timestamps for potentially millions of users.
 *    Efficiency is key.
 * 
 * Example
 * Let R=3 requests and T=60 seconds.
 * 
 * | Current Time (ms) | user_id | isRequestAllowed Output |
 * | 1000              | U1      | true                    |
 * | 10000             | U1      | true                    |
 * | 20000             | U1      | true                    |
 * | 30000             | U1      | false                   |
 * | 60000             | U2      | true                    |
 * | 60500             | U1      | false                   |
 * | 61001             | U1      | true                    |
 */


user_id = 1
t = 60
r = 3
[1000, 100000]


'''

import time
from collections import deque
class Solution:
  def __init__(self):
    self.users = {} 

  def get_current_time(self):
    return time.time()

  def isRequestAllowed(self, user_id, R, T):
    if user_id not in self.users:
      self.users[user_id] = deque()

    if len(self.users[user_id]) < R:
      self.users[user_id].appendleft(self.get_current_time())
      return True
    else:
      q = self.users[user_id]
      cur_time = self.get_current_time()
      while q and q[-1] <= cur_time - T:
        q.pop()
        if len(q) < R:
          break
      
      if len(q) < R:
        q.appendleft(cur_time)
        return True
      else:
        return False
      
      
sol = Solution()
user1 = 'U1'
R = 3
T = 6 # input was incorrect - we didn't need to multiply this because time is epoch time
print(sol.isRequestAllowed(user1, R, T))
print(sol.users)
time.sleep(1)
print(sol.isRequestAllowed(user1, R, T))
print(sol.users)
time.sleep(1)
print(sol.isRequestAllowed(user1, R, T))
print(sol.users)
time.sleep(1)
print(sol.isRequestAllowed(user1, R, T))
print(sol.users)
print(sol.isRequestAllowed(user1, R, T))
print(sol.users)
print(sol.isRequestAllowed(user1, R, T))
print(sol.users)
print(sol.isRequestAllowed(user1, R, T))
print(sol.users)
time.sleep(3)
print(sol.isRequestAllowed(user1, R, T))
print(sol.users)








