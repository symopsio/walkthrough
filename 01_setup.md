# Setup

To follow this tutorial, you'll need a CloudTrail trail named `symdemo` set up. You'll also need an IAM role, `SymDemoEscalated`, which provides exclusive access to the trail.

For the purposes of the demo, we'll assume the ARN for the trail is `arn:aws:cloudtrail:us-east-1:999999999:trail/symdemo`.

We will also assume that you've already set up Sym at your organization, and that users are federated through your IDP, via the Sym Users service.

Finally, we'll assume you've installed the Sym Slack Bot, and that it has been granted adequate permissions to DM users.

**[Next: Create a New Flow](02_new_flow.md)**
