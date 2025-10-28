# KH 2nd lists notes

#import random

#names = [ "alex", "ken","hi", "test"]

#print(names)
#print(names[3])

#names[-1] = "Xavier"
#names.extend(["wus53w","4q3waytf"])
#print(names)

#x = names.index("alex")
#print(x)

board = [[1,2,3],
         [4,5,6],
         [7,8,9]]
board[1][1] = "X"
print(board)
from colorama import Fore, Style

print(Fore.RED + "This text is red." + Style.RESET_ALL)