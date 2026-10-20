# `hcloud server-type` — View Server Types

Generated from `--help` output of hcloud 1.70.1. Global flags (--context, --config, --endpoint, --debug, --quiet, ...) apply to every command and are omitted here.

### `hcloud server-type describe`

Describe a Server Type

**Usage:**

```
hcloud server-type describe [options] <server-type>
```

**Flags:**

```
-o, --output stringArray   output options: json|yaml|format
```

### `hcloud server-type list`

Displays a list of Server Types.

Output can be controlled with the -o flag. Use -o noheader to suppress the
table header. Displayed columns and their order can be set with
-o columns=architecture,category (see available columns below).

**Columns:** architecture, category, cores, cpu_type, deprecated, description, disk, id, included_traffic, location, location_available, location_recommended, memory, name, storage_type, traffic

**Usage:**

```
hcloud server-type list [options]
```

**Flags:**

```
-o, --output stringArray   output options: noheader|columns=...|json|yaml
-l, --selector string      Selector to filter by labels
-s, --sort strings         Determine the sorting of the result
```
