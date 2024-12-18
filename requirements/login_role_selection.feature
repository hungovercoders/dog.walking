Feature: Role selection during login

  Scenario: Log in and select "Dog Walker" role
    Given I am on the login page
    When I enter my username "john_doe" and password "password123"
    And I click the "Login" button
    Then I should see a prompt to select a role
    When I select the "Dog Walker" role
    Then I should be directed to the Dog Walker dashboard

  Scenario: Log in and select "Dog Owner" role
    Given I am on the login page
    When I enter my username "jane_smith" and password "mypassword"
    And I click the "Login" button
    Then I should see a prompt to select a role
    When I select the "Dog Owner" role
    Then I should be directed to the Dog Owner dashboard

  Scenario: Attempt to log in with invalid credentials
    Given I am on the login page
    When I enter my username "unknown_user" and password "wrongpassword"
    And I click the "Login" button
    Then I should see an error message "Invalid username or password"

  Scenario: Skip role selection after login
    Given I am on the login page
    When I enter my username "john_doe" and password "password123"
    And I click the "Login" button
    Then I should see a prompt to select a role
    When I do not select any role and try to proceed
    Then I should see an error message "Please select a role to continue"
