import json
import os
# this is where data persistence happens
# this class handles all the file operations
class GymManager:
    def __init__(self):
        self.filename = 'members.json'
        self.all_members = self._load_data()
        # Changed default extension to .json
        

    def _load_data(self):
        """Helper method to read the JSON file and return a list."""
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, ValueError):
            return []

    def _save_data(self, data):
        """Helper method to write the entire list to the JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

    def is_id_unique(self, target_id):
        """Checks if the ID already exists in the JSON data."""
        data = self._load_data()
        for member in data:
            if member.get('member_id') == target_id:
                return False
        return True

    def save_new_member(self, member):
        """Saves a member object as a dictionary in the JSON list."""
        if not self.is_id_unique(member.get_member_id()):
            print(f"\nError: Member ID {member.get_member_id()} already exists!")
            return False

        data = self._load_data()
        
        # Convert the object into a dictionary for JSON storage
        member_dict = {
            "member_id": member.get_member_id(),
            "first_name": member.get_first_name(),
            "last_name": member.get_last_name(),
            "age": member.get_age(),
            "branch": member.get_branch(),  # New Branch field
            "member_type": member.member_type,
            "discount_rate": member.calculate_discount()
        }
        
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
        
        for m in data:
            if m.get('member_id') == target_id:
                m['first_name'] = new_first
                m['last_name'] = new_last
                m['age'] = new_age
                found = True
                break
        
        if found:
            self._save_data(data)
        return found
    def view_all_members(self):
        """Loads all members from JSON and prints them in a readable format."""
        data = self._load_data()
        
        if not data:
            print("\n--- No members found in the database. ---")
            return

        print("\n" + "="*70)
        print(f"{'ID':<6} {'Name':<20} {'Age':<5} {'Branch':<15} {'Type':<10}")
        print("-" * 70)
        
        for member in data:
            full_name = f"{member.get('first_name')} {member.get('last_name')}"
            m_id = member.get('member_id')
            age = member.get('age')
            branch = member.get('branch', 'N/A')
            m_type = member.get('member_type', 'Regular')
            
            print(f"{m_id:<6} {full_name:<20} {age:<5} {branch:<15} {m_type:<10}")