import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')

print("There's more code down here that will never get executed")
print("to prove that sys.exit() quits the program and not just the loop.")