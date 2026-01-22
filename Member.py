from abc import ABC, abstractmethod
# This the Parent Class, and ABC is imported to make it an Abstract Base Class
class Member(ABC):
    def __init__(self, first_name, last_name, age, member_id, branch):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__member_id = member_id
        self.__branch = branch
        self.__base_fee = 50.0

    # GETTERS
    def get_first_name(self): 
        return self.__first_name
    def get_last_name(self): 
        return self.__last_name
    def get_age(self): 
        return self.__age
    def get_member_id(self): 
        return self.__member_id
    def get_branch(self): 
        return self.__branch
    def get_base_fee(self): 
        return self.__base_fee

    # SETTERS (These must take a 'value' argument to work)
    def set_first_name(self, first_name): 
        self.__first_name = first_name
    def set_last_name(self, last_name): 
        self.__last_name = last_name
    def set_age(self, age): 
        self.__age = age

    @abstractmethod
    def calculate_discount(self):
        pass
    
    def get_details(self):
        print(f"Member ID: {self.get_member_id()}") 
        print(f"Name: {self.__first_name} {self.__last_name}")
        print(f"Branch: {self.get_branch()}")
        print(f"Age: {self.get_age()}")