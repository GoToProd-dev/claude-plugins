# `hcloud storage-box-type` — View Storage Box Types

Generated from `--help` output of hcloud 1.70.1. Global flags (--context, --config, --endpoint, --debug, --quiet, ...) apply to every command and are omitted here.

### `hcloud storage-box-type describe`

Describe a Storage Box Type

**Usage:**

```
hcloud storage-box-type describe [options] <storage-box-type>
```

**Flags:**

```
-o, --output stringArray   output options: json|yaml|format
```

### `hcloud storage-box-type list`

Displays a list of Storage Box Types.

Output can be controlled with the -o flag. Use -o noheader to suppress the
table header. Displayed columns and their order can be set with
-o columns=automatic_snapshot_limit,deprecated (see available columns below).

**Columns:** automatic_snapshot_limit, deprecated, description, id, name, size, snapshot_limit, subaccounts_limit

**Usage:**

```
hcloud storage-box-type list [options]
```

**Flags:**

```
-o, --output stringArray   output options: noheader|columns=...|json|yaml
-l, --selector string      Selector to filter by labels
-s, --sort strings         Determine the sorting of the result
```
