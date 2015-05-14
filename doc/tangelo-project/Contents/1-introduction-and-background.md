#Introduction and Background#

<div class="break"></div>

## Statement of Problem Area

During a recent CSULB semester, the Linux computer labs were replaced by Windows labs.  As a result, classes that heavily focused on using the Linux operating system forced students to install Linux on their personal computers and laptops via manual installation or a virtual machine.  This process has proven to be strenuous and adds an unnecessary setup time for the class.  Problems that students encounter may also rely on their hardware, due to the lack of uniform development environment.

<div class="break"></div>

## Background

### David Nuon

Graphics designer turned programmer, who works on web and mobile applications.  Holds interest in everything Linux and Open-Source.  Likes to name things after fruit.

### Eduardo Arevalos

Follower of modern events related to gaming and computers.  Hard working student who took up interest in computer science at the end of high school.  Aims to work in an engineering setting where he can apply his skills.

### Forest Turner
Experienced with 3D printing and hands on electronics. Is interested in studying algorithms. Aims to work in an engineering setting where he can apply his skills.

### Johnny Patterson

Experienced in developing the frontend and backend of video games as well as desktop, web, mobile, and embedded applications.  Aims to work in an engineering setting, working on robots and/or rockets.

### Shane Satterfield
Experienced in graphics programming and Linux.  Has interests in system programming and studying algorithms.  Aims to work in an engineering setting where he can apply his skills.

### Tiffany Artis
Has been working with computers from a very young age, and her first experience with coding coming in the form of HTML.  She created webpages and fixed computers as a fun hobby in middle school and high school, this hobby carried onto  her interests in college, which led her to a major in computer science, where she learned other languages, such as C++ and Java.

### Tyler Goodman
Interested in web development and NodeJS.  Experienced in using various web frameworks.

<div class="break"></div>

## Brief Project Description

Tangelo an application that allows user to login to a Linux terminal session through the browser. The user’s session will be sandboxed and he or she will be able to have full control over their container instance. An important feature of our application is that it will be easy to install by an administrator so that he or she may use it on their own servers. 

The administrator may also provide documents for things like a lesson plan or assignments that other users may refer to while using the system. Another important feature would be allowing the administrator to control each container a user has. If a user locks up their container, the administrator will be able to halt and reset it. An application such as ours can be useful for small vocational schools or secondary level institutions where appropriating a large IT staff is not feasible.

<div class="break"></div>

## Purpose/Objectives

Our product would allows users to have hands on experience with the use Linux through a web browser, in situations where they would otherwise not have access to.  In addition, by giving administrators the ability to create, destroy, halt, or restart instances will allow users to recover from what could have been a fatal mistake. 

Finally, by allowing instances  to be kept separate and/or on their own server(s), the actions of one user will not negatively impact other users.

<div class="break"></div>

## Team Achievements

<h3>Sprint 1</h3>
<h4>Feburary 26th, 2015</h4>

<div id="sprint-table">
<table cellpadding="0" cellspacing="0" class="c34">
<tbody>
<tr class="c3 heading">
<td class="c24 c47" colspan="1" rowspan="1">
<p class="c10"><span class="c16">User Stories</span></p>
</td>

<td class="c5 c47" colspan="1" rowspan="1">
<p class="c10"><span class="c16">Tasks</span></p>
</td>

<td class="c5 c47" colspan="1" rowspan="1">
<p class="c10"><span class="c16">Responsible Party</span></p>
</td>
</tr>

<tr class="c3">
<td class="c24" colspan="1" rowspan="1">
<p class="c15"><span class="c11">Administrator will be able to set a
user&rsquo;s password</span></p>

<p class="c8 c1"></p>

<p class="c15"><span class="c11">Administrator will be able to set password
expiration</span></p>

<p class="c8 c1"></p>

<p class="c15"><span class="c11">Users will be able to request to reset their
passwords</span></p>
</td>

<td class="c5" colspan="1" rowspan="1">
<p class="c10"><span class="c11">Write user authentication</span></p>

<p class="c8 c1"></p>

<p class="c10"><span class="c11">Write user login page</span></p>

<p class="c8 c1"></p>

<p class="c10"><span class="c11">Write dashboard functionality</span></p>

<p class="c8 c1"></p>

<p class="c10"><span class="c11">Design views and forms for modifying user
passwords and dashboard</span></p>

<p class="c8 c1"></p>
</td>

<td class="c5" colspan="1" rowspan="1">
<p class="c10"><span class="c11">Shane Satterfield</span></p>

<p class="c8 c1"></p>

