#System Verifications#

| Test Case #1                             |                                                                                                      |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Test Item                                | Admin will be able to successfully login                                                             |
| Pre-Conditions                           | Website must be active                                                                               |
| Post-Conditions                          | Successfully Logged in as Admin                                                                      |
| Input Specifications                     | Username and password                                                                                |
| Expected Output Specifications           | Redirected to admin dashboard                                                                        |
| Pass/Fail Criteria                       | After login client is taken to admin dashboard                                                       |
| Assumptions and Constraints              | Website is active and working properly                                                               |

| Test Case #2                             |                                                                                                      |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Test Item                                | User will be able to successfully login                                                              |
| Pre-Conditions                           | Website must be active                                                                               |
| Post-Conditions                          | Successfully Logged in as user                                                                       |
| Input Specifications                     | Username and password                                                                                |
| Expected Output Specifications           | Redirected to user container/dashboard                                                               |
| Pass/Fail Criteria                       | After login client is taken to user container/dashboard                                              |
| Assumptions and Constraints              | Website is active and working properly                                                               |

| Test Case #3                             |                                                                                                      |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Test Item                                | Admin can add a user                                                                                 |
| Pre-Conditions                           | Must be logged in as an Admin                                                                        |
| Post-Conditions                          | Added user appears in user lists                                                                     |
| Input Specifications                     | desired username, first name, last name, e-mail address, user-type(user or admin), password, and password confirmation |
| Expected Output Specifications           | There is a new user                                                                                  |
| Pass/Fail Criteria                       | User can be seen in list of users                                                                    |
| Assumptions and Constraints              | Website is active and working properly                                                               |

| Test Case #4                             |                                                                                                      |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Test Item                                | Admin can add multiple users a user                                                                  |
| Pre-Conditions                           | Must be logged in as an Admin                                                                        |
| Post-Conditions                          | Added user appears in user lists                                                                     |
| Input Specifications                     | CSV file that contains valid information for the the users to be added                               |
| Expected Output Specifications           | There are  new users                                                                                 |
| Pass/Fail Criteria                       | Users can be seen in list of users                                                                   |
| Assumptions and Constraints              | Website is active and working properly                                                               |

| Test Case #5                             |                                                                                                      |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Test Item                                | Admin can edit a userís information                                                                  |
| Pre-Conditions                           | Must be logged in as an Admin                                                                        |
| Post-Conditions                          | Change in user information appears in user lists                                                     |
| Input Specifications                     | desired change username, first name, last name, e-mail address, user-type(user or admin), or  password and password confirmation |
| Expected Output Specifications           | Userís information has been edited                                                                   |
| Pass/Fail Criteria                       | Change in user information can be seen in list of users                                              |
| Assumptions and Constraints              | Website is active and working properly                                                               |

| Test Case #6                             |                                                                                                      |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Test Item                                | Admin can delete a user                                                                              |
| Pre-Conditions                           | Must be logged in as an Admin                                                                        |
| Post-Conditions                          | Deleted user no longer appears in user lists                                                         |
| Input Specifications                     | User selected to be deleted                                                                          |
| Expected Output Specifications           | User has been deleted                                                                                |
| Pass/Fail Criteria                       | Deleted user no longer appears in user lists                                                         |
| Assumptions and Constraints              | Website is active and working properly                                                               |

| Test Case #7                             |                                                                                                      |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Test Item                                | Lesson can be added by admin                                                                         |
| Pre-Conditions                           | Must be logged in as admin                                                                           |
| Post-Conditions                          | Lesson appears on lesson list                                                                        |
| Input Specifications                     | Lesson/file to be added                                                                              |
| Expected Output Specifications           | Lesson is added                                                                                      |
| Pass/Fail Criteria                       | Lesson appears on lesson list                                                                        |
| Assumptions and Constraints              | Website is active and working properly                                                               |

| Test Case #8                             |                                                                                                      |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Test Item                                | Lesson can be deleted by admin                                                                       |
| Pre-Conditions                           | Must be logged in as admin                                                                           |
| Post-Conditions                          | Lesson no longer appears on lesson list                                                              |
| Input Specifications                     | Lesson to be deleted                                                                                 |
| Expected Output Specifications           | Lesson is removed                                                                                    |
| Pass/Fail Criteria                       | Lesson no longer appears on lesson list                                                              |
| Assumptions and Constraints              | Website is active and working properly                                                               |

| Test Case #9                             |                                                                                                      |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Test Item                                | Lesson can be seen/opened by user                                                                    |
| Pre-Conditions                           | Lesson has been added and must be logged in as a user                                                |
| Post-Conditions                          | Can view lesson text                                                                                 |
| Input Specifications                     | Select lesson to view/open                                                                           |
| Expected Output Specifications           | Lesson/file text appears onscreen                                                                    |
| Pass/Fail Criteria                       | Lesson/file text for selected lesson/file appears onscreen                                           |
| Assumptions and Constraints              | Website is active and working properly                                                               |

