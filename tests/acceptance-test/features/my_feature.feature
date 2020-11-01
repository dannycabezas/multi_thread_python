Feature: ETL Process for string data
  As a user I want to be able to extract all the my customers names from a database,
  convert them into lowercase and send them to a Kinesis stream
  
  Scenario Outline: ETL between database and kinesis in free mode
    Given an <source> as source
    And a <destination> as destination
    And a <processor> processor
    When I start ETL in free mode
    Then I get the same number of events produced as consumed
    Examples:
      | source  | processor          | destination |
      | DummyDB | metadata_decorator | Kinesis     |
  
  Scenario Outline: ETL between database and kinesis with a defined batch of events
    Given an <source> as source
    And a <destination> as destination
    And a <processor> processor
    When I start ETL with a batch of <number_events> events
    Then I get the same number of events produced as consumed
    Examples:
      | source   | processor | destination | number_events |
      | TextFile | lowercase | Kinesis     | 100           |
      | TextFile | lowercase | Kinesis     | 5000          |
      | TextFile | lowercase | Kinesis     | 20000         |
