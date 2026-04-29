Feature: Google Search
  As a user
  I want to search for "<Search>" on Google
  So that I can see the search results page

  Scenario Outline: Searching of ITESO in Google and verify careers
    Given I am on the Google homepage
    When I search for "<Search>"
    And I open the first results
    Then I should be on a page with domain "<domain>"
    When I search "<site_search>" in the current university site
    Then I should see results related to "<expected_text>"

  Examples:
    | Search | domain       | site_search | expected_text |
    | ITESO  | iteso.mx     | carreras    | carreras      |
    | ITESO  | iteso.mx     | becas       | becas         |
    | ITESO  | iteso.mx     | admisiones  | admisiones    |
    | CUCEI  | cucei.udg.mx | carreras    | licenciatura  |
    | CUCEI  | cucei.udg.mx | posgrados   | posgrados     |
    | UVM    | uvm.mx       | carreras    | profesional   |
    | UVM    | uvm.mx       | becas       | becas         |
