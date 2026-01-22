from Member import Member
class RegularMember(Member):
    def __init__(self, first_name, last_name, age, member_id, branch):
        # call the constructor of the parent class
        super().__init__(first_name, last_name, age, member_id, branch)
        self.member_type = "Regular"
    # method to calculate discount for regular members
    def calculate_discount(self):
        # this polymorphism method returns no discount for regular members
       return 0.0
    def get_details(self):
        # override the get_details method to include member type
        super().get_details()
        print(f"Member Type: {self.member_type}")