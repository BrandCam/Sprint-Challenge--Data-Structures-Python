class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if len(self.get()) == 5:
      self.storage[self.current] = item
      self.current += 1
    else:
      self.storage[0] = self.storage[1]
      self.storage[1] = self.storage[2]
      self.storage[2] = self.storage[3]
      self.storage[3] = self.storage[4]
      self.storage[4] = item

  def get(self):
    arr = []
    for item in self.storage:
      if item is not None:
        arr.append(item)
    return arr