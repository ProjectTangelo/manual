#API

###General Format
Most of the resources defined in the API schemas follow the same general outline:

####GET /:resource
Returns all resources that the given user is allowed to see

####GET /:resource/:id
Returns the resource that belongs to that identifier

####GET /:resource?conditions={}&fields=””&options={}
Returns all resources that pass the given criteria
- Query parameters:
    - conditions
        - JSON literal
        - defines the search criteria for the returned resources
    - fields
        - space-delimited string of field names
        - defines the fields in the resource that are returned
    - options
        - JSON literal
        - mongodb query options

####POST /:resource
Creates a resource. Fields are defined in the POST urlencoded body.

####PUT /:resource/:id
Updates a value of a resource.  Updated values are defined in the POST urlencoded body.

####DEL /:resource/:id
Deletes a resource. Often requires administrator authorization.


###Available resources

- /user
- /submission
- /feedback
- /file
- /upload

####/upload
The **/upload** resource is unique from the others.  Instead of providing a model and CRUD service on that model, **/upload** provides a means to retrieve previously uploaded files on the **/file** resource.  The **/file** resource itself stores and returns metadata for a given file.
