Feature: Get media
    This command Tests if the server is to provide media information

    Scenario: Client makes a get media request [1-2]
        After some test media from testing_assets is uploaded to kaltura with id <number>
        When kaltura attempts to get info on this media
        Then the server response status code is 200 ie OK
        And contains indication of success of data retrieval for uploaded entry
        And then the test entry is deleted

    Examples:
      | number |
      | 1      |
      | 2      |