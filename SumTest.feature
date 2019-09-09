# file:features/tutorial03_step_parameters.feature
Feature: Step Parameters (tutorial03)

  Scenario: Sum
    Given I insert number 1 and number 2
    When  I perform the sum
    Then  it should print the correct sum
