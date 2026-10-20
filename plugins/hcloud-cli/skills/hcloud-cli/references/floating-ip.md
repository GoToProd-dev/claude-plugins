# `hcloud floating-ip` — Manage Floating IPs

Generated from `--help` output of hcloud 1.70.1. Global flags (--context, --config, --endpoint, --debug, --quiet, ...) apply to every command and are omitted here.

### `hcloud floating-ip add-label`

Add a label to a Floating IP

**Usage:**

```
hcloud floating-ip add-label [--overwrite] <floating-ip> <label>...
```

**Flags:**

```
-o, --overwrite   Overwrite label if it exists already (true, false)
```

### `hcloud floating-ip create`

Create a Floating IP

**Usage:**

```
hcloud floating-ip create [options] --type <ipv4|ipv6> (--home-location <location> | --server <server>)
```

**Flags:**

```
    --description string          Description
    --enable-protection strings   Enable protection (delete) (default: none)
    --home-location string        Home Location
    --label stringToString        User-defined labels ('key=value') (can be specified multiple times) (default [])
    --name string                 Name
-o, --output stringArray          output options: json|yaml
    --server string               Server to assign Floating IP to
    --type string                 Type (ipv4 or ipv6) (required)
```

### `hcloud floating-ip delete`

Delete a Floating IP

**Usage:**

```
hcloud floating-ip delete <floating-ip>...
```

### `hcloud floating-ip describe`

Describe a Floating IP

**Usage:**

```
hcloud floating-ip describe [options] <floating-ip>
```

**Flags:**

```
-o, --output stringArray   output options: json|yaml|format
```

### `hcloud floating-ip list`

Displays a list of Floating IPs.

Output can be controlled with the -o flag. Use -o noheader to suppress the
table header. Displayed columns and their order can be set with
-o columns=age,blocked (see available columns below).

**Columns:** age, blocked, created, description, dns, home, id, ip, labels, name, protection, server, type

**Usage:**

```
hcloud floating-ip list [options]
```

**Flags:**

```
-o, --output stringArray   output options: noheader|columns=...|json|yaml
-l, --selector string      Selector to filter by labels
-s, --sort strings         Determine the sorting of the result
```

### `hcloud floating-ip remove-label`

Remove a label from a Floating IP

**Usage:**

```
hcloud floating-ip remove-label <floating-ip> (--all | <label>...)
```

**Flags:**

```
-a, --all    Remove all labels
```

### `hcloud floating-ip update`

Update a Floating IP

**Usage:**

```
hcloud floating-ip update [options] <floating-ip>
```

**Flags:**

```
    --description string   Floating IP description
    --name string          Floating IP name
```

### `hcloud floating-ip disable-protection`

Disable resource protection for a Floating IP

**Usage:**

```
hcloud floating-ip disable-protection <floating-ip> delete
```

### `hcloud floating-ip enable-protection`

Enable resource protection for a Floating IP

**Usage:**

```
hcloud floating-ip enable-protection <floating-ip> delete
```

### `hcloud floating-ip assign`

Assign a Floating IP to a server

**Usage:**

```
hcloud floating-ip assign <floating-ip> <server>
```

### `hcloud floating-ip unassign`

Unassign a Floating IP

**Usage:**

```
hcloud floating-ip unassign <floating-ip>
```

### `hcloud floating-ip set-rdns`

Change reverse DNS of a Floating IP

**Usage:**

```
hcloud floating-ip set-rdns [--ip <ip>] (--hostname <hostname> | --reset) <floating-ip>
```

**Flags:**

```
-r, --hostname string   Hostname to set as a reverse DNS PTR entry
-i, --ip ip             IP address for which the reverse DNS entry should be set
    --reset             Reset the reverse DNS entry to the default value (true, false)
```
