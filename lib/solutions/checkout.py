import itertools
import re

def isdirty(s):
   return True if re.search("[^A-D]") else False;

def clean(s):
   return re.sub("[^A-D]", "")


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

  if isdirty(skus):
      
  offers = { 'A': [(3, 139)], 'B': [(2, 45)]}
  costs = { 'A': 50, 'B': 30, 'C': 20, 'D': 15 }
  a_skus = sorted(skus.split(''))

  val = 0
  for k, g in a_skus.groupby(a_skus)  # identity lambda as def
      count = len(list(g))
      # consider offers first
      if k in offers
          # hmm, possible multiple offers.. order.. best val..
          for o in p_offers = of
          while count > 

      val += (count * costs[k])

