
Feature: Extract 4 data files with the Anscombe Quartet format

Scenario: When executed, the application extracts all four series present in the data file
    Given the Anscombe Quartet data file exists in the "data" directory with name "data1.csv"
    When the app command with args "-o target" for the data file is run
