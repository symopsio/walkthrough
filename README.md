# Sym Workflows: Compliance as Code

Hey! I'm [Yasyf](https://twitter.com/yasyf), CTO at [Sym](https://twitter.com/symops). Today I want to walk you through setting up a simple ephemeral access workflow as a `symflow`.

Let's say that an engineer wants access to application logs stored in a secure S3 bucket whenever a customer bug report comes in. This access must be gated by peer approval to comply with your company's Data Access Policy. Currently, this might involve filing a ticket with the Ops team and waiting for a multi-day turnaround. With Sym Workflows, we can implement a compliant policy that distributes approvals and gets you access in seconds, not days.

When we're done here, you'll have a smooth approval flow that you can initiate from your command line, with approvals granted via a message in a Slack channel, and fully-automated privilege escalations.

**[Next: Setup](01_setup.md)**

## Table of Contents

- [Setup](01_setup.md)
- [Create a New Flow](02_new_flow.md)
- [Define an Event](03_define_event.md)
- [Define a Workflow](04_define_flow.md)
- [Testing your Workflow](05_test_flow.md)
- [Deploying Your Workflow](06_deploy_flow.md)
- [Triggering Events](07_triggering_events.md)
- [Codifying an Access Workflow](08_codifying_access.md)
- [Setting a Config Value](09_setting_config.md)
- [Offering a Terminal Interface](10_terminal_interface.md)
- [Putting It All Together!](11_all_together.md)
- [Up next](12_up_next.md)
