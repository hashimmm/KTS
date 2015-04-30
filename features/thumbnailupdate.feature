Feature: Update thumbnail
    This command Tests whether new thumbnail can be applied to some media
    
    Scenario: New thumbnail [1-2]
        Given a valid file selection for thumbnail
        When this thumbnail file is applied to an uploaded testing file in kaltura with id <number>
        Thumbnail is successfully uploaded and applied
        And the testing file is deleted

    Examples:
      | number |
      | 1      |
      | 2      |