from Member import Member
class SeniorMember(Member):
    def __init__(self, first_name, last_name, age, member_id, branch):
        # call the constructor of the parent class
        super().__init__(first_name, last_name, age, member_id, branch)
        self.member_type = "Senior"
    # method to calculate discount for senior members
    def calculate_discount(self):
        # this polymorphism method returns a higher discount rate for senior members
        return 0.30  # 30% discount for senior members
    def get_details(self):
        # override the get_details method to include member type
        super().get_details()
        print(f"Member Type: {self.member_type}")