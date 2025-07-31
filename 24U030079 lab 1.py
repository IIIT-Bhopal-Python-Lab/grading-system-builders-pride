while True: #countinuously take input from user till exit.
    user_input = input("Enter marks obtained or exit to terminate :") #Taking input from user
    if user_input=="exit": #User can exit the program by typing 'exit'
        print("program terminated.") #Exiting the program
        break
    else:  #If input is not exit.
        try:   
            marks = int(user_input) #Typecast input to integer
            #Check if marks are within the valid range
            if marks < 0 or marks > 100:
                print("Invalid input.")
            elif marks >= 90:
                print("obtained Grade: A")
            elif marks >= 75:
                print("obtained Grade: B")
            elif marks >= 60:
                print("obtained Grade: C")
            elif marks >= 40:
                print("obtained Grade: D")
            
            else:
                print("obtained Grade: F")
        except ValueError: #if input is neither an integer nor 'exit'.
            print("Invalid input.") #error message.