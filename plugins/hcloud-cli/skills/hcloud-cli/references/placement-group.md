# `hcloud placement-group` — Manage Placement Groups

Generated from `--help` output of hcloud 1.70.1. Global flags (--context, --config, --endpoint, --debug, --quiet, ...) apply to every command and are omitted here.

### `hcloud placement-group add-label`

Add a label to a Placement Group

**Usage:**

```
hcloud placement-group add-label [--overwrite] <placement-group> <label>...
```

**Flags:**

```
-o, --overwrite   Overwrite label if it exists already (true, false)
```

### `hcloud placement-group create`

Create a Placement Group

**Usage:**

```
hcloud placement-group create [options] --name <name> --type <type>
```

**Flags:**

```
    --label stringToString   User-defined labels ('key=value') (can be specified multiple times) (default [])
    --name string            Name
-o, --output stringArray     output options: json|yaml
    --type string            Type of the Placement Group
```

### `hcloud placement-group delete`

Delete a Placement Group

**Usage:**

```
hcloud placement-group delete <placement-group>...
```

### `hcloud placement-group describe`

Describe a Placement Group

**Usage:**

```
hcloud placement-group describe [options] <placement-group>
```

**Flags:**

```
-o, --output stringArray   output options: json|yaml|format
```

### `hcloud placement-group list`

Displays a list of Placement Groups.

Output can be controlled with the -o flag. Use -o noheader to suppress the
table header. Displayed columns and their order can be set with
-o columns=age,created (see available columns below).

**Columns:** age, created, id, name, servers, type

**Usage:**

```
hcloud placement-group list [options]
```

**Flags:**

```
-o, --output stringArray   output options: noheader|columns=...|json|yaml
-l, --selector string      Selector to filter by labels
-s, --sort strings         Determine the sorting of the result
```

### `hcloud placement-group remove-label`

Remove a label from a Placement Group

**Usage:**

```
hcloud placement-group remove-label <placement-group> (--all | <label>...)
```

**Flags:**

```
-a, --all    Remove all labels
```

### `hcloud placement-group update`

Update a Placement Group

**Usage:**

```
hcloud placement-group update [options] <placement-group>
```

**Flags:**

```
    --name string   Placement Group name
```
