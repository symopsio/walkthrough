ID: infra_access
Summary: Sym Workflows turn tedious, manual compliance processes into executable workflow definitions that your ops teams can manage as code.
Feedback Link: mailto:founders@symops.io

# Sym Workflows: Infrastructure Access

## Welcome

Hey! I'm [Yasyf](https://twitter.com/yasyf), CEO at [Sym](https://www.symops.io/). Today I want to walk you through setting up a simple ephemeral infrastructure access control as a Sym Workflow.

Let's set up our use case. I'm an engineer at Healthy Health, a 100 person healthtech startup. We integrate with health systems, and in the process end up with lots of patient PHI, so we have to be HIPAA-compliant. Additionally, our customers require that we pass annual SOC 2 Type 2 audits, as well as routine vendor security assessments.

To increase the security and audibility of infrastructure access at Healthy Health, we've decided to put a peer-approval process around sensitive resources, with a low default access level, and short grants of escalated privileges upon approval. This happens to satisfy many of our compliance requirements, namely:

- **HIPAA Privacy Rule**: Minimum Necessary Requirement
- **HIPAA Security Rule**: Access Authorization, Unique User Identification, Automatic Logoff
-  **SOC 2**: Common Controls 4 (Monitoring Activities) and 6 (Logical and Physical Address)

Without Sym, we might decide to implement our approval and access workflow using JIRA tickets, and a single task queue that is owned by the SecOps team. This would require SecOps to manually review requests, escalate engineers, and revoke privileges at a later date. Such a workflow is prone to long turnaround times for engineers, wasted time for ops, and access drift as a result of forgotten grants.

With Sym, we can easily implement a compliant policy that distributes approvals and gets engineers short-lived access in seconds, while keeping ops out of the loop.

When you're done with this tutorial, you'll have a smooth approval flow that you can initiate from your command line, with approvals granted via a message in a Slack channel, and fully-automated privilege escalations.

## Setup

For the purposes of this tutorial, we'll assume that your company has already set up Sym at an organizational level. This includes integrating with your IDP to obtain a user mapping.

To complete this tutorial, you should [install Terraform](https://learn.hashicorp.com/terraform/getting-started/install), and make sure you have a working install of Python 3.

You'll also need an escalation strategy. An escalation strategy is how we tell Sym what to do when an access request has been approved. The easiest way to get Sym up and running is to have an AWS IAM Group whose members can assume a privileged role. We'll walk you through this if you don't already have it set up. Sym also supports escalation via Okta, and any custom lambda via our [Serverless Templates](https://github.com/symopsio/serverless-templates).

If you'd like to play around with connecting Okta with IAM for SSH, you should check out our [`terraform-okta-ssm-modules`](https://github.com/symopsio/terraform-okta-ssm-modules) posts.

## Escalation Strategy

Positive
: *You can skip this step if you already have an escalation strategy in place.*

Let's create a sample escalation strategy for use in this tutorial. Please login to the AWS Console and complete the following steps.

1. Create an IAM Role named `SymDemoEscalated`.
2. In your terminal, run `aws iam get-role --role-name SymDemoEscalated`.
   Note the `RoleId`, which should begin with `AROA`.
3. Create an S3 bucket named `SymDemo-YourNameHere`, and attach the following policy, which restricts access to the `SymDemoEscalated` Role.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::SymDemo-YourNameHere",
        "arn:aws:s3:::SymDemo-YourNameHere/*"
      ],
      "Condition": {
        "StringNotLike": {
          "aws:userId": [
            "AROAEXAMPLEID:*"
          ]
        }
      }
    }
  ]
}
```

4. Create an IAM Group, `SymDemoAdmins`, and attach the following policy, which allows the group to assume the `SymDemoEscalated` Role.

```json
{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": "sts:AssumeRole",
        "Resource": "arn:aws:iam::ACCOUNT-ID:role/SymDemoEscalated"
      }
    ]
}
```

Now, the only users who will be able to access our S3 bucket are the ones in the `SymDemoAdmins` IAM Group. This group will be our escalation strategy.


## Creating a New Workflow

Let's first install the Sym CLI helper.

```bash
$ brew install sym
```

```
==> Downloading https://homebrew.bintray.com/bottles/sym-3.04.mojave.bottle.tar.gz
######################################################################## 100.0%
==> Pouring sym-3.04.mojave.bottle.tar.gz
🍺  /usr/local/Cellar/sym/3.04: 65 files, 82.9KB
```

We'll have to login before we can do anything else. Sym also supports SSO, if your organization has set it up.

```bash
$ sym login
```

```
Sym Org: healthy-health
Username: yasyfm
Password: ************
MFA Token: ******

Success! Welcome, Yasyf. 🤓
```

Next, let's create a new Sym Workflow called `infra_access`. We'll use the `approval` template: one of many Sym-provided templates to explore.

```bash
sym flow new infra_access --template=hello-world
```

You'll notice that this creates a `infra_access` directory with two files: `infra_access.tf` and `infra_access.py`. The Terraform file is where we will declare the resources and configuration for this workflow, and the Python file is where we will put our custom workflow logic.

## Terraform Config

Let's take a look at `infra_access.tf`.

<button href="">Open in Cloud Shell</button>

```terraform
resource "sym_flow" "infra_access" {
  meta = {
    strategies = sym_strategies.escalation_strategies
  }

  handler = {
    parent = "sym:approval"
    hooks = file("infra_access.py")
  }
}

resource "sym_strategies" "escalation_strategies" {
  // Add your escalation strategies here
}
```

The `sym_flow` resource
