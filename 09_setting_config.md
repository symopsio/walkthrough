# Setting a Config Value

We need to set the value of `g.config.channel`. This is very simple to do with the Sym CLI.

```bash
$ sym config set --flow=demo --key=channel --value="#eng"
```

```json
{
  "type": "config",
  "name": "channel",
  "fqn": "config:symops:yasyfm:demo:channel",
  "value": "#eng"
}
```

**[Next: Offering a Terminal Interface](10_terminal_interface.md)**
