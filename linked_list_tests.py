# An AnyList is a:
# - None is Empty
# - Pair(first,rest)

class Pair:
   def __init__(self,first,rest):
      self.first = first # first is any value
      self.rest = rest # rest is an AnyList

   def __repr__(self):
      return 'Pair({}, {})'.format(self.first,self.rest)

   def __eq__(self,other):
      return type(other) == Pair and self.first == other.first and self.rest == other.rest

# empty_list : 
# Returns an empty list.
def empty_list():
   return None

# add : LinkedList int val count -> LinkedList
# Returns a list containing a value at the indicated location.
def add(lst,index,value,count=0):
   if index < 0:
      raise IndexError()
   if count == index:
      if lst == None:
         return Pair(value, None)
      else:
         return Pair(value, Pair(lst.first,lst.rest))
   elif count != index and lst == None:
      raise IndexError()
   else:
      return Pair(lst.first, add(lst.rest, index, value, count+1))

# length : LinkedList -> int
# Returns length of list.
def length(lst):
   if lst == None:
      return 0
   else:
      return 1 + length(lst.rest)

# get : LinkedList int -> val
# Returns the value at specified index.
def get(lst, index):
   if lst == None:
      raise IndexError()
   if index < 0:
      raise IndexError()
   if index == 0:
      return lst.first
   else:
      return get(lst.rest, index-1)

# set : LinkedList int value -> LinkedList
# Returns a list with a value replacing the previous value at a specified index.
def set(lst,index,value,acc=0):
   if index >= length(lst)+acc or index < 0:
      raise IndexError()
   elif acc != index:
      return Pair(lst.first,set(lst.rest,index,value,acc+1))
   else:
      return Pair(value, lst.rest)

# remove : LinkedList int int -> LinkedList
# Returns a list with the value removed at a specified index.
def remove(lst,index,count=0):
   if index < 0 or lst == None or index < count:
      raise IndexError()
   elif index == count:
      return (lst.first, lst.rest)
   else:
      return (remove(lst.rest, index, count + 1)[0],Pair(lst.first,remove(lst.rest, index, count+1)[1]))


# foreach : LinkedList func -> None
# Applies function to list iteratively.
def foreach(lst,func):
   if lst:
      func(lst.first)
      foreach(lst.rest,func)
   return None

# str_list : LinkedList -> None
# Prints values of list as a str representation.
def str_list(lst):
   if lst:
      print(str(lst.first))
      str_list(lst.rest)
   return None
