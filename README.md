# Sym Workflows: Compliance as Code

Hey! Today I want to walk you through setting up a simple ephemeral access workflow as a `symflow`.

Let's say that an engineer wants access to CloudTrail logs whenever a customer bug report comes in. This access must be gated by peer approval to comply with your company's Data Access Policy. Currently, this might involve filing a ticket with the Ops team and waiting for a multi-day turnaround. With Sym Workflows, we can implement a compliant policy that distributes approvals and gets you access in seconds, not days.

When we're done here, you'll have a smooth approval flow that you can initiate from your command line, with approvals granted via a message in a Slack channel.

**[Next: Setup](01_setup.md)**
