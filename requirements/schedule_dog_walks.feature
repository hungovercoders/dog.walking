Feature: Schedule dog walks

  As a dog walker
  I want to be able to schedule a dog walk associated with a dog profile to my account
  The dog walk should include the date and time to start and the duration of the walk
  I want to be able to reschedule a dog walk if it is already scheduled
  I also want to be able to cancel a scheduled walk if one is already scheduled
  So that I can manage my dog walking schedule effectively

  Scenario: Schedule a new dog walk
    Given I am logged in as a "Dog Walker"
    And I have an existing dog profile for "Buddy"
    When I navigate to the "Schedule Walk" page
    And I select the date "2023-12-20"
    And I select the time "10:00 AM"
    And I set the duration to "30 minutes"
    And I click the "Schedule Walk" button
    Then I should see the scheduled walk for "Buddy" listed on my schedule

  Scenario: Reschedule an existing dog walk
    Given I am logged in as a "Dog Walker"
    And I have an existing scheduled walk for "Buddy" on "2023-12-20" at "10:00 AM"
    When I navigate to the "Edit Walk" page for the scheduled walk
    And I change the date to "2023-12-21"
    And I change the time to "11:00 AM"
    And I change the duration to "45 minutes"
    And I click the "Save Changes" button
    Then I should see the updated walk for "Buddy" listed on my schedule with the new date and time

  Scenario: Cancel a scheduled dog walk
    Given I am logged in as a "Dog Walker"
    And I have an existing scheduled walk for "Buddy" on "2023-12-20" at "10:00 AM"
    When I navigate to the "Walk Details" page for the scheduled walk
    And I click the "Cancel Walk" button
    And I confirm the cancellation
    Then I should no longer see the scheduled walk for "Buddy" listed on my schedule

  Scenario: View full schedule of walks
    Given I am logged in as a "Dog Walker"
    And I have scheduled walks for multiple dogs
    When I navigate to the "My Schedule" page
    Then I should see a list of all scheduled walks with details including dog name, date, time, and duration