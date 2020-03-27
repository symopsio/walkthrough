# Offering a Terminal Interface

Currently, the only interface available to our flow for our user is Slack. In order for our flow to have a terminal interface to set temporary credentials on, we add a third call to `sym` to our `request.sh` script.

Please append this line to the script.

```bash
sym events receive $UUID
```

This will block on the triggered workflow's completion, and provide an interface for output.

**[Next: Putting It All Together!](10_all_together.md)**
