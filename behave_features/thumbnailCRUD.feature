@uploads
Feature: Thumbnail CRUD
    User is able to add new thumbnails to existing media,
    set defaults, list thumbnails, and remove thumbnails.
    
    Scenario Outline: Thumbnail CRUD
        Given some uploaded file
          And a thumbnail file at path <path>
         When this thumbnail file is applied to file
          And thumbnail is set as default
          And thumbnail list is requested
          And thumbnail path is requested
         Then the thumbnail path shows the default thumbnail
          And thumbnail list contains the correct number of thumbnails
          And thumbnail can be deleted

    Examples:
        | path                   |
        | testing_assets/irt.PNG |
