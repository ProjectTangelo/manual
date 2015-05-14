#Conclusions#

## Problems Encountered and Solved

### Keystone.JS

KeystoneJS is a CMS for NodeJS.  It does the bulk of the work related to presenting database materials in a pretty user interface with the ability to easily edit any information.  Keystone is not awful itself, but did not work for the requirements of our project.  Keystone’s problem for our project was in its flexibility.  Keystone is not able to be customized to the extent required to implement the functionality and user experience that we wanted for our project.  Obviously, we did not know this prior to choosing it to act as our CMS.

At the time that Sprint 1 was coming to a close, we had invested too much time into learning Keystone and forcing it to work.  Because of this, there was not enough time to abandon it and find a replacement before the Sprint 1 presentation.

For this reason, we were committed to using Keystone for Sprint 1, and our projections going into Sprint 2 were delayed.  Knowing what we know now, we would have not chosen to use Keystone.  The situation was not an entire loss, however.  Despite causing the major delay, delving into Keystone helped us learn how a professional-looking CMS works, which eventually helped us implement the functionality that the project uses now.

## Suggestion for better approaches to problem/project

### Skipping out on Linux Containers
The one reason why we chose to use containers was budget and practicality, we didn’t choose it because it was the ideal solution. David initially proposed a more expensive implementation. We wanted to save money and we did. We all had excess DigitalOcean credits and we all pitched in. We were able to run LXC’s in DO instances and got everything connected. This got us pretty far, however, we ran into some troubles with containers. First, LXC’s are pretty muchglorified chroots. It provides protection by having the kernel doing it all. 
 
It’s not a proper hypervisor so we couldn’t do things like limit RAM or CPU usage in a very clean manner. It always felt like a hack. Then there’s the fact that we’re running this on DigitalOcean. DigitalOcean runs KVM for their VPS instances and doesn’t expose and CPU extensions. So, even if we wanted to run something like VirtualBox it would be terribly slow. If we had infinite money, we probably would have set up Xen on actual hardware and take advantage of it’s remote API to run proper virtual machines or look for some provider that does that as a service.

### Using PostgresSQL instead of MongoDB
There’s not a technical reason for this but using a relational database would have helped increased the partition in our group as the non-relational database did hinder some of the team. 

### Using something other than Node.JS
We went with Node.JS because that was what the people responsible for the frontend wanted. We switched libraries several times and it was disheartening to see a few of them new, but not frequently maintained. Using Python’s Django or PHP’s Symfony may have been unsexy but we would have had better support.

## Suggestions for future extensions to project

If we had more time we would have implemented a GUI editor that the user can used to edit code.

