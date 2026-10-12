from datetime import datetime
time = datetime.now()
print(time)

print("Welcome to your expense tracker!" "\n This one go help you track and manage how you take dey spend your funds because e get where you go put money wey you dey collect, Wetin you spend am on, How much you don spend so far and how much remain..." "\n Use am... It's for your good!")
start = input("Enter y to continue: ")
while start.lower() != "y":
    start = input("Type y brr: ")
options = ["Add expense", "Add Income", "View Balance", "Summary by category", "Exit"]
categories = ["Transport", "Food", "Data", "Rent", "Other"]
Income_amount = 0
Total_expenses = 0
Food_total = 0
Transport_total = 0
Data_total = 0
Rent_total = 0
other_total = 0
while True:
    print("Oya." "\n Now wetin you wan do: ")
    for index,option in enumerate(options, start=1):
        print(f"{index}  {option}")

    choice = int(input("Choose an option (1-5): "))    
    if choice == 1:
        print(f"Expense \nChoose one below") 
        for index,category in enumerate(categories, start=1):
            print(f"{index}  {category}")
        selected_category = int(input("Choose an option (1-5): "))
        if selected_category == 1:
            print("You chose Transport")
            amount_for_transport = int(input("Enter amount: "))
            while amount_for_transport <= 0:
                print("Amount must be greater than zero!")
                amount_for_transport = int(input("Enter amount: "))
            Total_expenses += amount_for_transport
            Transport_total += amount_for_transport
            description_for_transport = str(input("Add description: "))
            print(f"Amount: ₦{amount_for_transport:,}\nDescription: {description_for_transport}") 
            print("Expense added successfully!")
        elif selected_category == 2:
            print("You chose Food")
            amount_for_food = int(input("Enter amount: "))
            while amount_for_food <= 0:
                print("Amount must be greater than zero!")
                amount_for_food = int(input("Enter amount: "))
            Total_expenses += amount_for_food
            Food_total += amount_for_food
            description_for_food = str(input("Add description: "))
            print(f"Amount: ₦{amount_for_food:,}\nDescription: {description_for_food}")
            print("Expense added successfully!")
        elif selected_category == 3:
            print("You chose Data")
            amount_for_data = int(input("Enter amount: "))
            while amount_for_data <= 0:
                print("Amount must be greater than zero!")
                amount_for_data = int(input("Enter amount: "))
            Total_expenses += amount_for_data
            Data_total += amount_for_data
            description_for_data = str(input("Add description: "))
            print(f"Amount: ₦{amount_for_data:,}\nDescription: {description_for_data}")
            print("Expense added successfully!")
        elif selected_category == 4:
            print("You chose Rent")
            amount_for_rent = int(input("Enter amount: "))
            while amount_for_rent <= 0:
                print("Amount must be greater than zero!")
                amount_for_rent = int(input("Enter amount: "))
            Total_expenses += amount_for_rent
            Rent_total += amount_for_rent
            description_for_rent = str(input("Add description: "))
            print(f"Amount: ₦{amount_for_rent:,}\nDescription: {description_for_rent}")
            print("Expense added successfully!")
        elif selected_category == 5:
            print("You chose Other")
            amount_for_other = int(input("Enter amount: "))
            while amount_for_other <= 0:
               print("Amount must be greater than zero!") 
               amount_for_other = int(input("Enter amount: "))
            Total_expenses += amount_for_other
            other_total += amount_for_other
            description_for_other = str(input("Add description: "))
            print(f"Amount: ₦{amount_for_other:,}\nDescription: {description_for_other}")
            print("Expense added successfully!")
            break

    elif choice == 2:
        print("Income")
        Income_amount = int(input("How much you earn: "))
        while Income_amount <= 0:
            print("Amount must be greater than zero!")
            Income_amount = int(input("How much you earn: "))
        print(f"₦{Income_amount:,} saved to your balance!")

    elif choice == 3:
        print("Balance")
        balance = Income_amount - Total_expenses

        print(f"You earned ₦{Income_amount:,}\nYou have spent ₦{Total_expenses:,} out of it\nSo now you have {balance}")
        
    elif choice == 4:
        print("Summary by category\nChoose Category")
        for index,category in enumerate(categories,start=1):
            print(f"{index}  {category}")
        selected_category = int(input("Choose from 1-5: "))
        if selected_category == 1:
            print(f"From ₦{Income_amount:,}, You spent ₦{Transport_total:,} on Transport")
        elif selected_category == 2:
            print(f"From ₦{Income_amount:,}, You have spent ₦{Food_total} on Food")
        elif selected_category == 3:
            print(f"From ₦{Income_amount:,}, You have spent ₦{Data_total} on Data")
        elif selected_category == 4:
            print(f"From ₦{Income_amount:,}, You have spent ₦{Rent_total} on Rent")
        elif selected_category == 5:
            print(f"From ₦{Income_amount:,}, You have spent ₦{other_total} on Other functionaries")
            
        
        
        
    elif choice == 5:
        print("Thanks... You don track all your funds!")
        break
    else:
        print("Enter a valid number!")

    


        

        