| Test Case #10                            |                                                                                                      |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Test Item                                | User can submit work to Admin                                                                        |
| Pre-Conditions                           | Must be logged in as user and there must be a lesson to submit work for                              |
| Post-Conditions                          | User work has been successfully submitted                                                            |
| Input Specifications                     | Work to be submitted                                                                                 |
| Expected Output Specifications           | User work has been submitted                                                                         |
| Pass/Fail Criteria                       | User work has been successfully submitted                                                            |
| Assumptions and Constraints              | Website is active and working properly                                                               |

| Test Case #11                            |                                                                                                      |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Test Item                                | Admin can see user submission                                                                        |
| Pre-Conditions                           | A user submission exists and must be logged in as Admin                                              |
| Post-Conditions                          | Admin can view user submission                                                                       |
| Input Specifications                     | Submission to view                                                                                   |
| Expected Output Specifications           | Submission is displayed on screen                                                                    |
| Pass/Fail Criteria                       | Selected User submission can be viewed and is displayed onscreen                                     |
| Assumptions and Constraints              | Website is active and working properly                                                               |

| Test Case #12                            |                                                                                                      |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Test Item                                | Admin can give feedback to user                                                                      |
| Pre-Conditions                           | Must be logged in as admin and there must exist a submission for which to give feedback              |
| Post-Conditions                          | Feedback has been posted                                                                             |
| Input Specifications                     | Text of feedback to be given                                                                         |
| Expected Output Specifications           | Feedback had been submitted                                                                          |
| Pass/Fail Criteria                       | Feedback has been successfully submitted for desired user submissions                                |
| Assumptions and Constraints              | Website is active and working properly                                                               |

| Test Case #13                            |                                                                                                      |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Test Item                                | User can see feedback given by Admin and feedback must exist                                         |
| Pre-Conditions                           | Must be logged in as a User                                                                          |
| Post-Conditions                          | Feedback can be viewed by user                                                                       |
| Input Specifications                     | Desired feedback to view                                                                             |
| Expected Output Specifications           | Feedback is displayed for User                                                                       |
| Pass/Fail Criteria                       | Desired feedback is viewable and displayed to User                                                   |
| Assumptions and Constraints              | Website is active and working properly                                                               |

| Test Case #14                            |                                                                                                      |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Test Item                                | Administrator will be able to deploy the software from an automatic install                          |
| Pre-Conditions                           | Must meet minimum requirements for platform                                                          |
| Post-Conditions                          | software is installed                                                                                |
| Input Specifications                     | not applicable                                                                                       |
| Expected Output Specifications           | not applicable                                                                                       |
| Pass/Fail Criteria                       | Software successfully installed                                                                      |
| Assumptions and Constraints              | Ubuntu is installed and minimum requirements are met                                                 |

| Test Case #15                            |                                                                                                      |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Test Item                                | Administrator will be able to view the status of servers and container instances from a control panel |
| Pre-Conditions                           | Logged in as Admin                                                                                   |
| Post-Conditions                          | Can view the status of server and container instances                                                |
| Input Specifications                     | Click on instances tab from menu                                                                     |
| Expected Output Specifications           | Can view the status of server and container instances                                                |
| Pass/Fail Criteria                       | Can successfully view the status of server and container instances                                   |
| Assumptions and Constraints              | Salt running software is up to date                                                                  |

| Test Case #16                            |                                                                                                      |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Test Item                                | Administrator will be able to add and remove container instances                                     |
| Pre-Conditions                           | Logged in Admin                                                                                      |
| Post-Conditions                          | Container instance was added or removed from list                                                    |
| Input Specifications                     | container name                                                                                       |
| Expected Output Specifications           | Container instance was added or removed from list                                                    |
| Pass/Fail Criteria                       | Container instance was successfully added or removed from list                                       |
| Assumptions and Constraints              | Salt running software is up to date                                                                  |

| Test Case #17                            |                                                                                                      |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Test Item                                | Administrator will be able to freeze and restart container instances from a control panel            |
| Pre-Conditions                           | Logged in as Admin                                                                                   |
| Post-Conditions                          | Container instance was frozen and/or restarted                                                       |
| Input Specifications                     | container name                                                                                       |
| Expected Output Specifications           | Container instance was frozen and/or restarted                                                       |
| Pass/Fail Criteria                       | Container instance was successfully frozen and/or restarted                                          |
| Assumptions and Constraints              | Salt running software is up to date                                                                  |

