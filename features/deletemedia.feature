Feature: Delete media
    This command Tests if the server is able to delete media upon request
    
    Scenario: One Delete Requested By Selection [1-2]
        After a file donkey.jpg from local relative path /testing_assets has been uploaded to kaltura with id <number>
        When attempting to delete this file
        The file ceases to exist

    Examples:
      | number |
      | 1      |
      | 2      |
