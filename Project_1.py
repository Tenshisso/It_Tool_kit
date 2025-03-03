#Angel Castillo
#00339250
#CIS-153-O1A
#Project 1
#IT Tool Kit


#FUNCTION for help desk option 1
def help_desk():

    print("\nIs your computer turned on? (y/n)")
    answer=input()

#first if statement to check the first question, if true the function ends, false continues to next question.
    if(answer=='n'):
        print("Please turn on the computer and reach out if you continue to have issues. The process is complete")
    else:
        print("Great! Let's check your network connection. Are you able to connect to the Internet? (y/n)")
        answer=input()


#second if statement inside else to check next question, if true the function ends, false continues to next question.
        if(answer=='n'):
            print("Please restart your modem and router and reach out if you continue to have issues. The process is complete")
        else:
            print("Let's check the software? Is a specific software application causing issues? (y/n)")
            answer=input()


#last if statement also inside the second else, the program ends no matter false or true, but the line print is different.
            if(answer=='n'):
                print("Sorry but we will have to escalate this issue to our software team. We will call you back, goodbye. The process is complete")
            else:
                print("Please restart application and reach out if you continue to have issues. The process is complete")



#FUNCTION for Data Center Temparature Checker. Option 2
def data_center_temp_check(temp,unit):

#if statement to check what unit we are using and two more if statements to check the temperature for each unit case.
    if(unit=='f'):
        if(temp<59):
            print("WARNING. TOO COLD FOR THE DATA CENTER!!")
        elif(temp>89.6):
            print("WARNING. TOO HOT FOR THE DATA CENTER")
        else:
            print("The temprature on the Data Center is within safe limits:", temp,"F")

    else:
        if(temp<15):
            print("WARNING. TOO COLD FOR THE DATA CENTER!!")
        elif(temp>32):
            print("WARNING. TOO HOT FOR THE DATA CENTER!!")
        else:
            print("The temperature on the Data Center is within safe limits:", temp,"C")



#FUNCTION to check network capabilities. option 3.
def network_speed_test(mbps):

#multiple if statements to check for the different speed ranges.
    if(mbps>=5) or (mbps < 5):
        print("Basic browsing, Email.\n")
    if(mbps>5):
        print("SD video streaming.\n")
    if(mbps>=10):
        print("HD video streaming, Moderate online gaming.\n")
    if(mbps>=25):
        print("4K video streaming, High-quality online gaming.\n")
    if(mbps>=50):
        print("Multiple HD/4K streams, Heavy online gaming, Large file downloads.\n")
    if(mbps>=100):
        print("High-end online gaming, large data transfers, High-demand applications.\n")
    if(mbps>=500):
        print("Extensive online gaming, Large network of devices.\n")


#FUNCTION to calculate IT equipment cost. option 4
def it_equipment_cost_calculator(cost,unit):
    total=cost*unit
    return total


#FUNCTION for the equipment report. option 5
def it_equipment_report():

#varaible to keep track of the total sum of all equipments.
    final_total=0

    for i in range(3):
        print("Enter the name of the equipment: ")
        equipment=input()
        print()

        print("Enter the cost of the equipment: ")
        cost=int(input())
        print()

        print("Enter the quantity of units: ")
        units=int(input())
        print()

        total=it_equipment_cost_calculator(cost,units)
        final_total+=total

        print("                    It Equipment Report          \n"
        "\n NAME         |       COST       |       UNITS        |     TOTAL\n"
        ,equipment,"            $",cost,"               ",units,"              $",total,'\n')


    print("                    Total cost for all equipment                \n"
          "                  $",final_total,"             "    )



#FUNCTION goodbye, to exit the program. option 6
def goodbye():
    print("Thank you. GoodBye.")



#menu function to print and select options. (set parameter to none to handle case where no argument is provided.)
def menu(option=None):
    print("1. Help Desk Query Generator.\n"
          "2. Data Center Temperature Checker.\n"
          "3. Network Speed Tester.\n"
          "4. IT Equipment Cost Calculator.\n"
          "5. IT Equipment Report.\n"
          "6. Exit.")


    if(option==1):
        print()
        help_desk()

    if(option==2):
        print()
        print("What unit temperature do you want to use?")
        unit=input()

        print("What is the temperature? ")
        temp=int(input())
        print()
        data_center_temp_check(temp,unit)

    if(option==3):
        print()
        print("What is the speed of your internet in mbps?")
        speed=int(input())
        print()
        network_speed_test(speed)

    if(option==4):
        print()
        print("Enter the name of the equipment: ")
        name=input()

        print("Enter the cost of the equipmenbt: ")
        cost=int(input())

        print("Enter the quantity of units: ")
        units=int(input())

        print()
        print("Your total is ", it_equipment_cost_calculator(cost,units))

    if(option==5):
        print()
        it_equipment_report()



#main function of the program
def main():
    print("\nIT Tool Kit Version 4.0\n"
          "Please Enter Your Name: ")

    name=input()
    print("\nWelcome", name, "how can we help you today?")

#loop to repeat the menu until the user selects option 6(function goodbye)
    while True:
        print()
        menu()

#added exception statement in case the user types a letter instead of an integer
#https://stackoverflow.com/questions/40184155/how-do-i-add-an-exception-for-invalid-input

        try:
            option = int(input())
            print()

        except ValueError:
            print("Not a valid selection.")
            break

        if(option>6) or (option<1):
            print("Not a valid selection.")
            break

#check for the option 6 here instead of inside menu function because can't use operator '>' with the parameter type none.
        elif(option==6):
            goodbye()
            break

        menu(option)

main()

