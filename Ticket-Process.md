Feature or enhancement tickets
=================================
1. Investigate and provide solution or list out what need to be done on that ticket 
2. Get confirm on solution (from component lead or team lead or technical architect)
3. Provide estimate: should provide both story point and hour story point just shows the complicated of ticket, if story point > 5 should be considered to break into smaller ones
4. Component team will discuss and provide estimate together
5. Component lead should track deadline for each members/tickets of that sprint to see if we have enough time to complete all assigned tickets of that sprint and raise comment if need start working  this is to avoid wasting effort on the wrong way

Bug tickets
==============================
1. All steps are resemble feature tickets
2. Adding more: when ticket is ready for review these information must be added into Jira:
    * Root cause
    * Solution
    * Scenario tests
    * Impact: Y/N
      *If yes: point out where is the place so QC will test this impact.
    
Comments
============================
1. The first comment of ticket must be : list out what need to be done for that ticket, team lead, component lead or architect will confirm then developer start to develop
2. Every day must update status for ticket: what has been done, difficulties if have, question for any non-obvious if have, next steps if ticket not yet done
3  Before making pull request, provide evidences: test scenarios, test coverage > 80%
4. Pull request link must be added to jira when ticket done.
5. Code review comments put directly into github
6. Team lead or component lead must put into ticket comments for internal review: “review done” or something like that to confirm that the ticket has been done at TMA side

Review process
=============================
1. Check if code has enough unit tests (code coverage)
2. Unit test pass
3. Coding standard
4. Code document
5. If a function has no unit test: comments in code document the reason why
6. Check if the implement satisfied requirement: check if scenario tests reflect requirement
7. Put comment into Jira for review passes or not

Vacation: TMA-1
Sick: TMA-2
Comp: TMA-3
Holiday: TMA-4
