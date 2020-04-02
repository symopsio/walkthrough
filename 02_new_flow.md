# Create a New Flow

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

We'll have to login before we can do anything else. For the purposes of this demo, we'll assume you're using our classic login flow, but Sym also supports SSO.

```bash
$ sym login
```

```
Sym Org: symops
Username: yasyfm
Password: ************
MFA Token: ******

Success! Welcome, Yasyf. 🤓
```

Next, let's create a new Sym Workflow called `demo`.

```bash
sym flow new demo
```

You'll notice that this creates a `demo` directory with two files: `events.yml` and `demo.symflow`.

**[Next: Define an Event](03_define_event.md)**
