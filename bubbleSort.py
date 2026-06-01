class Bubble(object):
    def __init__(self,n:int):
        self.n:int  = n
        

    def bubbleSort(self,unSortedArraay:list) -> list:
        self.SortedArray:list = unSortedArraay

        for i in range(self.n - 1): #4. 0 to  2
            for j in range(self.n - i - 1): #0 to 4-0-1 = 3 // 1 to 4-1-1 = 2 // 2 to 4 -2 -1 = 1

                if self.SortedArray[j] > self.SortedArray[j+1]:
                    
                     self.SortedArray[j+1], self.SortedArray[j] = self.SortedArray[j], self.SortedArray[j+1]

                    #  temp:int = self.SortedArray[j]
                    #  self.SortedArray[j] = self.SortedArray[j+1]
                    #  self.SortedArray[j+1] = temp

        return self.SortedArray

def main() -> None:
     while True:

       choice:int = int(input('''
                               1.Enter the Nth term.
                               2.Enter the unsorted array.
                               3.Display the sorted array.
                               4.Exit.
                               Enter the choice..
                               '''))
   
       if choice == 1:
           n:int = int(input("Enter the value of N:"))
           obj:Bubble = Bubble(n)
       elif choice == 2:
           unSortedArray:list = []
   
           for i in range(n):
               unSortedArray.append(int(input(f'Enter the {i+1} value:')))

          
   
           result:list = obj.bubbleSort(unSortedArray)
       elif choice == 3:
          
           print('Sorted array:',result)
   
       elif choice == 4:
           exit()
   
       else:
          print("invalid choice..")
    







if __name__ == "__main__":
    main()
