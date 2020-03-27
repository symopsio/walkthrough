# Codifying an Access Workflow

Let's reopen our `demo.symflow` file, and implement the access workflow we set out to acheive. As a reminder, there are three main steps:

1. A user requests access to a CloudTrail trail
2. Approval for this access is sent to a group of approvers in Slack
3. When access is granted, the user is able to access the trail instantly

### Step 1: Request

We will handle Step 1 in this demo by using the CLI to emit another event.

### Step 2: Approve

Step 2 will use the standard library method `io.confirm`, which is similar to `io.say`, but instead prompts the recipient with "yes" and "no" actions. Instead of DMing this to the current user, we will send it to a Slack channel.

We will want to use the trail ARN in our approval request. You can get the ARN by reading it from the Event input `trail_arn`. Inputs can be accessed at `g.context.inputs`.

```symflow
arn = g.context.inputs.trail_arn
```

Sym Config allows us to read arbitrary strings as config values from our workflows. We can access Config by calling `g.config.key`. Let's assume we have a config called `channel` with the name of our Slack channel; we'll look at how to set that value later.

```symflow
channel = g.config.channel
```

Instead of a `message`, `io.confirm` takes a `prompt`. Let's have the prompt in this case be: "NAME would like to access the trail ARN.".

```symflow
prompt = `#{user.name} would like to access the trail #{arn}`
```

Now, we can make our call to `io.confirm`.

```symflow
io.confirm(channel, prompt: prompt)
```

### Step 3: Escalate

Next, we need to implement Step 3. Sym's standard library exposes a `iam` module which you can import. Let's put that import at the op of our file.

```symflow
import iam
```

The `iam` module has a `assume_role` method which takes in a role name, and a user, and returns an `AWSSession` object. This object contains temporary credentials.

```symflow
session = iam.assume_role("SymDemoEscalated", user: user)
```

Finally, we want to return those credentials to the user. `io` has a handy method called `setenv` which will do exactly this, and as a bonus will set the relevant environment variables if the receiving interface is a terminal.

```symflow
io.setenv(session.credentials, user: user)
```

Putting all of the above together, our file should look something like this.

```symflow
import g, io
import iam

alias user = g.context.user

@poll('CLOUDTRAIL_ACCESS_REQUEST')
flow hello
  arn = g.context.inputs.trail_arn
  channel = g.config.channel
  prompt = `#{user.name} would like to access the trail #{arn}`
  io.confirm(channel, prompt: prompt)

  session = iam.assume_role("SymDemoEscalated", user: user)
  io.setenv(session.credentials, user: user)
end
```

Alright, almost done! Two steps left.

**[Next: Setting a Config Value](08_setting_config.md)**
