# ArrayList is one of any:
# - val
# - size
# - capacity

class List:
   def __init__(self,capacity=10):
      self.val = [None] * capacity
      self.size = 0
      self.capacity = capacity
   def __repr__(self):
      return 'List({},{},{})'.format(self.val,self.size,self.capacity)
   def __eq__(self,other):
      return type(other) == List and self.val == other.val and self.size == other.size and self.capacity == other.capacity

# empty_list : -> List()
# Returns an empty list.
def empty_list():
   return List()

# add : ArrayList int value -> ArrayList
# Returns a list containing a value at the indicated loaction.
def add(lst,index,value):
   newlist = List()
   if index >= lst.size + 1 or index < 0:
      raise IndexError()
   if index == lst.capacity:
      newlist.capacity = lst.capacity * 2
   for i in range(0, index):
      newlist.val[i] = lst.val[i]
   newlist.val[index] = value
   for i in range(index, lst.size):
      newlist.val[i + 1] = lst.val[i]
   newlist.size = lst.size + 1
   return newlist

# length : ArrayList -> int
# Returns length of list.
def length(lst):
   return lst.size

# get : ArrayList index count -> val
# Returns the value at specified index.
def get(lst, index):
   if index >= lst.size or index < 0:
      raise IndexError()
   return lst.val[index]

# set : ArrayList index value -> ArrayList
# Returns a list with a value replacing the previous value at a specified index.
def set(lst,index,value):
   newlist = List()
   if index >= lst.size or index < 0:
      raise IndexError()
   for i in range(0, index):
      newlist.val[i] = lst.val[i]
   newlist.val[index] = value
   for i in range(index + 1, lst.size):
      newlist.val[i] = lst.val[i]
   newlist.size = lst.size
   return newlist

# remove : ArrayList index -> ArrayList
# Returns a list with the value removed at a specified index.
def remove(lst,index):
   if index < 0 or index >= lst.size:
      raise IndexError
   value = lst.val[index]
 
   for i in range (index+1, lst.size):
      lst.val[i-1]=lst.val[i]
   lst.val[lst.size - 1] = None
   lst.size -= 1
   return(value, lst)
