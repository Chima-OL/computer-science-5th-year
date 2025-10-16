# Lesson 2 - Strings
# Worksheet 4
# Problem: Create a username validator
# Requirements:
#
# Between 5-15 characters
# Only letters and numbers
# Must start with a letter
def username(name):
    if len(name) < 5 or len(name) > 15:
        return "Username must be 5-15 characters"
    if not name[0].isalpha():
        return "Username must start with a letter"
    if not name.isalnum():
        return "Username can only contain letters and numbers"
    
    return "Valid username!"

print(username("mincraft@?@"))