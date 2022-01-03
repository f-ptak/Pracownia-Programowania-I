class Arrays():

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
    
    @staticmethod
    def print_in_row(array):
        for r in array:
            if r == array[-1]:
                print(f"{r}")
            else:
                print(f"{r},",end="")
            
my_array = [4,1,8,7,2]
print("Print in column:")
Arrays.print_in_col(my_array)
print("\nPrint in row:")
Arrays.print_in_row(my_array)