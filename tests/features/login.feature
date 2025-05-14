Feature: login

  Scenario Outline: Login to the application
    Given Open the login page
    When I enter <user> and <passw>
    Then I should be redirected to the dashboard

    Examples:
      | user    | passw       |
      | student | Password123 |
      | user2   | pass2       |
      | ""      | ""          |
      | student | pass3       |
      | user2   | Password123 |
