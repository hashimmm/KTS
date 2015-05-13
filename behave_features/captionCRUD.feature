@uploads
Feature: Caption CRUD
    User is able to add new captions to existing media,
    set defaults, list captions, update caption details,
    and remove captions.
    
    Scenario Outline: caption upload and list
        Given some uploaded file
          And a caption file at path <path>
         When this caption file is applied to file
          And caption list is requested
         Then the caption list contains uploaded caption

    Examples:
        | path                      |
        | testing_assets/sample.srt |

    Scenario: Caption update
        Given some uploaded file
          And the file has captions
         When a caption is updated
          And caption list is requested
         Then the caption list contains updated details

    Scenario: Caption delete
        Given some uploaded file
          And the file has captions
         When a caption is deleted
          And caption list is requested
         Then the caption list no longer contains it
