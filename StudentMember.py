from Member import Member
class StudentMember(Member):
    def __init__(self, first_name, last_name, age, member_id, institution, branch):
        # super init is used to call the parent class constructor
        super().__init__(first_name, last_name, age, member_id, branch)
        self.member_type = "Student"
        self.__institution = institution
    # getter for institution
    def get_institution(self):
        return self.__institution
    # setter for institution
    def set_institution(self, institution):
        self.__institution = institution
    # method to calculate discount for student members
    def calculate_discount(self):
        # this polymorphism method returns a discount rate for student members
        return 0.15  # 15% discount for student members
    def get_details(self):
        # this super calls the parent class get_details method
        super().get_details()
        # override the get_details method to include member type and institution
        print(f"Member Type: {self.member_type}")
        print(f"Institution: {self.get_institution()}")