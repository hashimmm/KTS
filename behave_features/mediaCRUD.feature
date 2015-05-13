@uploads
Feature: Media CRUD
    KTS is able to upload media, delete media and get media metadata.

    Scenario Outline: File Upload via pullpath
        Given some valid media file at URL <URL> of type <type>
          And a medianame <medianame>
         When client requests to upload this file
         Then the entry exists on kaltura
          And entry is of type <type>

    Examples:
      | URL                                                           | medianame       | type  |
      | https://www.dropbox.com/sh/m8874se6x8gc5ko/pbwBx5vb7v/irt.PNG | test_media_pull | image |


    Scenario Outline: File Upload via file post
        Given some valid media file at path <path> of type <type>
          And a medianame <medianame>
         When client requests to upload this file
         Then the entry exists on kaltura
          And entry is of type <type>

    Examples:
      | path                   | medianame        | type  |
      | testing_assets/irt.PNG | test_media_local | image |


    Scenario: Get entry metadata
        Given some uploaded file
         When client requests file metadata
         Then the server response status code is 200
          And the response contains 'success': true


    Scenario: Delete entry
        Given some uploaded file
         When attempting to delete this file
         Then the file ceases to exist
