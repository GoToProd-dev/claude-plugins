# `hcloud location` — View Locations

Generated from `--help` output of hcloud 1.70.1. Global flags (--context, --config, --endpoint, --debug, --quiet, ...) apply to every command and are omitted here.

### `hcloud location describe`

Describe a Location

**Usage:**

```
hcloud location describe [options] <location>
```

**Flags:**

```
-o, --output stringArray   output options: json|yaml|format
```

### `hcloud location list`

Displays a list of Locations.

Output can be controlled with the -o flag. Use -o noheader to suppress the
table header. Displayed columns and their order can be set with
-o columns=city,country (see available columns below).

**Columns:** city, country, description, id, latitude, longitude, name, network_zone

**Usage:**

```
hcloud location list [options]
```

**Flags:**

```
-o, --output stringArray   output options: noheader|columns=...|json|yaml
-l, --selector string      Selector to filter by labels
-s, --sort strings         Determine the sorting of the result
```
