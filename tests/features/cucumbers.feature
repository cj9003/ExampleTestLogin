Feature: Cucumber Basket
As a gardener,
I want to carry cucumbers in a BasketSo that i don't drop them all.

  Scenario: Add cucumbers to a Basket
    Given the basket has 2 cucumbers
    When 4 cucumbers are added to the basket
    Then the basket contains 6 cucumbers
