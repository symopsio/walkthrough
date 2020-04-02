# Define an Event

Let's check out `events.yml` first.

```bash
$ cat demo/events.yml
```

```yaml
- name: YOUR_EVENT_NAME_HERE
  inputs:
    - name: your_first_input
      type: string
```

This is a Sym Event definition. Events are messages that are sent around the Sym Runtime in response to triggers such as an API call, a cron schedule, a user action, or an event in a third-party system (via an integration). Let's define a simple `BUCKET_ACCESS_REQUEST` event by changing the file to the following.

```yaml
- name: BUCKET_ACCESS_REQUEST
  inputs:
    - name: bucket_arn
      type: "aws:arn"
```

Notice that the Sym Runtime has a native type for [ARNs](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html). Types in Sym can be namespaced.

**[Next: Define a Workflow](04_define_flow.md)**
