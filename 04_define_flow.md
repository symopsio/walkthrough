# Define a Workflow

Next, let's turn our attention to the `demo.symflow` file.

```bash
$ cat demo/demo.symflow
```

```symflow
import g, io

alias user = g.context.user

flow hello
  io.say(user, message: `Hello, #{user.name}!`)
end
```

### Imports

There's a few things to unpack here. First, the imports.

```symflow
import g, io
```

Import statements in Sym allow us to access external, pre-packaged logic. Here, we have two imports. The first, `g` allows us to access global state, such as the `context` of the current _run_ (execution) of the workflow. The second, `io`, gives us common utilities to interact with the outside world over common communication channels.

### Aliases

The next thing we see is an `alias`.

```symflow
alias user = g.context.user
```

You can think of an `alias` as a kind of compiler macro: the text on the RHS is simply pasted into place wherever the LHS is found in the remainder of the workflow.

The `alias` we see defined is a common one: `g.context.user` allows us access to the user who is responsible for the Event that kicked off the current run, and it is handy to simply refer to it as `user`.

### Flows

Finally, we turn our attention to the `flow` definition.

```symflow
flow hello
  io.say(user, message: `Hello, #{user.name}!`)
end
```

A `flow` is equivalent to a `function` in other languages: it is a packaged piece of code that can be named and invoked with arguments. Sym Workflows are lexically scoped, but a `flow` is not a closure: there are no variable bindings associated with it. The name of a `flow` must be unique within the file it is defined in.

In our starter file, we see a simple "Hello, World" flow which uses the `io` module to `say` a message to the current user. Since the Sym Slack Bot automatically provides an `io` location to the Sym Users service, this message will go to the `user` via a Slack DM.

**[Next: Deploying Your Workflow](05_deploy_flow.md)**
