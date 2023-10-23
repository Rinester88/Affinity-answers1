#!/usr/bin/env python
# coding: utf-8

# ## Address Validation
# 
# This notebook provides a solution to validate addresses based on their PIN code and post office branch name using the provided APIs. The objective is to ensure the correctness of the address details.
# 

# ## Required Libraries
# 
# - `requests`: To make HTTP requests to the APIs.
# - `re`: To perform regular expression operations for pattern matching.
# 

# ## Address Validation Function
# 
# The `validate_address` function performs the following steps:
# 
# 1. Extracts the PIN code from the address.
# 2. Validates the PIN code using the API.
# 3. Extracts potential post office names from the address.
# 4. Validates each potential post office name using the API.
# 5. Confirms the details (district, state, and city) from the API match the provided address.
# 
# Let's define the function:
# 

# - `def validate_address(address)`
# 

# ## Conclusion
# 
# The notebook showcases how to validate addresses using specific criteria and APIs. It's essential to ensure the accuracy of addresses, especially for applications like courier delivery, to prevent misdeliveries and maintain efficiency.
# 

# ### program that takes as input a free flowing address and checking if the PIN code indeed corresponds to the address mentioned.
# 
# ####  List of test cases that I used to test your program
# `Address: 2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050
# Result: Correct address.`
# 
# `Address: 2nd Phase, 374/B, 80 Feet Rd, Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050
# Result: Invalid Post Office name or the provided details don't match.`
# 
# `Address: 374/B, 80 Feet Rd, State Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bangalore. 560050
# Result: Invalid Post Office name or the provided details don't match.`
# 
# `Address: 2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560095
# Result: Correct address.`
# 
# `Address: Colony, Bengaluru, Karnataka 560050
# Result: Invalid Post Office name or the provided details don't match.`
# 
# `Address: UG Flr, The Destination Centre, Magarpatta, Hadapsar,Pune,Maharashtra 411028
# Result: Correct address.`

# In[16]:


import requests  # This module allows us to make HTTP requests. We're using it to interact with the API.
import re # This stands for Regular Expressions, a module that provides support to search for and manipulate strings based on patterns.

def validate_address(address): #  validate an address by checking both its PIN code and post office name against data from the provided APIs
    address_lower = address.lower()

    # Extract the PIN code from the address using regular expressions
    pincode_matches = re.findall(r'\b\d{6}\b', address) # regular expression (\b\d{6}\b), we search for a 6-digit number that represents the PIN code in the address.
    if not pincode_matches:
        return False, "No PIN code found in the address."

    pincode = pincode_matches[0]
    pin_url = f"https://api.postalpincode.in/pincode/{pincode}"

    # Fetch the address details using the provided API for the given PIN code
    pin_response = requests.get(pin_url) # Using requests.get(), we fetch data for that PIN code.
    pin_data = pin_response.json()

    if pin_data[0].get("Status") != "Success":
        return False, "Invalid PIN code."

    # Extract potential post office names from the address
    post_office_names = [word for word in re.findall(r'\b\w{4,}\b', address) if word not in pincode]

    post_office_valid = False
    for post_office_name in post_office_names:
        branch_url = f"https://api.postalpincode.in/postoffice/{post_office_name}"
        branch_response = requests.get(branch_url)
        branch_data = branch_response.json()

        if branch_data[0].get("Status") == "Success":
            post_office_data = branch_data[0].get("PostOffice", [])
            
            for post_office in post_office_data:
                district = post_office.get("District", "").lower()
                state = post_office.get("State", "").lower()
                city = post_office.get("Name", "").lower()

                if district in address_lower and state in address_lower and city in address_lower:
                    post_office_valid = True
                    break

            if post_office_valid:
                break

    if not post_office_valid:
        return False, "Invalid Post Office name or the provided details don't match."

    return True, "Correct address."

# Testing the function
addresses = [
    "2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050",
    "2nd Phase, 374/B, 80 Feet Rd, Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050",
    "374/B, 80 Feet Rd, State Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bangalore. 560050",
    "2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560095",
    "Colony, Bengaluru, Karnataka 560050",
    "UG Flr, The Destination Centre, Magarpatta, Hadapsar,Pune,Maharashtra 411028"
]

for address in addresses:
    result, message = validate_address(address)
    print(f"Address: {address}\nResult: {message}\n")


# ## why i used python programming for above code ?
# 
# - `Ease of Use:` Python's concise and clear syntax allows for rapid development and prototyping of solutions. The programme you asked involves string manipulation, API calls, and JSON handling, which are all simple in Python.
# 
# - `Libraries and Frameworks:` Python has a thriving library ecosystem. We used the requests package, which facilitates making HTTP requests, for the task at hand. There is almost always a Python library for almost any task you can think of, reducing the need to create everything from scratch.
# 
# - `Handling JSON Data:` The API you described returns data in JSON format. Python includes JSON support, making it simple to parse and extract information.
# 
# - `String Manipulation:` Python includes sophisticated string manipulation capabilities out of the box, which was critical for extracting PIN codes and checking address components.
# 
# - `Popularity and Community Support:` Python's popularity and community support mean that if you run into problems or need assistance with certain tasks, there are plenty of resources available. This improves the efficiency of troubleshooting and learning.
# 
# - `Cross-Platform:` Because Python is platform-independent, the code can run on a variety of operating systems without modification. This is useful if the solution must be deployed in several settings.