| Test Case #18                            |                                                                                                      |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Test Item                                | Administrator will be able to shutdown and restart containers if it is frozen                        |
| Pre-Conditions                           | Logged in as Admin                                                                                   |
| Post-Conditions                          | Frozen container was shutdown and restarted                                                          |
| Input Specifications                     | container name                                                                                       |
| Expected Output Specifications           | Frozen container was shutdown and restarted                                                          |
| Pass/Fail Criteria                       | Frozen container was successfully shutdown and restarted                                             |
| Assumptions and Constraints              | Salt running software is up to date                                                                  |

| Test Case #19                            |                                                                                                      |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Test Item                                | User will be able to have a text scratchpad available to take notes                                  |
| Pre-Conditions                           | Must be logged in as a User                                                                          |
| Post-Conditions                          | Scratchpad must be available for use                                                                 |
| Input Specifications                     | Click on button to bring up the scratchpad                                                           |
| Expected Output Specifications           | Scratchpad is now displayed on screen                                                                |
| Pass/Fail Criteria                       | Scratchpad has successfully displayed onscreen and can be used by User                               |
| Assumptions and Constraints              | Website is active and working properly                                                               |

| Test Case #20                            |                                                                                                      |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Test Item                                | Administrator will be able to update the software automatically                                      |
| Pre-Conditions                           | Software Installed and an system is connected to the internet                                        |
| Post-Conditions                          | Software hase been succesfully updated                                                               |
| Input Specifications                     | run git                                                                                              |
| Expected Output Specifications           | Software hase been succesfully updated                                                               |
| Pass/Fail Criteria                       | Software hase been succesfully updated                                                               |
| Assumptions and Constraints              | Software Installed and an system is connected to the internet                                        |

| Test Case #21                            |                                                                                                      |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Test Item                                | Administrator will be able to set a userís password                                                  |
| Pre-Conditions                           | Logged in as Admin                                                                                   |
| Post-Conditions                          | User's password was changed                                                                          |
| Input Specifications                     | New password                                                                                         |
| Expected Output Specifications           | User's password was changed                                                                          |
| Pass/Fail Criteria                       | User's password was successfully changed                                                             |
| Assumptions and Constraints              | Website is active and working properly                                                               |

| Test Case #22                            |                                                                                                      |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Test Item                                | Users will be able to manage their accounts and profile (for example name, email address and password) |
| Pre-Conditions                           | Must be logged in as User and user able to view their homepage and profile                           |
| Post-Conditions                          | Changes made to profile will be saved and displayed                                                  |
| Input Specifications                     | User inputs different information than currently provided                                            |
| Expected Output Specifications           | New information posted to user profile                                                               |
| Pass/Fail Criteria                       | Usersí new information is displayed upon viewing the profile                                         |
| Assumptions and Constraints              | Website is active and working properly                                                               |

| Test Case #23                            |                                                                                                      |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Test Item                                | User will be able have full access control over their container instance (including installing things inside it) |
| Pre-Conditions                           | Must be logged in as User                                                                            |
| Post-Conditions                          | User able to install required components, as well as make changes to and save lessons                |
| Input Specifications                     | The changes the user wants to amke                                                                   |
| Expected Output Specifications           | User able to install required components, as well as make changes to and save lessons                |
| Pass/Fail Criteria                       | User successfully able to install required components, as well as make changes to and save lessons   |
| Assumptions and Constraints              | Software Installed                                                                                   |

| Test Case #24                            |                                                                                                      |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Test Item                                | Administrator will be able to set quotas for usage for the containers (CPU shares, memory usage)     |
| Pre-Conditions                           | Logged in as Admin                                                                                   |
| Post-Conditions                          | Quota has been set                                                                                   |
| Input Specifications                     | The amount of resources to be allocated                                                              |
| Expected Output Specifications           | Quota has been set                                                                                   |
| Pass/Fail Criteria                       | Quota has been successfully set                                                                      |
| Assumptions and Constraints              | Software installed and supported by hardware                                                         |

| Test Case #25                            |                                                                                                      |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Test Item                                | User will be able to adjust the sizes of the panels in their terminal session (terminal, lesson plan, scratchpad) |
| Pre-Conditions                           | Logged in as user                                                                                    |
| Post-Conditions                          | Panel size has been changed                                                                          |
| Input Specifications                     | Panel is dragged to desired size                                                                     |
| Expected Output Specifications           | Panel size has been changed                                                                          |
| Pass/Fail Criteria                       | Panel size has been successfully changed                                                             |
| Assumptions and Constraints              | website is working properly                                                                          |


## Test run procedure and results
### Visual Diff/PhantomJS Testing
### Protractor Testing

## Discussion of test results