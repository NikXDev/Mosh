u_input = " "
start_value = True
stop_value = True

while True:
    u_input = input("> ")
    if u_input.lower() == "help":
        print("start - to start car \nstop - to stop car \nquit - to exit")

    elif u_input.lower() == "start":
        if start_value:
            print("Car Started")
            start_value = False
        else:
            print("Its already started u dick..!")

    elif u_input.lower() == "stop":
        stop_value = True
        if start_value:
            if stop_value:
                print("Car Stopped")
                stop_value = False
            start_value = False
        else:
            print("WTF...its already at halt..!")

    elif u_input.lower() == "quit":
        break

    else:
        print("Invalid Input")


#errors are between start stop values..Fix it!