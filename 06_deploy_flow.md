# Deploying Your Flow

Before we change our flow at all, let's try deploying it.

```bash
$ sym flow deploy demo
```

```
Checking for an existing flow...❌
Creating a new flow named "yasyfm:demo"...✅
Checking for new events...✅
Creating new event "BUCKET_ACCESS_REQUEST"...✅
Checking for a new flow definition...✅
Uploading "demo.symflow"...✅
Deploy of "demo" flow succeeded!
```

Let's make sure that worked.

```bash
$ sym flow status demo --format=json
```

```json
{
  "type": "flow",
  "name": "demo",
  "fqn": "flow:symops:yasyfm:demo",
  "last_update": "2020-03-27T05:30:43",
  "status": "ready",
  "flows": ["hello"],
  "subscriptions": [],
  "configs": []
}
```

Uh-oh! Notice how the `subscriptions` array is empty? That means there's no way to trigger our `hello` flow!

Subscriptions are how we let the Sym Runtime know to execute a flow based on an Event. The syntax for a subscription is a simple annotation: `@subscribe`. Let's try adding this to our `hello` flow in `demo.symflow`, passing in the name of the `BUCKET_ACCESS_REQUEST` Event that we created earlier.

```symflow
@subscribe('BUCKET_ACCESS_REQUEST')
flow hello
  ...
end
```

Let's deploy our flow again, and make sure our `subscribe` worked.

```bash
$ sym flow deploy demo
```

```
Checking for an existing flow...✅
Found flow "yasyfm:demo"!
Downloading current spec for "yasyfm:demo"...✅
Checking for new events...✅
No new events found!
Checking for a new flow definition...✅
Uploading "demo.symflow"...✅
Deploy of "demo" flow succeeded!
```

```bash
$ sym flow status demo --format=json
```

```json
{
  "name": "demo",
  "fqn": "flow:symops:yasyfm:demo",
  "last_update": "2020-03-27T05:35:00",
  "status": "ready",
  "flows": ["hello"],
  "subscriptions": ["poll:BUCKET_ACCESS_REQUEST"],
  "configs": []
}
```

Nice! We're killing it.

**[Next: Triggering Events](07_triggering_events.md)**
