{::comment}

simple flask microservice that returns mathematical operation on 2 int numbers, at first only +(add) feature would be implemented, later the *(multiply) feature will be added in its own branch for purposes of staging testing etc

project structure:
/flask - the 'app'
	simple microservice app
/dockerfile - infra provisioning
	container for app(possible k8s app cluster)
	jenkins - from building and testing app(maybe use gh actions?) to deploying infra and app
	promethius,graphana,zabbix - monitoring
	ELK stack - logging
	maybe rsyslog	
/docs
	docks for app (api docs)

/ansible - config management
	
todo template yoinked, has potentially unwanted thins, work in progress
{:/comment}

# TODO List

## Tags
- **[TODO]** - Tasks that need to be completed.
- **[FIXME]** - Code or tasks that need fixing.
- **[NOTE]** - Important notes or reminders.
- **[REVIEW]** - Items that need to be reviewed or checked.
- **[BLOCKED]** - Tasks that cannot proceed due to dependencies.
- **[IDEA]** - Suggestions or ideas for future improvements.
- **[URGENT]** - High-priority tasks that need immediate attention.
- **[IN-PROGRESS]** - Tasks currently being worked on.

## Tasks

### [TODO]
- [ ] Implement user authentication
- [ ] Write unit tests for the new feature
- [ ] Update documentation for API changes

### [FIXME]
- [ ] Fix the bug in the payment processing module
- [ ] Resolve the issue with the login page not redirecting

### [NOTE]
- [ ] Remember to update the dependencies before the release
- [ ] Check the server logs for any errors after deployment

### [REVIEW]
- [ ] Review the pull request from Jane regarding the new UI changes
- [ ] Check the latest design mockups for feedback

### [BLOCKED]
- [ ] Wait for approval from the client before proceeding with the new feature
- [ ] Cannot proceed with deployment until the database migration is complete

### [IDEA]
- [ ] Consider implementing a dark mode option for better user experience
- [ ] Explore options for improving application performance

### [URGENT]
- [ ] Address security vulnerability in the user data handling process
- [ ] Respond to critical customer support tickets

### [IN-PROGRESS]
- [x] Refactor codebase for better readability (in progress)

