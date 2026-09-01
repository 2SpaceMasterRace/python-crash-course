# Python already implements dynamic array through lists so Stack is just a cheap wrapper
class Stack:
    def __init__(self) -> None:
        self.stack = []

    def insert(self, n: int) -> None:
        self.stack.append(n)

    def remove(self) -> None:
        self.stack.pop()


class Dynamic_array:
    def __init__(self, length: int, capacity: int) -> None:
        self.length: int = length
        self.capacity: int = capacity
        self.array: list[int] = [0] * 5  # default size

    def resize(self) -> None:
        self.capacity: int = 2 * self.capacity
        new_array: list[int] = [0] * self.capacity

        for index in range(self.length):
            new_array[index] = self.array[index]

        self.array = new_array

    def get(self, i: int) -> None:
        if i < self.length:
            return self.array[i]
        else:
            raise IndexError

    def push_back(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()

        self.array[self.length] = n
        self.length += 1

    def insert(self, i: int, n: int) -> None:
        if i < self.length:
            self.array[i] = n
            return
        else:
            raise IndexError

    def remove(self) -> None:
        if self.length > 0:
            self.length -= 1
        else:
            raise IndexError

    def print(self) -> None:
        for index in range(self.length):
            print(self.array[index])


class Fixed_Array:
    """
    array     : actual array
    n         : element to be inserted/deleted at the next open position in the array
    length    : number of real values in the array
    capacity  : size (memory allocated) for the fixed size array
    """

    def __init__(self, array: int, length: int, capacity: int) -> None:
        self.array = array
        self.length = length
        self.capacity = capacity

    def insert_end(self, n: int) -> None:
        if self.length < self.capacity:
            self.array[self.length]: int = n
        else:
            # Overflow, number of elements is greater than the given capacity of the array
            raise OverflowError

    def remove_end(self) -> None:
        # Sanity check to ensure the array is not empty (aka length = 0)
        # We reduce the length of array by 1 and replace the last element of the array with some default senital value, in this case 0
        if self.length > 0:
            self.array[self.length - 1]: int = 0
            self.length -= 1
        else:
            print("Underflow Error")

    def insert_middle(self, n: int, i: int) -> None:
        """
        TODO: try to make sense of how this works by visualizing properly
        """
        # Sanity checks to ensure array is not full and i is a valid index
        if self.length == self.capacity:
            raise Exception
        if type(i) is not int:
            raise TypeError
        elif i > self.length:
            raise Exception

        # Shift every index from the end to i to the right and then insert n into position i
        # Example, say length = 3, n = 4 and index = 2, iteration would look like:
        #               0           1         2
        #          --------------------------------
        #          |    1    |       2    |    3   |
        #          --------------------------------
        # for index in range(2, 1, -1): // 1 is not inclusive
        #       arr[2+1=3] = arr[2] // a[3] = a[2]
        # arr[2] = 4
        # new values = a[0] = 1, a[1] = 2, a[2] = 4, a[3] = 3
        for index in range(self.length - 1, i - 1, -1):
            self.array[index + 1] = self.array[index]

        self.array[i] = n

    def remove_middle(self, i: int) -> None:
        # Sanity Checks
        if self.length < 0:
            print("Underflow Error")
        if type(i) is not int:
            raise TypeError
        elif i > self.length:
            raise Exception

        # Shift elements left from ith position to the end
        for index in range(i + 1, self.length):
            self.array[index - 1] = self.array[index]

    def print_array(self) -> int:
        for index in range(self.capacity):
            print(self.array[index])


def main():
    print("Hello from arrays!")


if __name__ == "__main__":
    main()
