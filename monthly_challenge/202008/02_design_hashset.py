class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.members = [0 for i in range(1_000_001)]

    def add(self, key: int) -> None:
        self.members[key] = 1
        

    def remove(self, key: int) -> None:
        self.members[key] = 0

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.members[key]
