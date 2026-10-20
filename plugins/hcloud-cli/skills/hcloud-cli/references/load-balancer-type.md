# `hcloud load-balancer-type` — View Load Balancer Types

Generated from `--help` output of hcloud 1.70.1. Global flags (--context, --config, --endpoint, --debug, --quiet, ...) apply to every command and are omitted here.

### `hcloud load-balancer-type describe`

Describe a Load Balancer Type

**Usage:**

```
hcloud load-balancer-type describe [options] <load-balancer-type>
```

**Flags:**

```
-o, --output stringArray   output options: json|yaml|format
```

### `hcloud load-balancer-type list`

Displays a list of Load Balancer Types.

Output can be controlled with the -o flag. Use -o noheader to suppress the
table header. Displayed columns and their order can be set with
-o columns=deprecated,description (see available columns below).

**Columns:** deprecated, description, id, max_assigned_certificates, max_connections, max_services, max_targets, name

**Usage:**

```
hcloud load-balancer-type list [options]
```

**Flags:**

```
-o, --output stringArray   output options: noheader|columns=...|json|yaml
-l, --selector string      Selector to filter by labels
-s, --sort strings         Determine the sorting of the result
```
