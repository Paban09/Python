start=0
stop=0
command=""
print("Start the car Game")
while True:
    command=input('> ').lower()
    if command == 'start':
        if start==0:
            print ('the car has started' )
            start=+1
            stop=0
        else:
            print("The car is already Started" )

    elif command == 'stop':
        if stop == 0:
            print('the car has stopped')
            start = 0
            stop = +1
        else:
            print("The car is already Stopped" )
    elif command == 'quit':
        print('Game over')
        break
    else:
        print("Invalid command")
print("Come back later")