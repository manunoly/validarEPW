__author__ = 'manuel'
from itertools import takewhile, product
import sys
import datetime

print(type(datetime.date(2012,12,12)))
exit()

print(sys.path)
exit()
nums = {55:1, 11:1}
print(nums.get(4))

exit()
print(list(takewhile(lambda x: x % 2 != 0,nums)))
exit()
print(nums)
exit()
def decor(func):
  def wrap():
    print("============")
    func()
    print("============")
  return wrap

def print_text():
  print("Hello world!")

decorated = decor(print_text)
decorated()
exit()
if all([i>5 for i in nums]):
    print("All OK")
else: print("No all comply")

if any([i % 2 == 0 for i in nums]):
    print("one exist that can by divided by 0")

for v, b in enumerate(nums):
   print(v, b)