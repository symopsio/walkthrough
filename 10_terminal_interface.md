# Offering a Terminal Interface

So far the only interface to our flow is Slack. In order to add a terminal interface to set temporary credentials on, we add a third call to `sym` in our `request.sh` script.

Please append this line to the script.

```bash
sym events receive $UUID
```

This will block on the triggered workflow's completion, and provide an interface for output.

**[Next: Putting It All Together!](11_all_together.md)**
