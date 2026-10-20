# `hcloud image` — Manage Images

Generated from `--help` output of hcloud 1.70.1. Global flags (--context, --config, --endpoint, --debug, --quiet, ...) apply to every command and are omitted here.

### `hcloud image add-label`

Add a label to an Image

**Usage:**

```
hcloud image add-label [--overwrite] <image> <label>...
```

**Flags:**

```
-o, --overwrite   Overwrite label if it exists already (true, false)
```

### `hcloud image delete`

Delete an Image

**Usage:**

```
hcloud image delete <image>...
```

### `hcloud image describe`

Describe an Image

**Usage:**

```
hcloud image describe [options] <image>
```

**Flags:**

```
-a, --architecture string   architecture of the Image, default is x86 (default "x86")
-o, --output stringArray    output options: json|yaml|format
```

### `hcloud image list`

Displays a list of Images.

Output can be controlled with the -o flag. Use -o noheader to suppress the
table header. Displayed columns and their order can be set with
-o columns=age,architecture (see available columns below).

**Columns:** age, architecture, bound_to, created, created_from, deprecated, description, disk_size, id, image_size, labels, name, os_flavor, os_version, protection, rapid_deploy, status, type

**Usage:**

```
hcloud image list [options]
```

**Flags:**

```
-a, --architecture strings   Only show Images of given architecture: x86|arm
-o, --output stringArray     output options: noheader|columns=...|json|yaml
-l, --selector string        Selector to filter by labels
-s, --sort strings           Determine the sorting of the result
-t, --type strings           Only show Images of given type: system|app|snapshot|backup
```

### `hcloud image remove-label`

Remove a label from an Image

**Usage:**

```
hcloud image remove-label <image> (--all | <label>...)
```

**Flags:**

```
-a, --all    Remove all labels
```

### `hcloud image update`

Update an Image

**Usage:**

```
hcloud image update [options] <image>
```

**Flags:**

```
    --description string   Image description
    --type string          Image type
```

### `hcloud image disable-protection`

Disable resource protection for an Image

**Usage:**

```
hcloud image disable-protection <image> delete
```

### `hcloud image enable-protection`

Enable resource protection for an Image

**Usage:**

```
hcloud image enable-protection <image> delete
```
