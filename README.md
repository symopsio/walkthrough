# Sym Workflows: Compliance as Code

Hey! I'm [Yasyf](https://twitter.com/yasyf), CTO at [Sym](https://twitter.com/symops). Today I want to walk you through setting up a simple ephemeral access workflow as a `symflow`.

Let's say that an engineer wants access to application logs stored in a secure S3 bucket whenever a customer bug report comes in. This access must be gated by peer approval to comply with your company's Data Access Policy. Currently, this might involve filing a ticket with the Ops team and waiting for a multi-day turnaround. With Sym Workflows, we can implement a compliant policy that distributes approvals and gets you access in seconds, not days.

When we're done here, you'll have a smooth approval flow that you can initiate from your command line, with approvals granted via a message in a Slack channel, and fully-automated privilege escalations.

**[Next: Setup](01_setup.md)**

## Table of Contents

1. [Setup](01_setup.md)
2. [Create a New Flow](02_new_flow.md)
3. [Define an Event](03_define_event.md)
4. [Define a Workflow](04_define_flow.md)
5. [Testing your Workflow](05_test_flow.md)
6. [Deploying Your Workflow](06_deploy_flow.md)
7. [Triggering Events](07_triggering_events.md)
8. [Codifying an Access Workflow](08_codifying_access.md)
9. [Setting a Config Value](09_setting_config.md)
10. [Offering a Terminal Interface](10_terminal_interface.md)
11. [Putting It All Together!](11_all_together.md)
12. [Up next](12_up_next.md)
