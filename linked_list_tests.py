import unittest
from linked_list import *

class TestList(unittest.TestCase):
    # Note that this test doesn't assert anything! It just verifies your
    #  class and function definitions.
   def test_interface(self):
      temp_list = empty_list()
      temp_list = add(temp_list, 0, "Hello!")
      length(temp_list)
      get(temp_list, 0)
      temp_list = set(temp_list, 0, "Bye!")
      remove(temp_list, 0)
   def test_repr(self):
      t = Pair("Food", Pair(2, None))
      self.assertEqual(repr(t),'Pair(Food, Pair(2, None))')
   def test_mt(self):
      self.assertEqual(empty_list(),None)
   def test_add(self):
      temp_list = Pair("Food", Pair(2, None))
      self.assertEqual(add(temp_list,1,"Hi"), Pair("Food", Pair("Hi", Pair(2,None))))
   def test_add_2(self):
      temp_list = Pair(1, Pair(3, Pair("Here",None)))
      self.assertEqual(add(temp_list,0,2), Pair(2, Pair(1, Pair(3, Pair("Here",None)))))
   def test_add_none(self):
      temp_list = None
      self.assertEqual(add(temp_list,0,3),Pair(3, None))
   def test_length(self):
      temp_list = Pair("Food", Pair(2, None))
      self.assertEqual(length(temp_list), 2)
   def test_add_err(self):
      with self.assertRaises(IndexError):
         add(Pair("This", Pair("will", Pair("fail", None))), -1, "me")
   def test_add_err_2(self):
      with self.assertRaises(IndexError):
         add(None, -1, 2)
   def test_add_err_3(self):
      with self.assertRaises(IndexError):
         add(None, 3, 4)
   def test_add_err_4(self):
      with self.assertRaises(IndexError):
         add(Pair("Foof", Pair("LOOF",None)),3,5,7)
   def test_add_none_again(self):
      self.assertEqual(add(None,0,3), Pair(3, None))
   def test_get(self):
      temp_list = Pair("Food", Pair(2, None))
      self.assertEqual(get(temp_list, 1),2)
   def test_get_err(self):
      with self.assertRaises(IndexError):
      get(Pair("How",Pair("to",Pair("unnittest",Pair("errors",None)))), 7)
   def test_get_none(self):
      with self.assertRaises(IndexError):
      get(Pair("here", Pair("lies",None)), -1)
   def test_set(self):
      temp_list = Pair("Food", Pair(2, None))
      self.assertEqual(set(temp_list, 1, "Bye!"),Pair("Food",Pair("Bye!",None)))
   def test_set_err(self):
      with self.assertRaises(IndexError):
         set(Pair("Here",Pair("is",None)),-1,3)
   def test_rem_err(self):
      with self.assertRaises(IndexError):
         remove(Pair("Here",Pair("is",None)),-1)
   def test_set_0(self):
      temp_list = Pair(1,None)
      self.assertEqual(set(temp_list,0,2), Pair(2,None))
   def test_remove(self):
      temp_list = Pair("Food", Pair(2, None))
      self.assertEqual(remove(temp_list,1),(2,Pair("Food",None)))
   def test_remove_1(self):
      temp_list = Pair(1, Pair("Hey", Pair(4, None)))
      self.assertEqual(remove(temp_list,0),(1,Pair("Hey", Pair(4,None))))
   def test_remove_2(self):
      temp_list = Pair(1, Pair("Hey", Pair(4, None)))
      with self.assertRaises(IndexError):
      remove(temp_list,-1)
   def test_remove_3(self):
      temp_list = Pair(1, Pair("Bye", Pair(5, None)))
      self.assertEqual(remove(temp_list,2),(5,Pair(1,Pair("Bye",None))))
if __name__ == '__main__':
    unittest.main()
