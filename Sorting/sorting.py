class Sorting:
    def selectionSort(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]

        return arr

    def bubbleSort(self, arr):
        for i in range(len(arr)):
            for j in range(1, len(arr) - i):
                if arr[j - 1] > arr[j]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]

        return arr

    def insertionSort(self, arr):
        for i in range(len(arr)):
            j = i
            while j > 0 and arr[j - 1] > arr[j]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1

        return arr

    def mergeSort(self, arr):
        self.ms(arr, 0, len(arr) - 1)
        return arr

    def ms(self, arr, left, right):
        if left >= right:
            return

        mid = (left + right) // 2
        self.ms(arr, left, mid)
        self.ms(arr, mid + 1, right)
        self.merge(arr, left, mid, right)

        return arr

    def merge(self, arr, left, mid, right):
        temp = []
        i, j = left, mid + 1

        while i <= mid and j <= right:
            if arr[i] < arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1

        while i <= mid:
            temp.append(arr[i])
            i += 1

        while j <= right:
            temp.append(arr[i])
            i += 1

        for x in range(left, right + 1):
            arr[x] = temp[x - left]

    def quickSort(self, arr):
        self.qs(arr, 0, len(arr) - 1)
        return arr

    def qs(self, arr, left, right):
        if left < right:
            partition_elem = self.partition(arr, left, right)
            self.qs(arr, left, partition_elem - 1)
            self.qs(arr, partition_elem + 1, right)

        return arr

    def partition(self, arr, left, right):
        pivot = arr[left]
        i = left
        j = right

        while i < j:
            while arr[i] <= pivot and i <= right - 1:
                i += 1
            while arr[j] > pivot and j >= left + 1:
                j -= 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[left], arr[j] = arr[j], arr[left]

        return j


s = Sorting()

print("Original Array is: [5, 3, 4, 2, 2, 1]")
print("Selection Sort -> ", s.selectionSort([5, 3, 4, 2, 2, 1]))
print("Bubble Sort -> ", s.bubbleSort([5, 3, 4, 2, 2, 1]))
print("Insertion Sort -> ", s.insertionSort([5, 3, 4, 2, 2, 1]))
print("Merge Sort -> ", s.mergeSort([5, 3, 4, 2, 2, 1]))
print("Quick Sort -> ", s.quickSort([5, 3, 4, 2, 2, 1]))
