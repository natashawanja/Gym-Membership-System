from Member import Member
class CorporateMember(Member):
    def __init__(self, first_name, last_name, age, member_id, company, branch):
        # super init is used to call the parent class constructor
        super().__init__(first_name, last_name, age, member_id, branch)
        self.member_type = "Corporate"
        self.__company = company
    # getter for company
    def get_company(self):
        return self.__company
    # setter for company
    def set_company(self, company):
        self.__company = company
    # method to calculate discount for corporate members
    def calculate_discount(self):
        # this polymorphism method returns a discount rate for corporate members
        return 0.25  # 25% discount for corporate members
    def get_details(self):
        # this super calls the parent class get_details method
        super().get_details()
        # override the get_details method to include member type and company
        print(f"Member Type: {self.member_type}")
        print(f"Company: {self.get_company()}")