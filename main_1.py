try:
    class Cinema:

        global nr_of_tickets
        nr_of_tickets = []

        def __init__(self):

            print("Welcome".center(20,' '))
            self.rows = 0
            self.columns = 0
            a = True
            
            while(a):
                self.rows = input("Enter the number of rows: ")
                self.columns = input("Enter the number of seats in each row: ")
            
                if (self.rows  == '0') or (self.columns == '0'):
                    print("Enter a non zero number")

                elif self.rows.isdigit() == False or self.columns.isdigit() == False:
                    print("Please Enter numbers only!")
                
                else:
                    a = False
                
            self.rows = int(self.rows)
            self.columns = int(self.columns)
            print("")
            
            
            self.row_nr = []
            self.column_nr = []
            self.current_income = 0
            self.total_income = 0
            self.menu()
            self.details_list = []

        
        def menu(self):
            try:
                print("\n\nChoose one of the following options: ")
                print("1. Show the seats")
                print("2. Buy a ticket")
                print("3. Statistics")
                print("4. Show booked tickets user info")
                print("0. Exit")
                self.choice = int(input())
            except:
                print("Invalid ")

        
        def _seat_matrix(self):
            print("\t Cinema: \n")
            print('   ' + '  '.join(map(str,list(range(1,self.columns+1)))))
            print()
            for i in range(0, self.rows):
                    print(i+1, end = ' ')
                    for j in range(self.columns):
                        if ((i+1,j+1) in list(zip(self.row_nr,self.column_nr))):
                            print(" B ", end = '')
                        else:
                            print(" S ", end = '')
                    print("\n")
            
        def _book_tickets(self, nr_of_tickets): 
            try:
                for i in nr_of_tickets: 
                          
                    
                    row = input("Please enter row number " + str(i) + ": ")
                    column = input("Please enter column number " + str(i) + ": ")
                    x = True
                    while x:
                        if (row.isdigit() == False or column.isdigit() == False):
                            print("Please enter valid number")
                            row = input("Please enter row number " + str(i) + ": ")
                            column = input("Please enter column number f" + str(i) + ": ")

                        elif (int(row) > self.rows) or (int(row) < 1):
                            print("Row number does not exist!")
                            row = input("Please enter a row number between {} and {}: ".format(1, self.rows))

                        elif (int(column) > self.columns) or (int(column) < 1):
                            print("Invalid number")
                            column = input("Please enter a column number between {} and {}: ".format(1, self.columns))
                        else:
                            x = False
                            
                    row = int(row)
                    column = int(column)

                    
                    if (row, column) in list(zip(self.row_nr, self.column_nr)):         
                        print("Already Booked !Please try another seat!")
                        self._book_tickets([i])
                    else:
                        print("Price for ticket no {} is: ${}".format(i, self.ticket_price(row)))
                        if (input("Please enter 'Yes' if you would like to proceed to book the ticket!") in ['Yes','yes']):
                            self.row_nr.append(row)
                            self.column_nr.append(column) 
                            print("Great! Please enter your details ", i)
                            self._get_details()
                            print("Ticket No. {} has been booked!".format(str(i)))
                            print("-"*15)
                        else:
                            print("Thanks for visiting!")

            except:
                print("Invalid value...! Please try again with valid number")
                
        def _get_details(self):
            details = {}
            for i in ["Name", "Gender", "Age", "Phone Number"]:
                details[i] = input("Please enter your {}: ".format(i))

            for i in range(len(self.row_nr)):
                details["Row Number"] =self.row_nr[i]
                details["Column Number"] =self.column_nr[i]
                details["Ticket Price"] = "$" + str(self.ticket_price(self.row_nr[i]))

            
            self.details_list.append(details)

            print("Please check the details ")
            for i,j in details.items():
                print("{}: {}".format(i,j))


        def ticket_price(self, row_nr):
            if (self.columns * self.rows) < 60:
                return 10
            else:
                if (self.rows%2 != 0) and (row_nr <= self.rows//2):
                    return 10
                elif (self.rows % 2 != 0) and (row_nr > self.rows//2):
                    return 8
                elif (self.rows % 2 == 0) and (row_nr <= self.rows//2):
                    return 10
                elif (self.rows % 2 == 0) and (row_nr > self.rows//2):
                    return 8
                
        def _total_income(self):
            if (self.rows*self.columns) < 60:
                return self.rows*self.columns*10
            else:
                return (self.columns)*((self.rows-self.rows//2)*8 + ((self.rows//2)*10))
            
        
        def ShowSeats(self):      
            try:
                if len(self.row_nr) > 0:
                    print("\n\n")
                    self._seat_matrix()           
                else:
                    print("\n\n\n")
                    self._seat_matrix()
            except ValueError:
                print("You have to enter an integer value!")    
            
        def Tickets(self):   
            try:
                
                nr_of_tickets = [i+1 for i in range(int(input("How many tickets would you like to book?")))]
                if len(nr_of_tickets) > (self.columns * self.rows):
                    print("Out of range")
                    raise Exception()

                print("Please enter the row and column numbers for {} tickets below!".format(max(nr_of_tickets)))

                self._book_tickets(nr_of_tickets)
                print("Booked successfully!")
                print("-"*15)
                                  
                self._seat_matrix()
                
            except ValueError:
                print("Please enter a valid integer value between 1 and {} seats!".format(self.rows*self.columns))

        def Statistics(self):
            try:
                perc_of_tickets = round((len(self.row_nr)*100/(self.columns * self.rows)),2)

                for i in self.row_nr:
                    self.current_income += self.ticket_price(i)

                print("Number of purchased tickets: ",len(self.row_nr))
                print("Percentage of tickets booked: {}%".format(str(perc_of_tickets)))
                print("Current Income is: $", self.current_income)
                print("Total Income: $", self._total_income())
                print("-"*15)
            except ZeroDivisionError:
                print("\n\nSeems like you've not yet defined the theater and seats!")

        def User_info(self):
            try:
                if len(self.details_list) > 0:
                    row = int(input("Please enter Row Number: "))
                    column = int(input("Please enter Column Number: "))

                    for i in self.details_list:
                        if (i["Row Number"] == row) and (i["Column Number"] == column):
                            print("Your details!")
                            for (j,k) in i.items():
                                print("{}: {}".format(j,k))
                            break
                        else:
                            continue
                    else:
                        print("Haven't booked these tickets!")
                else:
                    print("No tickets have been booked yet!")
            except ValueError:
                print("Please enter a valid number!")
except:
    print("I'm sorry, something went wrong!")
    
try:
    obj = Cinema()

    while obj.choice != 0:
        if obj.choice == 1:
            obj.ShowSeats()
            obj.menu() 
        elif obj.choice == 2:
            obj.Tickets()
            obj.menu()
        elif obj.choice == 3:
            obj.Statistics()
            obj.menu()
        elif obj.choice == 4:
            obj.User_info()
            obj.menu()
        else:
            raise Exception()
except:
    print("Please make sure you've entered a correct option!")
    obj.menu()