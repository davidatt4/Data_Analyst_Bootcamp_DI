# Managing a Simple User Database

# Scenario:
# You're building a basic user management system that interacts with a PostgreSQL database. 
# Users should be able to:

# View all existing users.
# Add a new user.
# Update a user's information.
# Delete a user.

# Tasks:
# Database Setup:

# Create a PostgreSQL database named user_management.
# Inside the database, create a table named users with columns: 
# id (integer, primary key), username (varchar), email (varchar), and age (integer).

# Python Script:

# Write a Python script that connects to the user_management database.
# Implement functions to perform the following operations:
# View all users from the users table.
# Add a new user to the users table.
# Update a user's information based on their id.
# Delete a user from the users table based on their id.

# User Interaction:

# Create a simple command-line interface (CLI) to interact with your Python functions.
# The CLI should provide options to view, add, update, or delete users, 
# and take appropriate inputs from the user to perform these actions.

# Testing:

# Test your Python script by adding users, viewing all users, 
# updating user information, and deleting users.