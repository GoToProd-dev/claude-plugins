# `hcloud ssh-key` — Manage SSH Keys

Generated from `--help` output of hcloud 1.70.1. Global flags (--context, --config, --endpoint, --debug, --quiet, ...) apply to every command and are omitted here.

### `hcloud ssh-key add-label`

Add a label to an SSH Key

**Usage:**

```
hcloud ssh-key add-label [--overwrite] <ssh-key> <label>...
```

**Flags:**

```
-o, --overwrite   Overwrite label if it exists already (true, false)
```

### `hcloud ssh-key create`

Create an SSH Key

**Usage:**

```
hcloud ssh-key create [options] --name <name> (--public-key <key> | --public-key-from-file <file>)
```

**Flags:**

```
    --label stringToString          User-defined labels ('key=value') (can be specified multiple times) (default [])
    --name string                   Key name (required)
-o, --output stringArray            output options: json|yaml
    --public-key string             Public key
    --public-key-from-file string   Path to file containing public key
```

### `hcloud ssh-key delete`

Delete an SSH Key

**Usage:**

```
hcloud ssh-key delete <ssh-key>...
```

### `hcloud ssh-key describe`

Describe an SSH Key

**Usage:**

```
hcloud ssh-key describe [options] <ssh-key>
```

**Flags:**

```
-o, --output stringArray   output options: json|yaml|format
```

### `hcloud ssh-key list`

Displays a list of SSH Keys.

Output can be controlled with the -o flag. Use -o noheader to suppress the
table header. Displayed columns and their order can be set with
-o columns=age,created (see available columns below).

**Columns:** age, created, fingerprint, id, labels, name, public_key

**Usage:**

```
hcloud ssh-key list [options]
```

**Flags:**

```
-o, --output stringArray   output options: noheader|columns=...|json|yaml
-l, --selector string      Selector to filter by labels
-s, --sort strings         Determine the sorting of the result
```

### `hcloud ssh-key remove-label`

Remove a label from an SSH Key

**Usage:**

```
hcloud ssh-key remove-label <ssh-key> (--all | <label>...)
```

**Flags:**

```
-a, --all    Remove all labels
```

### `hcloud ssh-key update`

Update an SSH Key

**Usage:**

```
hcloud ssh-key update [options] <ssh-key>
```

**Flags:**

```
    --name string   SSH Key name
```
