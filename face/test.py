def option():
    print("welcome to the first option for the system")
    
def next():
    print ("this is the next one")
    
def another():
    print ("heres another")

def option_select():
    #1.give options
    print("welcome to the application")
    done = 0

    while done == 0:
        #2.read options
        print("hello word")
        select = input("what do you want to do")

        #3.open selected subsystem
        if select == 1:
            option()

        if select == 2:
            next()

        while done == 1:
            results = input("is that all you want to do?")
            #4.reset or close#
            if results == "yes":
                done = 1

            elif results == "no":
                done = 0
    
            else:
                print ("you have not entered a valid response")
            
            
        if done == 1:
            print("this should be working")