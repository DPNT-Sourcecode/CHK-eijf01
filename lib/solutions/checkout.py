import itertools
import re

def isdirty(s):
   return True if re.search("[^A-D]", s) else False

def clean(s):
   return re.sub("[^A-D]", "")


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

  if isdirty(skus):
      return -1

  offers = { 'A': [(3, 139)], 'B': [(2, 45)]}
  costs = { 'A': 50, 'B': 30, 'C': 20, 'D': 15 }
  a_skus = sorted(skus.split(''))

  val = 0
  for k, g in a_skus.groupby(a_skus):  # identity lambda as def
      count = len(list(g))
      # consider offers first
      if k in offers:
          # hmm, possible multiple offers.. order.. best val..
          for quantity, cost in offers[k]:
              print("considering offer on %r, %d for %d" % (k, quantity, cost))
              while count > quanity:
                  val += cost
                  count -= quantity
      # single item cost
      val += (count * costs[k])
  return val
