import Unittest
import * from Node
import * from DoublyLinkedList

Instance = DoublyLinkedList()
a = Node(1)
b = Node(3)
c = Node(2)
d = Node(4)
Instance.add_first(a)
Instance.add_after(b,a)
Instance.add_before(c,b)
Instance.add_last(d)
Instance.remove(d)

class TestDLL(unittest.TestCase):
  def test__iter__(self):
    self.assertEqual(print(Instance.__iter__), None) #I need clarification for the iterator tests
  
  def test__next__(self):
    self.assertEqual(Instance.__next__().get_element(), None)

  def test_map(self):
    self.assertListEqual(print(Instance.map(lambda x: x+1)), [2,3,4])

  def test_size(self):
    self.assertEqual(Instance.size(),3)

  def test_is_empty(self):
    self.assertFalse(Instance.is_empty())

  def test_get_first(self):
    self.assertEqual(print(Instance.get_first()),1)

  def test_get_last(self):
    self.assertEqual(print(Instance.get_first()),3)

  def test_get_previous(self):
    self.assertEqual(Instance.get_previous(c).get_element(),1)

  def test_get_next(self):
    self.assertEqual(Instance.get_next(c).get_element(),3)

if __name__ == '__main__':
  unittest.main()
