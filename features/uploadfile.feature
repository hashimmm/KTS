Feature: Upload File
    This command Tests whether a given file can be uploaded successfully to the server
    
    Scenario: File Upload via pullpath [1-2]
        Given a valid dropbox link as pullpath for uploading to kaltura with id <number>
        When client requests to upload this file
        Then kaltura downloads the file from dropbox
        Then the file exists on kaltura
        And then this file is deleted from kaltura since it was just for testing

    Examples:
      | number |
      | 1      |
      | 2      |


    Scenario: File Upload via file post [1-2]
    	A file from server testing assets is uploaded to kaltura with id <number>
        Then this file is deleted from this client since it was just for testing

    Examples:
      | number |
      | 1      |
      | 2      |
