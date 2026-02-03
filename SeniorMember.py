from Member import Member
class SeniorMember(Member):
    def __init__(self, first_name, last_name, age, member_id, branch):
        # super init is used to call the parent class constructor
        super().__init__(first_name, last_name, age, member_id, branch)
        self.member_type = "Senior"
    # method to calculate discount for senior members
    def calculate_discount(self):
        # this polymorphism method returns a higher discount rate for senior members
        return 0.30  # 30% discount for senior members
    def get_details(self):
        # this super calls the parent class get_details method
        super().get_details()
        # override the get_details method to include member type
        print(f"Member Type: {self.member_type}")