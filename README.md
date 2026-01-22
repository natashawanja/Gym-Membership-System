# Gym-Membership-System
## This program moves Diikochii Gym from paper records to a digital Python-based system. It helps the gym manager organize members across three branches (Kileleshwa, Westlands, and Parklands) without losing documents
Key Features

Full CRUD Support: The admin can Create new members, Read data from a members.json file, Update names or ages, and Delete members using a unique 4-digit ID.
+2


Member Types: Supports Regular, Student, Senior, and Corporate memberships with built-in age validation.


Automated Discounts: Calculates discounts automatically: Seniors (30%), Corporate (25%), and Students (15%)

Technical Setup

OOP Structure: Uses Inheritance so all members share a base "Member" class, and Encapsulation to keep personal info like names and IDs private.


Smart Logic: Uses a GymManager "logic engine" to handle all file operations and business rules.