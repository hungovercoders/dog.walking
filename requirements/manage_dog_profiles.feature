Feature: Manage dog profiles

  As a dog walker
  I want to be able to add a dog to my account and set its name, breed, profile image, and details
  Or I want to update an existing dog's name, breed, profile image, and details
  Or I want to remove a dog
  So that I can manage the dogs associated with my account

  Scenario: Add a new dog profile
    Given I am logged in as a "Dog Owner" or "Dog Walker"
    When I navigate to the "Add Dog" page
    And I enter the dog's name "Buddy"
    And I select the dog's breed "Golden Retriever"
    And I upload a profile image "buddy.jpg"
    And I fill in additional details "Friendly and energetic"
    And I click the "Save" button
    Then I should see the new dog profile listed with the name "Buddy"

  Scenario: Update an existing dog profile
    Given I am logged in as a "Dog Owner" or "Dog Walker"
    And I have an existing dog profile for "Buddy"
    When I navigate to the "Edit Dog" page for "Buddy"
    And I update the dog's name to "Buddy Jr."
    And I change the dog's breed to "Labrador Retriever"
    And I upload a new profile image "buddy_jr.jpg"
    And I update additional details to "Playful and loves swimming"
    And I click the "Save" button
    Then I should see the updated dog profile listed with the name "Buddy Jr."

  Scenario: Remove a dog profile
    Given I am logged in as a "Dog Owner" or "Dog Walker"
    And I have an existing dog profile for "Buddy Jr."
    When I navigate to the "Dog Profile" page for "Buddy Jr."
    And I click the "Delete" button
    And I confirm the deletion
    Then I should no longer see "Buddy Jr." listed in my dog profiles

Scenario: View all available dogs
    Given I am logged in as a "Dog Walker"
    And I have multiple dogs
    When I navigate to the "My Dogs" page
    Then I should see a list of all the dogs associated with my account