<p class="c10"><span class="c11">Tyler Goodman</span></p>

<p class="c8 c1"></p>

<p class="c8 c1"></p>
</td>
</tr>

<tr class="c3">
<td class="c24" colspan="1" rowspan="1">
<p class="c15"><span class="c11">Administrator will be able to set up user
accounts from a CSV file</span></p>

<p class="c8 c1"></p>

<p class="c15"><span class="c11">Administrator will be able to set up to
create and remove individual users from an administrator panel</span></p>

<p class="c8 c1"></p>
</td>

<td class="c5" colspan="1" rowspan="1">
<p class="c10"><span class="c11">Design views and forms for uploading CSV
files and managing users</span></p>

<p class="c8 c1"></p>

<p class="c10"><span class="c11">Write functionality for parsing a CSV file
and creating those users it</span></p>

<p class="c8 c1"></p>

<p class="c10"><span class="c11">Write user model with required
fields</span></p>
</td>

<td class="c5" colspan="1" rowspan="1">
<p class="c10"><span class="c11">Eduardo Arevalos</span></p>

<p class="c8 c1"></p>

<p class="c8 c1"></p>
</td>
</tr>

<tr class="c3">
<td class="c24" colspan="1" rowspan="1">
<p class="c15"><span class="c11">Users will be able to manage their accounts
and profile (for example name, email address and password)</span></p>

<p class="c8 c1"></p>
</td>

<td class="c5" colspan="1" rowspan="1">
<p class="c10"><span class="c11">Design views and forms for managing a user
profile</span></p>

<p class="c8 c1"></p>

<p class="c10"><span class="c11">Write functionality for committing those
changes to the database</span></p>
</td>

<td class="c5" colspan="1" rowspan="1">
<p class="c10"><span class="c11">Tiffany Artis</span></p>
</td>
</tr>
</tbody>
</table>

<table cellpadding="0" cellspacing="0" class="c34">
<tbody>
<tr class="c3">
<td class="c61" colspan="1" rowspan="1">
<p class="c15"><span class="c11">User will be able have full access control
over their container instance (including installing things inside
it)</span></p>
</td>

<td class="c48" colspan="1" rowspan="1">
<p class="c10"><span class="c11">Setup virtual machines for
development</span></p>

<p class="c8 c1"></p>

<p class="c10"><span class="c11">Create LXC templates that will be a
user&rsquo;s default system</span></p>

<p class="c8 c1"></p>

<p class="c8 c1"></p>

<p class="c8 c1"></p>
</td>

<td class="c52" colspan="1" rowspan="1">
<p class="c10"><span class="c11">David Nuon</span></p>

<p class="c8 c1"></p>

<p class="c10"><span class="c11">Forest Turner</span></p>
</td>
</tr>

<tr class="c3">
<td class="c61" colspan="1" rowspan="1">
<p class="c15"><span class="c11">User will be able to log into the system
(from the browser) and access a terminal session that is logged into their
container instance</span></p>
</td>

<td class="c48" colspan="1" rowspan="1">
<p class="c10"><span class="c11">Write automatic login into container from
browser</span></p>

<p class="c8 c1"></p>

<p class="c10"><span class="c11">Design view that will hold the terminal
and</span></p>

<p class="c10"><span class="c11">user menu</span></p>

<p class="c8 c1"></p>

<p class="c10"><span class="c11">Embed the terminal in user view</span></p>
</td>

<td class="c52" colspan="1" rowspan="1">
<p class="c10"><span class="c11">Shane Satterfield</span></p>

<p class="c8 c1"></p>

<p class="c10"><span class="c11">Johnny Patterson</span></p>
</td>
</tr>
</tbody>
</table>

<div class="break"></div>

<h3>Sprint 2</h3>
<h4>March 19th, 2015</h4>

<table cellpadding="0" cellspacing="0" class="c34">
<tbody>
<tr class="c3 heading">
<td class="c31" colspan="1" rowspan="1">
<p class="c10"><span class="c16">User Stories</span></p>
</td>

<td class="c62 c47" colspan="1" rowspan="1">
<p class="c10"><span class="c16">Tasks</span></p>
</td>

<td class="c40 c47" colspan="1" rowspan="1">
<p class="c10"><span class="c16">Responsible Party</span></p>
</td>
</tr>

<tr class="c3">
<td class="c63" colspan="1" rowspan="1">
<p class="c15"><span class="c11">Administrator will be able to submit
documents (PDF, HTML, DOCX, and ODF) for other users to view</span></p>
</td>

