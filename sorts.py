from abc import ABC, abstractmethod

class AbstractSortInterface(ABC):

    @abstractmethod
    def sort(self, arr):
        pass

class InsertionSort(AbstractSortInterface):
    # Compares adjacent elements and swaps them if they are in the wrong order
    # Complexity: O(n^2) in the worst case, O(n) in the best case
    # In place, stable, 
    def sort(self, array):
        self.arr = array
        for i in range(1, len(self.arr)):
            for j in range(i, 0, -1):
                if self.arr[j] < self.arr[j - 1]:
                    self.arr[j], self.arr[j - 1] = self.arr[j - 1], self.arr[j]
                else:
                    break
        return self.arr



test = InsertionSort()
print(test.sort([5, 2, 9, 1, 5, 6]))