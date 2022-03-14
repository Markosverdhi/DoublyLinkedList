class Node(object):
  """Doubly linked node which stores an object"""

  def __init__(self, element, next_node=None, previous_node=None):
    # The underscores are to prevent overwriting the variables if inherited
    self.__element = element
    self.__next_node = next_node
    self.__previous_node = previous_node

  def get_element(self):
    """Returns the element stored in this node"""
    return self.__element

  def get_previous(self):
    """Returns the previous linked node"""
    return self.__previous_node

  def get_next(self):
    """Returns the next linked node"""
    return self.__next_node

  def set_element(self, element):
    """Sets the element stored in this node"""
    self.__element = element

  def set_previous(self, previous_node):
    """Sets the previous linked node"""
    self.__previous_node = previous_node

  def set_next(self, next_node):
    """Sets the next linked node"""
    self.__next_node = next_node

class DoublyLinkedList(object):
  def __init__(self):
    self.__size = 0
    self.__header = Node('Header')
    self.__trailer = Node('Trailer')
    self.__header.set_next(self.__trailer)
    self.__trailer.set_previous(self.__header)
    self.__current = None

  def __iter__(self):
    self.__current = self.__header
    return self

  def __next__(self):
    if self.__current == None:
      self.__current = self.__header
    next = self.__current.get_next()
    if next == self.__trailer:
      raise StopIteration
    self.__current = next
    return next

  def map(self, function):
    current = self.get_first()
    while current != self.__trailer:
      current.set_element(function(current.get_element()))
      current = current.get_next()


  def size(self):
      return self.__size

  def is_empty(self):
      return self.__size == 0

  def get_first(self):
      return self.__header.get_next()

  def get_last(self):
      return self.__trailer.get_previous()

  def get_previous(self, node):
      return node.get_previous()

  def get_next(self, node):
      return node.get_next()

  def add_before(self, new, existing):
    existing.get_previous().set_next(new)
    new.set_previous(existing.get_previous())
    new.set_next(existing)
    existing.set_previous(new)
    self.__size += 1


  def add_after(self, new, existing):
    existing.get_next().set_previous(new)
    new.set_next(existing.get_next())
    new.set_previous(existing)
    existing.set_next(new)
    self.__size += 1

  def add_first(self, new):
    new.set_previous(self.__header)
    self.__header.get_next().set_previous(new)
    new.set_next(self.__header.get_next())
    self.__header.set_next(new)
    self.__size += 1

  def add_last(self, new):
    new.set_next(self.__trailer)
    self.__trailer.get_previous().set_next(new)
    new.set_previous(self.__trailer.get_previous())
    self.__trailer.set_previous(new)
    self.__size += 1

  def remove(self, node):
    node.get_previous().set_next(node.get_next())
    node.get_next().set_previous(node.get_previous())
    self.__size -= 1
