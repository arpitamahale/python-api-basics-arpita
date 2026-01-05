"""
Part 2: Status Codes and JSON Parsing
=====================================
Difficulty: Beginner+

Learn:
- Understanding HTTP status codes
- Parsing JSON data like a Python dictionary
- Accessing specific fields from API response
"""

import requests

print("=== Understanding Status Codes ===\n")

# Example 1: Successful request (200 OK)
print("--- Example 1: Valid Request ---")
url_valid = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url_valid)

print(f"URL: {url_valid}")
print(f"Status Code: {response.status_code}")
print(f"Success? {response.status_code == 200}")


# Example 2: Not Found (404)
print("\n--- Example 2: Invalid Request (404) ---")
url_invalid = "https://jsonplaceholder.typicode.com/posts/99999"
response_404 = requests.get(url_invalid)

print(f"URL: {url_invalid}")
print(f"Status Code: {response_404.status_code}")
print(f"Found? {response_404.status_code == 200}")


# Example 3: Parsing JSON Data
print("\n--- Example 3: Parsing JSON ---")
url = "https://jsonplaceholder.typicode.com/users/5"
response = requests.get(url)

# Convert response to Python dictionary
data = response.json()

# Access specific fields
print(f"Full Name: {data['name']}")
print(f"Username: {data['username']}")
print(f"Email: {data['email']}")
print(f"City: {data['address']['city']}")
print(f"Company: {data['company']['name']}")


# Example 4: Working with a list of items
print("\n--- Example 4: List of Items ---")
url_list = "https://jsonplaceholder.typicode.com/posts?userId=1"
response = requests.get(url_list)
posts = response.json()

print(f"User 1 has {len(posts)} posts:")
for i, post in enumerate(posts[:3], 1):  # Show first 3
    print(f"  {i}. {post['title'][:40]}...")


# --- COMMON STATUS CODES ---
print("\n--- Common HTTP Status Codes ---")
status_codes = {
    200: "OK - Request successful",
    201: "Created - Resource created",
    400: "Bad Request - Invalid syntax",
    401: "Unauthorized - Authentication required",
    403: "Forbidden - Access denied",
    404: "Not Found - Resource doesn't exist",
    500: "Internal Server Error - Server problem"
}

for code, meaning in status_codes.items():
    print(f"  {code}: {meaning}")


# --- EXERCISES ---
#
# Exercise 1: Fetch user with ID 5 and print their phone number
#             URL: https://jsonplaceholder.typicode.com/users/5
#
# Exercise 2: Check if a resource exists before printing data
#             if response.status_code == 200:
#                 print(data)
#             else:
#                 print("Resource not found!")
#
# Exercise 3: Count how many comments are on post ID 1
#             URL: https://jsonplaceholder.typicode.com/posts/1/comments


print("=== EXERCISE SOLUTIONS ===\n")

# ================================
# Exercise 1:
# Fetch user with ID 5 and print their phone number
# URL: https://jsonplaceholder.typicode.com/users/5

print("--- Exercise 1: User 5 Phone Number ---")
url_user5 = "https://jsonplaceholder.typicode.com/users/5"
response_user5 = requests.get(url_user5)

if response_user5.status_code == 200:
    data_user5 = response_user5.json()
    print(f"User 5 Name: {data_user5['name']}")
    print(f"Phone Number: {data_user5['phone']}")
else:
    print("User not found!")
    

# ================================
# Exercise 2:
# Check if resource exists before printing data

print("\n--- Exercise 2: Check Resource Existence ---")
url_check = "https://jsonplaceholder.typicode.com/posts/12345"  # A post that does NOT exist
response_check = requests.get(url_check)

if response_check.status_code == 200:
    print("Data found!")
    print(response_check.json())
else:
    print("Resource not found! (Status:", response_check.status_code, ")")

    
# ================================
# Exercise 3:
# Count how many comments are on post ID 1
# URL: https://jsonplaceholder.typicode.com/posts/1/comments

print("\n--- Exercise 3: Count Comments on Post 1 ---")
url_comments = "https://jsonplaceholder.typicode.com/posts/1/comments"
response_comments = requests.get(url_comments)

if response_comments.status_code == 200:
    comments = response_comments.json()
    print(f"Total Comments on Post 1: {len(comments)}")

    # Show first 2 comments (optional)
    print("\nFirst 2 Comments:")
    for c in comments[:2]:
        print(f"- {c['name']} ({c['email']})")
else:
    print("Could not fetch comments!")

print("\n=== END OF EXERCISES ===")
