# `hcloud iso` — View ISOs

Generated from `--help` output of hcloud 1.70.1. Global flags (--context, --config, --endpoint, --debug, --quiet, ...) apply to every command and are omitted here.

### `hcloud iso describe`

Describe an ISO

**Usage:**

```
hcloud iso describe [options] <iso>
```

**Flags:**

```
-o, --output stringArray   output options: json|yaml|format
```

### `hcloud iso list`

Displays a list of ISOs.

Output can be controlled with the -o flag. Use -o noheader to suppress the
table header. Displayed columns and their order can be set with
-o columns=architecture,description (see available columns below).

**Columns:** architecture, description, id, name, type

**Usage:**

```
hcloud iso list [options]
```

**Flags:**

```
    --architecture strings            Only show Images of given architecture: x86|arm
    --include-architecture-wildcard   Include ISOs with unknown architecture, only required if you want so show custom ISOs and still filter for architecture. (true, false)
-o, --output stringArray              output options: noheader|columns=...|json|yaml
-l, --selector string                 Selector to filter by labels
-s, --sort strings                    Determine the sorting of the result
    --type strings                    Types to include (public, private) (default [public,private])
```
