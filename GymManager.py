import json
import os
from StudentMember import StudentMember
from CorporateMember import CorporateMember
# this is where data persistence happens
# this class handles all the file operations
class GymManager:
    def __init__(self):
        self.filename = 'members.json'
        self.all_members = self._load_data()
        # Changed default extension to .json
        

    # this is a helper method to load data from the JSON file
    def _load_data(self):
        """Helper method to read the JSON file and return a list."""
        if not os.path.exists(self.filename):
            return []
        try:
            # this will read the entire JSON file and return a list of dictionaries
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, ValueError):
            return []

    def _save_data(self, data):
        """Helper method to write the entire list to the JSON file."""
        # this will overwrite the entire JSON file with the new data
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    def is_id_unique(self, target_id):
        """Checks if the ID already exists in the JSON data."""
        data = self._load_data()
        for member in data:
            if member.get('member_id') == target_id:
                return False
        return True

    def save_new_member(self, member, overwrite=False):
        """Saves member, with an option to overwrite existing ID for updates."""
        data = self._load_data()
        
        if overwrite:
            # Remove the existing entry to avoid duplicates during update
            data = [m for m in data if m.get('member_id') != member.get_member_id()]
        else:
            if not self.is_id_unique(member.get_member_id()):
                print(f"\nError: Member ID {member.get_member_id()} already exists!")
                return False

        # Prepare base dictionary
        member_dict = {
            'first_name': member.get_first_name(),
            'last_name': member.get_last_name(),
            'age': member.get_age(),
            'member_id': member.get_member_id(),
            'branch': member.get_branch(),
            'member_type': member.member_type
        }
        
        # Add subclass specific attributes
        if isinstance(member, StudentMember):
            member_dict['institution'] = member.get_institution()
        elif isinstance(member, CorporateMember):
            member_dict['company'] = member.get_company()
        # this appends the new member dictionary to the list
        data.append(member_dict)
        self._save_data(data)
        return True

    def delete_member(self, target_id):
        """Removes a member from the JSON list by ID."""
        data = self._load_data()
        initial_length = len(data)
        
        # Keep all members EXCEPT the one with the target_id
        data = [m for m in data if m.get('member_id') != target_id]
        
        if len(data) < initial_length:
            self._save_data(data)
            return True
        return False

    def update_member(self, target_id, new_first, new_last, new_age):
        """Updates specific fields in the JSON dictionary."""
        data = self._load_data()
        found = False
        # this loops through the list to find the member by ID
        for m in data:
            if m.get('member_id') == target_id:
                m['first_name'] = new_first
                m['last_name'] = new_last
                m['age'] = new_age
                found = True
                break
        # this saves the updated list back to the JSON file
        if found:
            self._save_data(data)
        return found
    def view_all_members(self):
        """Loads all members from JSON and prints them in a readable format."""
        data = self._load_data()
        
        if not data:
            print("\n--- No members found in the database. ---")
            return
        # this is the header for the table
        print("\n" + "="*70)
        # this is the title for the table
        print(f"{'ID':<6} {'Name':<20} {'Age':<5} {'Branch':<15} {'Type':<10}")
        # this is the separator line
        print("-" * 70)
        
        # this loops through each member and prints their details
        for member in data:
            full_name = f"{member.get('first_name')} {member.get('last_name')}"
            m_id = member.get('member_id')
            age = member.get('age')
            branch = member.get('branch', 'N/A')
            m_type = member.get('member_type', 'Regular')
            
            print(f"{m_id:<6} {full_name:<20} {age:<5} {branch:<15} {m_type:<10}")