# Putting It All Together!

Let's first verify that we can't currently access the trail.

```bash
$ aws cloudtrail get-trail-status --name symdemo
```

```
An error occurred (TrailNotFoundException) when calling the GetTrailStatus operation: Unknown trail: arn:aws:cloudtrail:us-east-2:999999999:trail/symdemo for the user: 999999999
```

Look's like, as expected, we don't have access to that trail.

Now, let's run our script to kick off a request via Sym.

```bash
$ ./request.sh
```

```json
{
  "type": "event",
  "name": "CLOUDTRAIL_ACCESS_REQUEST",
  "fqn": "event:symops:yasyfm:demo:CLOUDTRAIL_ACCESS_REQUEST",
  "created_at": "2020-03-27T05:35:23",
  "uuid": "6A76A214-586B-4C63-960F-392650416796"
}
```

```
Waiting for output from workflows triggered by Event 6A76A214-586B-4C63-960F-392650416796...
.
.
.
```

At this point, we should see a Slack message in the `#eng` channel, requesting approval.

![Slack Approval](img/approve.png)

Click "Approve", then tune back in to your terminal.

```
.
.
.
Received 1 `setenv`!

The AWS_SESSION_TOKEN environment variable has been set. You can now use the AWS CLI with the `SymDemoEscalated` Role.

If you need to use the AWS Console with this Role, please visit the following link: https://signin.aws.amazon.com/xxx
```

Awesome, it worked! Let's test it out with the AWS CLI.

```bash
$ aws cloudtrail get-trail-status --name symdemo
```

```json
{
  "LatestNotificationTime": 1454022144.869,
  "LatestNotificationAttemptSucceeded": "2020-01-28T23:02:24Z",
  "LatestDeliveryAttemptTime": "2020-01-28T23:02:24Z",
  "LatestDeliveryTime": 1454022144.869,
  "TimeLoggingStarted": "2015-11-06T18:36:38Z",
  "LatestDeliveryAttemptSucceeded": "2020-01-28T23:02:24Z",
  "IsLogging": true,
  "LatestCloudWatchLogsDeliveryTime": 1454022144.918,
  "StartLoggingTime": 1446834998.695,
  "StopLoggingTime": 1446834996.933,
  "LatestNotificationAttemptTime": "2020-01-28T23:02:24Z",
  "TimeLoggingStopped": "2015-11-06T18:36:36Z"
}
```

Success! We can now use commands such as `aws cloudtrail lookup-events` to dive into the logs.

**[Next: Up next](11_up_next.md)**