<td class="c62" colspan="1" rowspan="1">
<p class="c10"><span class="c11">Write file handling and functionality for
associating with lessons</span></p>

<p class="c8 c1"></p>

<p class="c10"><span class="c11">Design and write views for managing
documents</span></p>
</td>

<td class="c40" colspan="1" rowspan="1">
<p class="c10"><span class="c11">Shane Satterfield</span></p>

<p class="c8 c1"></p>

<p class="c10"><span class="c11">Tyler Goodman</span></p>

<p class="c8 c1"></p>

<p class="c10"><span class="c11">Tiffany Artis</span></p>

<p class="c8 c1"></p>

<p class="c10"><span class="c11">Eduardo Arevalos</span></p>

<p class="c8 c1"></p>
</td>
</tr>

<tr class="c3">
<td class="c63" colspan="1" rowspan="1">
<p class="c15"><span class="c11">User will be able to have a text scratchpad
available to take notes.</span></p>
</td>

<td class="c62" colspan="1" rowspan="1">
<p class="c10"><span class="c11">Write widget and button toggle that hides
and shows scratchpad</span></p>
</td>

<td class="c40" colspan="1" rowspan="1">
<p class="c10"><span class="c11">Eduardo Arevalos</span></p>
</td>
</tr>
</tbody>
</table>

<table cellpadding="0" cellspacing="0" class="c34">
<tbody>
<tr class="c3">
<td class="c55" colspan="1" rowspan="1">
<p class="c15"><span class="c11">Administrator will be able to set quotas for
usage for the containers (CPU shares, memory usage)</span></p>

<p class="c8 c1"></p>

<p class="c15"><span class="c11">Administrator will be able to shutdown and
restart containers if it is frozen</span></p>

<p class="c8 c1"></p>

<p class="c15"><span class="c11">Administrator will be able to view the
status of servers and container instances from a control panel</span></p>
</td>

<td class="c45" colspan="1" rowspan="1">
<p class="c10"><span class="c11">Write utility to manage container quotas so
it can be used by node</span></p>

<p class="c8 c1"></p>

<p class="c10"><span class="c11">Write utility to shutdown and restart
instances</span></p>

<p class="c8 c1"></p>

<p class="c10"><span class="c11">Write utility to poll other
servers</span></p>

<p class="c1 c8"></p>

<p class="c10"><span class="c11">Design and write views so they can interact
with the utilities</span></p>
</td>

<td class="c60" colspan="1" rowspan="1">
<p class="c10"><span class="c11">David Nuon</span></p>

<p class="c8 c1"></p>

<p class="c10"><span class="c11">Forest Turner</span></p>

<p class="c8 c1"></p>

<p class="c10"><span class="c11">Shane Satterfield</span></p>

<p class="c8 c1"></p>

<p class="c10"><span class="c11">Tyler Goodman</span></p>
</td>
</tr>

<tr class="c3">
<td class="c55" colspan="1" rowspan="1">
<p class="c15"><span class="c11">SSL</span></p>
</td>

<td class="c45" colspan="1" rowspan="1">
<p class="c10"><span class="c11">Setup and configure SSL</span></p>
</td>

<td class="c60" colspan="1" rowspan="1">
<p class="c10"><span class="c11">Johnny Patterson</span></p>
</td>
</tr>

<tr class="c3">
<td class="c55" colspan="1" rowspan="1">
<p class="c15"><span class="c11">User will be able to log into a terminal
session from the browser</span></p>
</td>

<td class="c45" colspan="1" rowspan="1">
<p class="c10"><span class="c11">Implement user terminal using WebSockets
instead of AJAX</span></p>
</td>

<td class="c60" colspan="1" rowspan="1">
<p class="c10"><span class="c11">Johnny Patterson</span></p>
</td>
</tr>
</tbody>
</table>


<h3>Sprint 3</h3>
<h4>April 9th, 2015</h4>

<table cellpadding="0" cellspacing="0" class="c34">
<tbody>
<tr class="c3 heading">
<td class="c49 c47" colspan="1" rowspan="1">
<p class="c10"><span class="c16">User Stories</span></p>
</td>

<td class="c46 c47" colspan="1" rowspan="1">
<p class="c10"><span class="c16">Tasks</span></p>
</td>

<td class="c35 c47" colspan="1" rowspan="1">
<p class="c10"><span class="c16">Responsible Party</span></p>
</td>
</tr>

<tr class="c3">
<td class="c49" colspan="1" rowspan="1">
<p class="c15"><span class="c11">User will be able to submit work to the
administrator</span></p>

<p class="c8 c1"></p>
</td>

