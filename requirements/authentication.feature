Feature: Dog Walker Authentication and Role Management
  As a dog walker
  I want to log in and manage my account with a specific role
  So that I can use the application to manage my dog walking tasks

  Scenario: Dog walker logs into the application
    Given the dog walker has registered with a valid email and password
    When the dog walker logs in with valid credentials
    Then the dog walker is authenticated and granted access to their account

  Scenario: Dog walker role is assigned
    Given the dog walker is logged into the application
    When they access their account settings
    Then their role is displayed as "Dog Walker"