# `hcloud network` — Manage Networks

Generated from `--help` output of hcloud 1.70.1. Global flags (--context, --config, --endpoint, --debug, --quiet, ...) apply to every command and are omitted here.

### `hcloud network add-label`

Add a label to a Network

**Usage:**

```
hcloud network add-label [--overwrite] <network> <label>...
```

**Flags:**

```
-o, --overwrite   Overwrite label if it exists already (true, false)
```

### `hcloud network change-ip-range`

Change the IP range of a Network

**Usage:**

```
hcloud network change-ip-range --ip-range <ip-range> <network>
```

**Flags:**

```
    --ip-range ipNet   New IP range (required)
```

### `hcloud network create`

Create a Network

**Usage:**

```
hcloud network create [options] --name <name> --ip-range <ip-range>
```

**Flags:**

```
    --enable-protection strings   Enable protection (delete) (default: none)
    --expose-routes-to-vswitch    Expose routes from this Network to the vSwitch connection. It only takes effect if a vSwitch connection is active. (true, false)
    --ip-range ipNet              Network IP range (required)
    --label stringToString        User-defined labels ('key=value') (can be specified multiple times) (default [])
    --name string                 Network name (required)
-o, --output stringArray          output options: json|yaml
```

### `hcloud network delete`

Delete a network

**Usage:**

```
hcloud network delete <network>...
```

### `hcloud network describe`

Describe a Network

**Usage:**

```
hcloud network describe [options] <network>
```

**Flags:**

```
-o, --output stringArray   output options: json|yaml|format
```

### `hcloud network list`

Displays a list of Networks.

Output can be controlled with the -o flag. Use -o noheader to suppress the
table header. Displayed columns and their order can be set with
-o columns=age,created (see available columns below).

**Columns:** age, created, expose_routes_to_v_switch, id, ip_range, labels, name, protection, servers

**Usage:**

```
hcloud network list [options]
```

**Flags:**

```
-o, --output stringArray   output options: noheader|columns=...|json|yaml
-l, --selector string      Selector to filter by labels
-s, --sort strings         Determine the sorting of the result
```

### `hcloud network remove-label`

Remove a label from a Network

**Usage:**

```
hcloud network remove-label <network> (--all | <label>...)
```

**Flags:**

```
-a, --all    Remove all labels
```

### `hcloud network update`

Update a Network.

To enable or disable exposing routes to the vSwitch connection you can use the subcommand "hcloud network expose-routes-to-vswitch".

**Usage:**

```
hcloud network update [options] <network>
```

**Flags:**

```
    --name string   Network name
```

### `hcloud network disable-protection`

Disable resource protection for a Network

**Usage:**

```
hcloud network disable-protection <network> delete
```

### `hcloud network enable-protection`

Enable resource protection for a Network

**Usage:**

```
hcloud network enable-protection <network> delete
```

### `hcloud network add-route`

Add a route to a Network

**Usage:**

```
hcloud network add-route --destination <destination> --gateway <ip> <network>
```

**Flags:**

```
    --destination ipNet   Destination Network or host (required)
    --gateway ip          Gateway IP address (required)
```

### `hcloud network expose-routes-to-vswitch`

Enabling this will expose routes to the connected vSwitch. Set the --disable flag to remove the exposed routes.

**Usage:**

```
hcloud network expose-routes-to-vswitch [--disable] <network>
```

**Flags:**

```
    --disable   Remove any exposed routes from the connected vSwitch
```

### `hcloud network remove-route`

Remove a route from a Network

**Usage:**

```
hcloud network remove-route --destination <destination> --gateway <ip> <network>
```

**Flags:**

```
    --destination ipNet   Destination Network or host (required)
    --gateway ip          Gateway IP address (required)
```

### `hcloud network add-subnet`

Add a subnet to a Network

**Usage:**

```
hcloud network add-subnet [options] --type <cloud|server|vswitch> --network-zone <zone> <network>
```

**Flags:**

```
    --ip-range ipNet        Range to allocate IPs from
    --network-zone string   Name of Network zone (required)
    --type string           Type of subnet (required)
    --vswitch-id int        ID of the vSwitch
```

### `hcloud network remove-subnet`

Remove a subnet from a Network

**Usage:**

```
hcloud network remove-subnet --ip-range <ip-range> <network>
```

**Flags:**

```
    --ip-range ipNet   Subnet IP range (required)
```

### `hcloud network list-members`

Displays a list of Network Members.

Output can be controlled with the -o flag. Use -o noheader to suppress the
table header. Displayed columns and their order can be set with
-o columns=alias_ips,id (see available columns below).

**Columns:** alias_ips, id, ip, status, subnet, type

**Usage:**

```
hcloud network list-members [options] <network>
```

**Flags:**

```
-o, --output stringArray   output options: noheader|columns=...|json|yaml
-l, --selector string      Selector to filter by labels
-s, --sort strings         Determine the sorting of the result
    --status strings       Only Members with one of these statuses are displayed
    --subnet strings       Only Members attached to one of these subnets are displayed
    --type strings         Only Members with one of these types are displayed
```