<td class="c46" colspan="1" rowspan="1">
<p class="c10"><span class="c11">Implement functionality that allows users to
submit work from inside their container</span></p>

<p class="c8 c1"></p>

<p class="c10"><span class="c11">Implement functionality to show the result
in the user&rsquo;s dashboard</span></p>
</td>

<td class="c35" colspan="1" rowspan="1">
<p class="c10"><span class="c11">Eduardo Arevalos</span></p>

<p class="c8 c1"></p>

<p class="c10"><span class="c11">Tyler Goodman</span></p>

<p class="c8 c1"></p>
</td>
</tr>

<tr class="c3">
<td class="c49" colspan="1" rowspan="1">
<p class="c15"><span class="c11">Administrator will be able to view work a
user submitted and provide feedback on user submissions</span></p>
</td>

<td class="c46" colspan="1" rowspan="1">
<p class="c10"><span class="c11">Implement functionality to view user
submissions and comment on them</span></p>
</td>

<td class="c35" colspan="1" rowspan="1">
<p class="c10"><span class="c11">Shane Satterfield</span></p>

<p class="c8 c1"></p>

<p class="c10"><span class="c11">Tiffany Artis</span></p>
</td>
</tr>

<tr class="c3">
<td class="c49" colspan="1" rowspan="1">
<p class="c15"><span class="c11">Administrator will be able to add/remove
container instances</span></p>

<p class="c8 c1"></p>
</td>

<td class="c46" colspan="1" rowspan="1">
<p class="c10"><span class="c11">Implement saltstack module to send
add/remove instance commands to other servers</span></p>

<p class="c8 c1"></p>
</td>

<td class="c35" colspan="1" rowspan="1">
<p class="c10"><span class="c11">David Nuon</span></p>

<p class="c8 c1"></p>

<p class="c10"><span class="c11">Forest Turner</span></p>
</td>
</tr>

<tr class="c3">
<td class="c49" colspan="1" rowspan="1">
<p class="c15"><span class="c11">Administrator will be able to deploy the
software from an automatic install</span></p>

<p class="c8 c1"></p>

<p class="c15"><span class="c11">Administrator will be able to update the
software automatically</span></p>

<p class="c8 c1"></p>
</td>

<td class="c46" colspan="1" rowspan="1">
<p class="c10"><span class="c11">Write installer for the node.js frontend for
the system</span></p>

<p class="c8 c1"></p>

<p class="c10"><span class="c11">Write saltstack configuration files so that
other servers will be able to be configured with the proper
packages</span></p>

<p class="c8 c1"></p>

<p class="c10"><span class="c11">Test on Vagrant boxes and
DigitalOcean</span></p>
</td>

<td class="c35" colspan="1" rowspan="1">
<p class="c10"><span class="c11">Johnny Patterson</span></p>

<p class="c8 c1"></p>

<p class="c10"><span class="c11">David Nuon</span></p>
</td>
</tr>
</tbody>
</table>

<div class="break"></div>

<h3>Final Sprint</h3>
<h3> May 14, 2015</h3>

<table cellpadding="0" cellspacing="0" class="c34">
<tbody>
<tr class="c3 heading">
<td class="c39 c47" colspan="1" rowspan="1">
<p class="c10"><span class="c16">User Stories</span></p>
</td>

<td class="c50 c47" colspan="1" rowspan="1">
<p class="c10"><span class="c16">Tasks</span></p>
</td>

<td class="c43" colspan="1" rowspan="1">
<p class="c10"><span class="c16">Responsible Party</span></p>
</td>
</tr>

<tr class="c3">
<td class="c39" colspan="1" rowspan="1">
<p class="c10"><span class="c11">User will find minimal errors</span></p>
</td>

<td class="c50" colspan="1" rowspan="1">
<p class="c10"><span class="c11">Fix any bugs / regressions that
haven&rsquo;t been addressed in previous sprints</span></p>
</td>

<td class="c59" colspan="1" rowspan="1">
<p class="c10"><span class="c11">Entire Team</span></p>
</td>
</tr>

<tr class="c3">
<td class="c39" colspan="1" rowspan="1">
<p class="c10"><span class="c11">Bonus features</span></p>
</td>

<td class="c50" colspan="1" rowspan="1">
<p class="c10"><span class="c11">Choose and implement one of the stretch
goals if time allows</span></p>
</td>

<td class="c59" colspan="1" rowspan="1">
<p class="c10"><span class="c11">Entire Team</span></p>
</td>
</tr>
</tbody>
</table>
</div><!-- Sprint Table -->
