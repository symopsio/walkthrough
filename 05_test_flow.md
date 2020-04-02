# Test a Workflow

The Sym platform has built-in support for unit and acceptance testing. Let's explore both, with our toy workflow.

## Unit Testing

We can create a unit test file called `demo.symflow.test`, and put the following basic test inside. Note that the syntax for tests is similar to that of defining a workflow, but files with an `import` of `t` (short for _test_) will be rejected by the Sym Runtime if you try to deploy them.

```symflow
import g, t

# @test:description The user is greeted
test hello
  t.expect_output(g.context.user, body: "Hello, Yasyf Mohamedali!")
end
```

A few important things to note.

The name of a test must match the name of the flow we are unit-testing. To define multiple tests for a flow, simply provide multiple `test` blocks, supplying the same name each time.

The `t` module has several expectations built in. Above, we are using `expect_output` to assert that the `io.say` in our main flow succeeds. The current user (canonically located at `g.context.user`), which here is used to indicate the channel to expect output on, is supplied by the test harness (although various properties can be overridden).

Let's try to run our test!

```bash
sym flow test demo
```

```
Testing flow "demo.symflow"...
Running tests in "demo.symflow.test"...
Running 1/1 test for "hello"...
❌The user is greeted

Channel `User (Ben Bitdiddle)` received output, but that output ("Hello, Ben Bitdiddle!") did not match what was expected ("Hello, Yasyf Mohamedali!")
```

Whoops! Without overriding the user's name, we get the default test value, which will not match our test. We could change the expected value to a regular expression that would match any name, but let's instead explore how to change the injected test data.

To inject a custom name for our test user, we simply use the `--context` CLI flag, passing in a JSON object to be merged into the default data.

```bash
CONTEXT='{"user": {"first_name": "Yasyf", last_name: "Mohamedali"}}'
sym flow test demo --context=$CONTEXT
```

```
Testing flow "demo.symflow"...
Running tests in "demo.symflow.test"...
Running 1/1 test for "hello"...
✅The user is greeted
```

Looks like that did it!

## Acceptance Testing

When running in acceptance testing mode, the Sym CLI simply takes in a set of inputs (or uses sane defaults if none are supplied), and adds a default `io` interface for every entity, which is the current terminal.

```bash
sym flow run demo --flow=hello --context=$CONTEXT
```

```
Running flow "hello" in "demo.symflow"...
> Hello, Yasyf Mohamedali!
```

**[Next: Deploying Your Workflow](06_deploy_flow.md)**
