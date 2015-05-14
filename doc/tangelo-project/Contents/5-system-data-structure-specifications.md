#System Data Structure Specifications#

## System DataBase/File Structure Specification

Data in stored in MongoDB. The base form of our documents are as follows. 

### Users

- username
    - **trim** &mdash; True
    - **unique** &mdash; True
    - **required** &mdash; True
    - **type** &mdash; String
- node_id
    - **trim** &mdash; True
    - **default** &mdash; 
    - **lowercase** &mdash; True
    - **type** &mdash; String
- name_first
    - **trim** &mdash; True
    - **default** &mdash; 
    - **type** &mdash; String
- name_last
    - **trim** &mdash; True
    - **default** &mdash; 
    - **type** &mdash; String
- password
    - **trim** &mdash; True
    - **required** &mdash; True
    - **type** &mdash; String
    - **select** &mdash; False
- type
    - **trim** &mdash; True
    - **default** &mdash; user
    - **lowercase** &mdash; True
    - **enum** &mdash; ['admin', 'user']
    - **type** &mdash; String
- email
    - **trim** &mdash; True
    - **default** &mdash; 
    - **lowercase** &mdash; True
    - **type** &mdash; String
- container_id
    - **trim** &mdash; True
    - **default** &mdash; 
    - **lowercase** &mdash; True
    - **type** &mdash; String

<div class="break"></div>
### Feedback

- content
    - **required** &mdash; True
    - **type** &mdash; String
- createdAt
    - **type** &mdash; Date
- submission
    - **ref** &mdash; submission
    - **required** &mdash; True
    - **type** &mdash; String

### File Uploads

- content
    - **required** &mdash; True
    - **type** &mdash; String
    - **select** &mdash; False
- ext
    - **required** &mdash; True
    - **type** &mdash; String
- size
    - **required** &mdash; True
    - **type** &mdash; Number
- filename
    - **required** &mdash; True
    - **type** &mdash; String

<div class="break"></div>

### User Submission

- owner
    - **ref** &mdash; user
    - **required** &mdash; True
    - **type** &mdash; String
- content
    - **required** &mdash; True
    - **type** &mdash; String
- number
    - **default** &mdash; 0
    - **type** &mdash; Number
- createdAt
    - **type** &mdash; Date
- feedback
    - **ref** &mdash; feedback
    - **type** &mdash; String

### Lesson Plan

- content
    - **required** &mdash; True
    - **type** &mdash; String
- number
    - **required** &mdash; True
    - **type** &mdash; Number
- createdAt
    - **type** &mdash; Date

<div class="break"></div>

## System Internal Data Structure Specification

### LXC Salt Query Response 

- data
    - **type** &mdash; String
- STDOUT
    - **type** &mdash; String
- command
    - **type** &mdash; String
- date
    - **type** &mdash; Date
