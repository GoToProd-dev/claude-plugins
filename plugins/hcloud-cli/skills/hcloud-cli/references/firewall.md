# `hcloud firewall` — Manage Firewalls

Generated from `--help` output of hcloud 1.70.1. Global flags (--context, --config, --endpoint, --debug, --quiet, ...) apply to every command and are omitted here.

### `hcloud firewall add-label`

Add a label to a Firewall

**Usage:**

```
hcloud firewall add-label [--overwrite] <firewall> <label>...
```

**Flags:**

```
-o, --overwrite   Overwrite label if it exists already (true, false)
```

### `hcloud firewall create`

Create a Firewall

**Usage:**

```
hcloud firewall create [options] --name <name>
```

**Flags:**

```
    --label stringToString   User-defined labels ('key=value') (can be specified multiple times) (default [])
    --name string            Name
-o, --output stringArray     output options: json|yaml
    --rules-file string      JSON file containing your routes (use - to read from stdin). The structure of the file needs to be the same as within the API: https://docs.hetzner.cloud/reference/cloud#firewalls-get-a-firewall
```

### `hcloud firewall delete`

Delete a Firewall

**Usage:**

```
hcloud firewall delete <firewall>...
```

### `hcloud firewall describe`

Describe a Firewall

**Usage:**

```
hcloud firewall describe [options] <firewall>
```

**Flags:**

```
-o, --output stringArray   output options: json|yaml|format
```

### `hcloud firewall list`

Displays a list of Firewalls.

Output can be controlled with the -o flag. Use -o noheader to suppress the
table header. Displayed columns and their order can be set with
-o columns=age,applied_to_count (see available columns below).

**Columns:** age, applied_to_count, created, id, labels, name, rules_count

**Usage:**

```
hcloud firewall list [options]
```

**Flags:**

```
-o, --output stringArray   output options: noheader|columns=...|json|yaml
-l, --selector string      Selector to filter by labels
-s, --sort strings         Determine the sorting of the result
```

### `hcloud firewall remove-label`

Remove a label from a Firewall

**Usage:**

```
hcloud firewall remove-label <firewall> (--all | <label>...)
```

**Flags:**

```
-a, --all    Remove all labels
```

### `hcloud firewall update`

Update a Firewall

**Usage:**

```
hcloud firewall update [options] <firewall>
```

**Flags:**

```
    --name string   Firewall name
```

### `hcloud firewall add-rule`

Add a single rule to a firewall

**Usage:**

```
hcloud firewall add-rule [options] (--direction in --source-ips <ips> | --direction out --destination-ips <ips>) (--protocol <tcp|udp> --port <port> | --protocol <icmp|esp|gre>) <firewall>
```

**Flags:**

```
    --description string        Description of the Firewall rule
    --destination-ips strings   Destination IPs (CIDR Notation) (required when direction is out)
    --direction string          Direction (in, out) (required)
    --port string               Port to which traffic will be allowed, only applicable for protocols TCP and UDP, you can specify port ranges, sample: 80-85
    --protocol string           Protocol (icmp, esp, gre, udp or tcp) (required)
    --source-ips strings        Source IPs (CIDR Notation) (required when direction is in)
```

### `hcloud firewall delete-rule`

Delete a single rule from a Firewall

**Usage:**

```
hcloud firewall delete-rule [options] (--direction in --source-ips <ips> | --direction out --destination-ips <ips>) (--protocol <tcp|udp> --port <port> | --protocol <icmp|esp|gre>) <firewall>
```

**Flags:**

```
    --description string        Description of the Firewall rule
    --destination-ips strings   Destination IPs (CIDR Notation) (required when direction is out)
    --direction string          Direction (in, out) (required)
    --port string               Port to which traffic will be allowed, only applicable for protocols TCP and UDP
    --protocol string           Protocol (icmp, esp, gre, udp or tcp) (required)
    --source-ips strings        Source IPs (CIDR Notation) (required when direction is in)
```

### `hcloud firewall replace-rules`

Replaces all rules from a Firewall from a file

**Usage:**

```
hcloud firewall replace-rules --rules-file <file> <firewall>
```

**Flags:**

```
    --rules-file string   JSON file containing your routes (use - to read from stdin). The structure of the file needs to be the same as within the API: https://docs.hetzner.cloud/reference/cloud#firewalls-get-a-firewall
```

### `hcloud firewall apply-to-resource`

Applies a Firewall to a single resource

**Usage:**

```
hcloud firewall apply-to-resource (--type server --server <server> | --type label_selector --label-selector <label-selector>) <firewall>
```

**Flags:**

```
-l, --label-selector string   Label Selector
    --server string           Server name of ID (required when type is server)
    --type string             Resource Type (server, label_selector) (required)
```

### `hcloud firewall remove-from-resource`

Removes a Firewall from a single resource

**Usage:**

```
hcloud firewall remove-from-resource (--type server --server <server> | --type label_selector --label-selector <label-selector>) <firewall>
```

**Flags:**

```
-l, --label-selector string   Label Selector
    --server string           Server name of ID (required when type is server)
    --type string             Resource Type (server) (required)
```
