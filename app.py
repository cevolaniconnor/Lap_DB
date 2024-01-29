import functions
import add 

def main():
    while True:
        print("\n1. Retrieve Laptime Data")
        print("2. See manufacturers")
        print("3. Add Car Record")
        print("4. Exit")
        
        choice = input("Enter your choice (1, 2, 3, or 4): ")

        if choice == "1":
            functions.retrieve_laptime_data()
        elif choice == "2":
            functions.retrieve_manu_data()
        elif choice == "3":
            add.insert_car()  
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()