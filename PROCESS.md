# Charm public listing review process

*(This will probably get moved to a spec, but starting it here for now.)*

## Issues with the current process

* Inconsistency in terms of what is reviewed. Some items are written quite subjectively, and some reviewers go beyond what is in the checklist.
* Code review or no code review? The instructions get people to do a 'from empty' pull request, which hints at code review, but generally the checklist isn't about reviewing the code. This means that some reviewers do code review and some do not.
* Some of the checks are 'does this exist', or 'does this run without errors', which isn't a good use of reviewer time.
* Authors, particularly external ones, would like to know how close they are to meeting the criteria, before a review is submitted.
* "Charm works as expected" is hard to review. Sometimes you need specialised resources, sometimes there are poor instructions, this can be quite time consuming.
* Inconsistent timing - time to get assigned a reviewer, time for the reviewer to do an initial review, follow-up time. There are no times documented, so no-one is "wrong" here, but no-one is happy, either.
* Easy to get forgotten - Discourse threads are not in anyone's ticketing system, so there's no system for making sure that progress is being made.
* Difficult to assign the right people - maybe someone is on vacation, maybe it's a really busy pulse for someone, etc.

## Fixes

* Very explicit instructions that are as objective as possible. It should be clear to any reviewer and any author what the expectations are. If the reviewer wants to add additional commentary, that's fine, but it does not block the public listing. Reviewers can submit PRs for improvements to the process, checklist, and best practices when they notice something missing, and that can be discussed as a group before being adopted.
* No code review, other than specific items in the main checklist or best practices. It's too late to be reviewing the code line-by-line, and that should be the responsibility of the people building the charm, not the reviewer.
* Automate as many checks as possible. Let authors get results prior to a reviewer being assigned.
* Prefer demos over the reviewer testing the charm behaviour themselves, except for simple cases. For simple cases, there should be a tutorial that can be followed.
* Use a ticketing system rather than Discourse.
* Explicitly state the expected timetable for reviewing.
* Assign reviews to team managers, with the expectation that they delegate to someone from their team to do the actual review.

## Process

* Use GitHub (many charming teams are more primarily using Jira, but we need something that is externally accessible - reviewers can mirror tickets from GitHub to Jira if needed). It's reasonable to expect anyone that is submitting a charm for review can use GitHub issues.
* Use an GitHub issue form to get the required data in a simple format, ensuring that everything required is provided by the author.
* Use a GitHub workflow to automatically post a comment on the issue that outlines what is needed from the reviewer. This also does automatic checks where possible, so pre-ticks some items. There is a mechanism to trigger the automatic checks to run again. The automation also picks an appropriate manager to assign the review to.
* A new way is found to contact the store team to publicly list the charm (instead of a @ping on Discourse), perhaps posting a ticket somewhere, through some automation?
* Issues are closed (:fixed) when the review is successful and the charm has been publicly listed.
* Charm Tech is responsible for monitoring the state of issues overall, but team managers are responsible for meeting the timelines in the issues they are assigned.

See also:

* Example request: https://github.com/tonyandrewmeyer/charmhub-listing-review/issues/2
* Example comment: https://github.com/tonyandrewmeyer/charmhub-listing-review/issues/2#issuecomment-3047512986
* Issue submission form: https://github.com/tonyandrewmeyer/charmhub-listing-review/issues (choose the first option)
