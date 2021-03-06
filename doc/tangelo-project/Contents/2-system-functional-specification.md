#System Functional Specification#

<div class="break"></div>

## User Interface Design
The user interface is meant to leverage newer browser technologies like CSS3 and HTML5. Some of the new features used is the drag-and-drop API and media queries for responsive design. 

### Admin Screens
![ Landing admin screen ](images/screens/admin_screen.png)
Here is the default admin screen.

![ Admin lxc managment ](images/screens/lxc-managment.png)
The administrator will be able to manage LXC instances here. 

![ Admin adding lessons ](images/screens/add-lessons.png)
The administrator will be able to upload lesson plans here. 

![ Admin views lessons ](images/screens/lessons.png)
The administrator will be able to view uploaded lesson plans here. 

![ Admin views submissions ](images/screens/submissions.png)
The administrator will be able to see submissions made by clients.

![ Admin views user list ](images/screens/user-list.png)
The administrator will be able to see a list of users here.

![ Admin bulk user import ](images/screens/import.png)

The adminstrator will be able to import a list of users as a CSV file here.


### Client (non-admin) Screens
![ Client views lesson plans ](images/screens/client-lesson-plans.png)
The user will be able to see what lesson plans the administrator has uploaded.

![ Client views scratchpad ](images/screens/client-scratchpad.png)
The user will be able to have a scratchpad available to use like a secondary clipboard.

![ Client views submissions ](images/screens/client-submissions.png)
The user will be able to see their submissions and comments made by the administrator here. 

<div class="break" ></div>
## System Specifications
### Authentication of users to Linux instances

 When a session is created, its ID is sent out to all of the nodes.

 Each node has a folder called `/opt/tangelo_sessions/`

 Session files are written in the directory, on each relevant node.

 The master writes a file onto the other nodes. It can also
 deletes those nodes. We're implementing this with files in a directory because 
 it is simpler than having a monolithic file, or database.

 **To check if a node has a session:**

 Given the url:
 `https//node-01.tangelo.work/?session_id=XXXXXXXX`

 The session is valid if and only if the file `/opt/tangelo_sessions/XXXXXXXX.session` exists.
