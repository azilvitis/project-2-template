import unittest
from array_list import *

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
        a = List(3)
        a.val[0]=3
        a.val[1]=5
        a.val[2]=7
        a.size=3
        self.assertEqual(repr(a),'List([3, 5, 7],3,3)')

    def test_empty(self):
        self.assertEqual(empty_list(),List())

    def test_add(self):
         a = List(3)
         a.val[0]=3
         a.val[1]=5
         a.val[2]=7
         a.size=3
         b = List()
         b.val[0]=3
         b.val[1]=5
         b.val[2]=11
         b.val[3]=7
         b.size = 4
         self.assertEqual(add(a,2,11),b)
        
    def test_length(self):
        temp_list = List()
        self.assertEqual(length(temp_list),0)

    def test_length_2(self):
        temp_list = List(5)
        temp_list.val[0] = 1
        temp_list.val[1] = 2
        temp_list.size = 2
        self.assertEqual(length(temp_list),2)

    def test_get(self):
        temp_list = List(3)
        temp_list.val[0] = 1
        temp_list.val[1] = 2
        temp_list.size = 2
        self.assertEqual(get(temp_list,0),1)

    def test_set(self):
        temp_list = List(3)
        temp_list.val[0] = 1
        temp_list.val[1] = 2
        temp_list.val[2] = 3
        temp_list.size = 3
        b = List(10)
        b.val[0]=4
        b.val[1]=2
        b.val[2]=3
        b.size=3
        self.assertEqual(set(temp_list, 0, 4),b)
        
    def test_add_ex(self):
        l1 = List(4)
        l1.val = [0, 1, 2, 3]
        l1.size = 4
        l2 = add(l1, 2, 3)
        self.assertEqual(l2.val, [0, 1, 3, 2, 3, None, None, None, None, None])
    
    def test_remove_ex(self):
        l = List(3)
        l.val = [1, 2, 3]
        l.size = 3
        a = remove(l,1)
        s = (2, List([1, 3, None],2,3))
        #self.assertEqual(remove(l, 1), s)
        self.assertEqual(a,s)
        
    def test_set_ex(self):
        l1 = List(3)
        l1.val = [1, 2, 3]
        l1.size = 3
        l2 = set(l1, 1, 49)
        self.assertEqual(l2.val, [1, 49, 3, None, None, None, None, None, None, None])
        
    def test_add_err(self):
        with self.assertRaises(IndexError):
           b = List(3)
           b.val[0]=4
           b.val[1]=2
           b.val[2]=3
           b.size=3
           add(b,-1,4)

    def test_get_err(self):
        with self.assertRaises(IndexError):
           b = List(3)
           b.val[0]=4
           b.val[1]=2
           b.val[2]=3
           b.size=3
           get(b,-1)
            
    def test_set_err(self):
        with self.assertRaises(IndexError):
           b = List(3)
           b.val[0]=4
           b.val[1]=2
           b.val[2]=3
           b.size=3
           set(b,-1,3)
           
    def test_rem_err(self):
        with self.assertRaises(IndexError):
           b = List(3)
           b.val[0]=4
           b.val[1]=2
           b.val[2]=3
           b.size=3
           remove(b,4)
           
    def test_remove(self):
        a = List(3)
        a.val[0]=3
        a.val[1]=1
        a.size=2
        b = List(3)
        b.val[0]=3
        b.size=1
        self.assertEqual(remove(a,1),(1,b))

if __name__ == '__main__':
    unittest.main()
