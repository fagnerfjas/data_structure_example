
import unittest
from data_structure.ArrayList import *

class TestStringMethods(unittest.TestCase):
	
	def setUp(self):
		self.list1 = ArrayList(5)
		self.list2 = ArrayList()
		self.list3 = ArrayList(5)

	def test_initial(self):
		self.assertListEqual( self.list1.a_list, [None, None, None, None, None] )
		self.assertEqual(0, self.list1.size)
		self.assertEqual(5, self.list1.capacity)
		self.assertEqual(0, self.list2.size)
		self.assertEqual(10, self.list2.capacity)
		n = 0
		for i in range(15): 
			if(n < self.list2.capacity):
				self.assertTrue( self.list2.add(i) ) 
			else:
				self.assertFalse( self.list2.add(i) ) 
			n+=1
		self.assertEqual(10, self.list2.size)

	def test_shift(self):
		for i in range(3):
			self.list1.add(i)
		self.assertListEqual(self.list1.a_list, [0, 1, 2, None, None])
		self.assertTrue( self.list1.rightShift() )
		self.assertListEqual(self.list1.a_list, [None, 0, 1, 2, None])
		self.assertTrue( self.list1.rightShift(3) )
		self.assertListEqual(self.list1.a_list, [None, 0, 1, None, 2])
		self.assertFalse( self.list1.rightShift(4) )

	def test_insertIn(self):
		self.assertTrue(self.list3.addIn('first', 2))
		self.assertListEqual(self.list3.a_list, [None, None, 'first', None, None])
		self.assertTrue(self.list3.addIn('second', 1))
		self.assertListEqual(self.list3.a_list, [None, 'second', 'first', None, None])
		self.assertTrue(self.list3.addIn('third'))
		self.assertListEqual(self.list3.a_list, ['third', 'second', 'first', None, None])
		self.assertTrue(self.list3.addIn('fourth', 2))
		self.assertListEqual(self.list3.a_list, ['third', 'second', 'fourth', 'first', None])
		self.assertTrue(self.list3.addIn('last'))
		self.assertListEqual(self.list3.a_list, ['last', 'third', 'second', 'fourth', 'first'])
		self.assertFalse(self.list3.addIn('error'))
		self.assertListEqual(self.list3.a_list, ['last', 'third', 'second', 'fourth', 'first'])

	def test_set(self):
		self.assertTrue( self.list3.set(2, 'new Second') )
		self.assertListEqual(self.list3.a_list, [None, None, 'new Second', None, None])
		self.assertTrue(self.list3.set(2, 'removed'))
		self.assertListEqual(self.list3.a_list, [None, None, 'removed', None, None])
		self.assertTrue(self.list3.set(4, 'new element'))
		self.assertListEqual(self.list3.a_list, [None, None, 'removed', None, 'new element'])
		
	def test_remove(self): 

	
if __name__ == '__main__':
	unittest.main()	