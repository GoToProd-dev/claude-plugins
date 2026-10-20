# `hcloud volume` — Manage Volumes

Generated from `--help` output of hcloud 1.70.1. Global flags (--context, --config, --endpoint, --debug, --quiet, ...) apply to every command and are omitted here.

### `hcloud volume add-label`

Add a label to a Volume

**Usage:**

```
hcloud volume add-label [--overwrite] <volume> <label>...
```

**Flags:**

```
-o, --overwrite   Overwrite label if it exists already (true, false)
```

### `hcloud volume create`

Create a Volume

**Usage:**

```
hcloud volume create [options] --name <name> --size <size>
```

**Flags:**

```
    --automount                   Automount Volume after attach (Server must be provided) (true, false)
    --enable-protection strings   Enable protection (delete) (default: none)
    --format string               Format Volume after creation (ext4 or xfs)
    --label stringToString        User-defined labels ('key=value') (can be specified multiple times) (default [])
    --location string             Location (ID or name)
    --name string                 Volume name (required)
-o, --output stringArray          output options: json|yaml
    --server string               Server (ID or name)
    --size int                    Size (GB) (required)
```

### `hcloud volume delete`

Delete a Volume

**Usage:**

```
hcloud volume delete <volume>...
```

### `hcloud volume describe`

Describe a Volume

**Usage:**

```
hcloud volume describe [options] <volume>
```

**Flags:**

```
-o, --output stringArray   output options: json|yaml|format
```

### `hcloud volume list`

Displays a list of Volumes.

Output can be controlled with the -o flag. Use -o noheader to suppress the
table header. Displayed columns and their order can be set with
-o columns=age,created (see available columns below).

**Columns:** age, created, id, labels, linux_device, location, name, protection, server, size, status

**Usage:**

```
hcloud volume list [options]
```

**Flags:**

```
-o, --output stringArray   output options: noheader|columns=...|json|yaml
-l, --selector string      Selector to filter by labels
-s, --sort strings         Determine the sorting of the result
```

### `hcloud volume remove-label`

Remove a label from a Volume

**Usage:**

```
hcloud volume remove-label <volume> (--all | <label>...)
```

**Flags:**

```
-a, --all    Remove all labels
```

### `hcloud volume resize`

Resize a volume

**Usage:**

```
hcloud volume resize --size <size> <volume>
```

**Flags:**

```
    --size int   New size (GB) of the Volume (required)
```

### `hcloud volume update`

Update a Volume

**Usage:**

```
hcloud volume update [options] <volume>
```

**Flags:**

```
    --name string   Volume name
```

### `hcloud volume disable-protection`

Disable resource protection for a Volume

**Usage:**

```
hcloud volume disable-protection <volume> delete
```

### `hcloud volume enable-protection`

Enable resource protection for a Volume

**Usage:**

```
hcloud volume enable-protection <volume> delete
```

### `hcloud volume attach`

Attach a Volume to a Server

**Usage:**

```
hcloud volume attach [--automount] --server <server> <volume>
```

**Flags:**

```
    --automount       Automount Volume after attach (true, false)
    --server string   Server (ID or name) (required)
```

### `hcloud volume detach`

Detach a Volume

**Usage:**

```
hcloud volume detach <volume>
```
