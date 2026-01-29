from GymManager import GymManager
from RegularMember import RegularMember
from StudentMember import StudentMember
from SeniorMember import SeniorMember
from CorporateMember import CorporateMember
# this is the console class that handles user interaction
class Console:
    # this initializes the console with a GymManager instance
    def __init__(self):
        # Initializing the logic engine
        self.manager = GymManager()
    # this is the main application loop
    def run_app(self):
        """Main menu loop to run the program."""
        while True:
            print("\n--- Diikochii Gym Management System ---")
            print("1. Register as a New Member")
            print("2. Update Existing Member")
            print("3. Delete Member")
            print("4. View All Members")
            print("5. Exit")
            choice = input("Select an option: ")
            
            if choice not in ['1', '2', '3', '4', '5']:
                print(f"{choice} is not a valid option. Please enter 1 - 5.")
                continue
            
            if choice == '1':
                self.register_member_ui()
            elif choice == '2':
                self.update_member_ui()
            elif choice == '3':
                self.delete_member_ui()
            elif choice == '4':
                self.manager.view_all_members()
            elif choice == '5':
                print("Exiting the Diikochii Gym Membership Management system. Goodbye!")
                break
    
    # this handles the registration user interface
    def register_member(self):
        """Handles the registration process and input validation."""
        # --- SUB-MENU VALIDATION ---
        while True:
            print("\n--- Select Membership Type ---")
            print("1. Regular Member")
            print("2. Student Member (16-25)")
            print("3. Senior Member (60+)")
            print("4. Corporate Member")
            sub_choice = input("Choice: ")
            
            if sub_choice in ['1', '2', '3', '4']:
                break
            else:
                print("Invalid selection! Please choose 1, 2, 3, or 4.")

        # 1. VALIDATE NAME
        while True:
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            if first_name.isalpha() and last_name.isalpha():
                break
            print("Invalid name. Please use alphabetic characters only.")

        # 2. VALIDATE AGE
        while True:
            try:
                age = int(input("Enter member age: "))
                if sub_choice == '2' and not (16 <= age <= 25):
                    print("Students must be between 16 and 25 years old.")
                    continue
                elif sub_choice == '3' and age < 60:
                    print("Seniors must be at least 60 years old.")
                    continue
                break
            except ValueError:
                print("Invalid age. Please enter a numeric value.")

        # 3. VALIDATE MEMBER ID
        while True:
            member_id = input("Enter 4 digit member ID: ")
            if len(member_id) == 4 and member_id.isdigit():
                if self.manager.is_id_unique(member_id):
                    break
                else:
                    print("This ID is already assigned to another member. Try again.")
            else:
                print("Invalid ID. Must be 4 digits.")

        # 4. BRANCH SELECTION MENU
        while True:
            print("\n--- Select Branch ---")
            print("1. Kileleshwa")
            print("2. Westlands")
            print("3. Parklands")
            branch_choice = input("Choice: ")
            if branch_choice == '1':
                branch = "Kileleshwa"
                break
            elif branch_choice == '2':
                branch = "Westlands"
                break
            elif branch_choice == '3':
                branch = "Parklands"
                break
            else:
                print("Invalid selection! Please choose 1, 2, or 3.")

        # 5. CREATE MEMBER OBJECT BASED ON TYPE
        if sub_choice == '1':
            new_member = RegularMember(first_name, last_name, age, member_id, branch)
        elif sub_choice == '2':
            inst = input("Enter institution: ")
            new_member = StudentMember(first_name, last_name, age, member_id, inst, branch)
        elif sub_choice == '3':
            new_member = SeniorMember(first_name, last_name, age, member_id, branch)
        elif sub_choice == '4':
            comp = input("Enter company: ")
            new_member = CorporateMember(first_name, last_name, age, member_id, comp, branch)

        # 6. SAVE TO JSON
        self.manager.save_new_member(new_member)
        print(f"Success! {first_name} {last_name} registered at {branch} branch.")
    # this handles the update user interface
    def update_member(self):
        """Handles the update process."""
        while True:
            target = input("Enter ID to update: ")
            if len(target) == 4 and target.isdigit():
                break
            print("Invalid ID. Must be exactly 4 digits.")
        
        if self.manager.is_id_unique(target):
            print("Error: Member ID not found")
            return

        while True:
            new_first = input("Enter new first name: ")
            new_last = input("Enter new last name: ")
            if new_first.isalpha() and new_last.isalpha():
                break
            else:
                print("Invalid name. Please use alphabetic characters only.")
            
        while True:
            try:
                new_age = int(input("Enter new age: "))
                break
            except ValueError:
                print("Invalid age. Please enter a number.")

        if self.manager.update_member(target, new_first, new_last, new_age):
            print(f"Successfully updated details for ID: {target}!")
        else:
            print("Update failed please try again")
    # this handles the deletion user interface
    def delete_member(self):
        """Handles the deletion process."""
        while True:
            target = input("Enter the 4-digit ID of the member to delete: ")
            if len(target) == 4 and target.isdigit():
                break
            print("Invalid ID. Must be exactly 4 digits.")

        if self.manager.delete_member(target):
            print("Successfully deleted!")
        else:
            print("Error: Member ID not found in the database.")