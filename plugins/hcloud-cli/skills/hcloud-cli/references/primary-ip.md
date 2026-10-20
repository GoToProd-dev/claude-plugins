# `hcloud primary-ip` — Manage Primary IPs

Generated from `--help` output of hcloud 1.70.1. Global flags (--context, --config, --endpoint, --debug, --quiet, ...) apply to every command and are omitted here.

### `hcloud primary-ip add-label`

Add a label to a Primary IP

**Usage:**

```
hcloud primary-ip add-label [--overwrite] <primary-ip> <label>...
```

**Flags:**

```
-o, --overwrite   Overwrite label if it exists already (true, false)
```

### `hcloud primary-ip create`

Create a Primary IP.

The --datacenter flag has been removed. Use --location or --assignee-id instead.
See https://docs.hetzner.cloud/changelog#2026-07-01-removing-datacenters.

The --assignee-type flag will be required together with the --assignee-id flag. Using
the default value (server) for the --assignee-type flag is deprecated. Consider
explicitly setting the --assignee-type flag.

See https://docs.hetzner.cloud/changelog#2026-04-27-primary-ips-will-return-unassigned
and https://docs.hetzner.cloud/changelog#2026-04-27-primary-ips-make-assignee_type-optional.

**Usage:**

```
hcloud primary-ip create [options] --type <ipv4|ipv6> --name <name>
```

**Flags:**

```
    --assignee-id int             Assignee (usually a Server) to assign Primary IP to
    --assignee-type string        Assignee Type to assign Primary IP to (default: server) (default "server")
    --auto-delete                 Delete Primary IP if assigned resource is deleted (true, false)
    --enable-protection strings   Enable protection (delete) (default: none)
    --label stringToString        User-defined labels ('key=value') (can be specified multiple times) (default [])
    --location string             Location (ID or name) of Primary IP
    --name string                 Name (required)
-o, --output stringArray          output options: json|yaml
    --type string                 Type (ipv4 or ipv6) (required)
```

### `hcloud primary-ip delete`

Delete a Primary IP

**Usage:**

```
hcloud primary-ip delete <primary-ip>...
```

### `hcloud primary-ip describe`

Describe a Primary IP

**Usage:**

```
hcloud primary-ip describe [options] <primary-ip>
```

**Flags:**

```
-o, --output stringArray   output options: json|yaml|format
```

### `hcloud primary-ip list`

Displays a list of Primary IPs.

Output can be controlled with the -o flag. Use -o noheader to suppress the
table header. Displayed columns and their order can be set with
-o columns=age,assignee (see available columns below).

**Columns:** age, assignee, assignee_id, assignee_type, auto_delete, blocked, created, dns, id, ip, labels, name, protection, type

**Usage:**

```
hcloud primary-ip list [options]
```

**Flags:**

```
-o, --output stringArray   output options: noheader|columns=...|json|yaml
-l, --selector string      Selector to filter by labels
-s, --sort strings         Determine the sorting of the result
```

### `hcloud primary-ip remove-label`

Remove a label from a Primary IP

**Usage:**

```
hcloud primary-ip remove-label <primary-ip> (--all | <label>...)
```

**Flags:**

```
-a, --all    Remove all labels
```

### `hcloud primary-ip update`

Update a Primary IP

**Usage:**

```
hcloud primary-ip update [options] <primary-ip>
```

**Flags:**

```
    --auto-delete   Delete this Primary IP when the resource it is assigned to is deleted (true, false)
    --name string   Primary IP name
```

### `hcloud primary-ip disable-protection`

Disable resource protection for a Primary IP

**Usage:**

```
hcloud primary-ip disable-protection <primary-ip> [delete]
```

### `hcloud primary-ip enable-protection`

Enable resource protection for a Primary IP

**Usage:**

```
hcloud primary-ip enable-protection <primary-ip> [delete]
```

### `hcloud primary-ip assign`

Assign a Primary IP to an assignee (usually a Server)

**Usage:**

```
hcloud primary-ip assign --server <server> <primary-ip>
```

**Flags:**

```
    --server string   Name or ID of the Server
```

### `hcloud primary-ip unassign`

Unassign a Primary IP from an assignee (usually a server)

**Usage:**

```
hcloud primary-ip unassign <primary-ip>
```

### `hcloud primary-ip set-rdns`

Change reverse DNS of a Primary IP

**Usage:**

```
hcloud primary-ip set-rdns [--ip <ip>] (--hostname <hostname> | --reset) <primary-ip>
```

**Flags:**

```
-r, --hostname string   Hostname to set as a reverse DNS PTR entry
-i, --ip ip             IP address for which the reverse DNS entry should be set
    --reset             Reset the reverse DNS entry to the default value (true, false)
```
