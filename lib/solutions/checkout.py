from itertools import groupby
import re

def isdirty(s):
   return True if re.search("[^A-E]", s) else False

#def clean(s):
#   return re.sub("[^A-E]", "")


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

  if isdirty(skus):
      return -1

  offers = { 'A': [(3, 130, '')], 'B': [(2, 45, '')], 'E': [(2, 80, 'B')]}
  costs = { 'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40 }
  a_skus = sorted(list(skus))

  # group and count
  counts = {}
  for k, g in groupby(a_skus):  # identity lambda as def
      counts[k] = len(list(g))

  val = 0

  # consider offers first
  for k, count in counts.items():
      #print("considering %r, count %d" % (k, count))
      if k in offers:
          # hmm, possible multiple offers.. order.. best val..
          for quantity, cost, bogof in offers[k]:
              #print("considering offer on %r, %d for %d" % (k, quantity, cost))
              while count >= quantity:
                  #print("offer requirements met, %d for %d on %r" % (quantity, cost, k))
                  val += cost
                  count -= quantity
                  counts[k] -= quantity  # outer context
                  freebies = list(bogof)
                  if len(freebies) > 0:
                      # reduce count(s) for given items
                      for p in freebies:
                          counts[p] -= 1

  # single item costs only remain
  for k, count in counts.items():
      val += (count * costs[k])

  return val
