# `hcloud server` — Manage Servers

Generated from `--help` output of hcloud 1.70.1. Global flags (--context, --config, --endpoint, --debug, --quiet, ...) apply to every command and are omitted here.

### `hcloud server add-label`

Add a label to a Server

**Usage:**

```
hcloud server add-label [--overwrite] <server> <label>...
```

**Flags:**

```
-o, --overwrite   Overwrite label if it exists already (true, false)
```

### `hcloud server change-type`

Change type of a server

**Usage:**

```
hcloud server change-type [--keep-disk] <server> <server-type>
```

**Flags:**

```
    --keep-disk   Keep disk size of current Server Type. This enables downgrading the server. (true, false)
```

### `hcloud server create`

Create a Server.

The --datacenter flag has been removed. Use --location instead.
See https://docs.hetzner.cloud/changelog#2026-07-01-removing-datacenters.

**Usage:**

```
hcloud server create [options] --name <name> --type <server-type> --image <image>
```

**Flags:**

```
    --allow-deprecated-image            Enable the use of deprecated Images (default: false) (true, false)
    --automount                         Automount Volumes after attach (default: false) (true, false)
    --enable-backup                     Enable automatic backups (true, false)
    --enable-protection strings         Enable protection (delete, rebuild) (default: none)
    --firewall strings                  ID or name of Firewall to attach the Server to (can be specified multiple times)
    --image string                      Image (ID or name) (required)
    --label stringToString              User-defined labels ('key=value') (can be specified multiple times) (default [])
    --location string                   Location (ID or name)
    --name string                       Server name (required)
    --network strings                   ID or name of Network to attach the Server to (can be specified multiple times)
-o, --output stringArray                output options: json|yaml
    --placement-group string            Placement Group (ID of name)
    --primary-ipv4 string               Primary IPv4 (ID of name)
    --primary-ipv6 string               Primary IPv6 (ID of name)
    --ssh-key strings                   ID or name of SSH Key to inject (can be specified multiple times)
    --start-after-create                Start Server right after creation (true, false) (default true)
    --type string                       Server Type (ID or name) (required)
    --user-data-from-file stringArray   Read user data from specified file (use - to read from stdin)
    --volume strings                    ID or name of Volume to attach (can be specified multiple times)
    --without-ipv4                      Creates the Server without an IPv4 (default: false) (true, false)
    --without-ipv6                      Creates the Server without an IPv6 (default: false) (true, false)
```

### `hcloud server create-image`

Create an Image from a Server

**Usage:**

```
hcloud server create-image [options] --type <snapshot|backup> <server>
```

**Flags:**

```
    --description string     Image description
    --label stringToString   User-defined labels ('key=value') (can be specified multiple times) (default [])
    --type string            Image type (backup, snapshot) (required)
```

### `hcloud server delete`

Delete a server

**Usage:**

```
hcloud server delete <server>...
```

### `hcloud server describe`

Describe a Server

**Usage:**

```
hcloud server describe [options] <server>
```

**Flags:**

```
-o, --output stringArray   output options: json|yaml|format
```

### `hcloud server list`

Displays a list of Servers.

Output can be controlled with the -o flag. Use -o noheader to suppress the
table header. Displayed columns and their order can be set with
-o columns=age,backup_window (see available columns below).

**Columns:** age, backup_window, created, id, included_traffic, ingoing_traffic, ipv4, ipv6, labels, location, locked, name, outgoing_traffic, placement_group, primary_disk_size, private_net, protection, rescue_enabled, status, type, volumes

**Usage:**

```
hcloud server list [options]
```

**Flags:**

```
-o, --output stringArray   output options: noheader|columns=...|json|yaml
-l, --selector string      Selector to filter by labels
-s, --sort strings         Determine the sorting of the result
    --status strings       Only Servers with one of these statuses are displayed
```

### `hcloud server rebuild`

Rebuild a server

**Usage:**

```
hcloud server rebuild [options] --image <image> <server>
```

**Flags:**

```
    --allow-deprecated-image            Enable the use of deprecated images (default: false) (true, false)
    --image string                      ID or name of Image to rebuild from (required)
    --user-data-from-file stringArray   Read user data from specified file (use - to read from stdin)
```

### `hcloud server remove-label`

Remove a label from a Server

**Usage:**

```
hcloud server remove-label <server> (--all | <label>...)
```

**Flags:**

```
-a, --all    Remove all labels
```

### `hcloud server update`

Update a Server

**Usage:**

```
hcloud server update [options] <server>
```

**Flags:**

```
    --name string   Server name
```

### `hcloud server disable-protection`

Disable resource protection for a Server

**Usage:**

```
hcloud server disable-protection <server> (delete|rebuild)...
```

### `hcloud server enable-protection`

Enable resource protection for a Server

**Usage:**

```
hcloud server enable-protection <server> (delete|rebuild)...
```

### `hcloud server disable-rescue`

Disable rescue for a server

**Usage:**

```
hcloud server disable-rescue <server>
```

### `hcloud server enable-rescue`

Enable rescue for a server

**Usage:**

```
hcloud server enable-rescue [options] <server>
```

**Flags:**

```
    --ssh-key strings   ID or name of SSH Key to inject (can be specified multiple times)
    --type string       Rescue type (default "linux64")
```

### `hcloud server poweroff`

Poweroff a Server

**Usage:**

```
hcloud server poweroff <server>
```

### `hcloud server poweron`

Poweron a server

**Usage:**

```
hcloud server poweron <server>
```

### `hcloud server reboot`

Reboot a server

**Usage:**

```
hcloud server reboot <server>
```

### `hcloud server reset`

Reset a Server

**Usage:**

```
hcloud server reset [options] <server>
```

### `hcloud server shutdown`

Shuts down a Server gracefully by sending an ACPI shutdown request. The Server operating system must support ACPI and react to the request, otherwise the Server will not shut down. Use the --wait flag to wait for the Server to shut down before returning.

**Usage:**

```
hcloud server shutdown [options] <server>
```

**Flags:**

```
    --wait                    Wait for the Server to shut down before exiting (true, false)
    --wait-timeout duration   Timeout for waiting for off state after shutdown (default 30s)
```

### `hcloud server attach-to-network`

Attach a Server to a Network

**Usage:**

```
hcloud server attach-to-network [options] --network <network> <server>
```

**Flags:**

```
    --alias-ips ipSlice   Additional IP addresses to be assigned to the Server (default [])
    --ip ip               IP address to assign to the Server (auto-assigned if omitted)
    --ip-range ipNet      IP range in CIDR block notation of the subnet to attach to (auto-assigned if omitted)
-n, --network string      Network (ID or name) (required)
```

### `hcloud server change-alias-ips`

Change a server's alias IPs in a Network

**Usage:**

```
hcloud server change-alias-ips [options] --network <network> <server>
```

**Flags:**

```
    --alias-ips strings   New alias IPs
    --clear               Remove all alias IPs
-n, --network string      Network (ID or name) (required)
```

### `hcloud server detach-from-network`

Detach a Server from a Network

**Usage:**

```
hcloud server detach-from-network --network <network> <server>
```

**Flags:**

```
-n, --network string   Network (ID or name) (required)
```

### `hcloud server attach-iso`

Attach an ISO to a server

**Usage:**

```
hcloud server attach-iso <server> <iso>
```

### `hcloud server detach-iso`

Detach an ISO from a Server

**Usage:**

```
hcloud server detach-iso <server>
```

### `hcloud server add-to-placement-group`

Add a Server to a Placement Group

**Usage:**

```
hcloud server add-to-placement-group --placement-group <placement-group> <server>
```

**Flags:**

```
-g, --placement-group string   Placement Group (ID or name) (required)
```

### `hcloud server remove-from-placement-group`

Removes a Server from a Placement Group

**Usage:**

```
hcloud server remove-from-placement-group <server>
```

### `hcloud server disable-backup`

Disable backup for a server

**Usage:**

```
hcloud server disable-backup <server>
```

### `hcloud server enable-backup`

Enable backup for a server

**Usage:**

```
hcloud server enable-backup <server>
```

**Flags:**

```
    --window string   (deprecated) The time window for the daily backup to run. All times are in UTC. 22-02 means that the backup will be started between 10 PM and 2 AM.
```

### `hcloud server ip`

Print a server's IP address

**Usage:**

```
hcloud server ip [--ipv6] <server>
```

**Flags:**

```
-6, --ipv6   Print the first address of the Server's Primary IPv6 network
```

### `hcloud server metrics`

[ALPHA] Metrics from a Server

**Usage:**

```
hcloud server metrics [options] (--type <cpu|disk|network>)... <server>
```

**Flags:**

```
    --end string           ISO 8601 timestamp
-o, --output stringArray   output options: json|yaml
    --start string         ISO 8601 timestamp
    --type strings         Types of metrics you want to show
```

### `hcloud server request-console`

Request a WebSocket VNC console for a Server

**Usage:**

```
hcloud server request-console [options] <server>
```

**Flags:**

```
-o, --output stringArray   output options: json|yaml
```

### `hcloud server reset-password`

Reset the root password of a Server

**Usage:**

```
hcloud server reset-password [options] <server>
```

**Flags:**

```
-o, --output stringArray   output options: json|yaml
```

### `hcloud server set-rdns`

Change reverse DNS of a Server

**Usage:**

```
hcloud server set-rdns [--ip <ip>] (--hostname <hostname> | --reset) <server>
```

**Flags:**

```
-r, --hostname string   Hostname to set as a reverse DNS PTR entry
-i, --ip ip             IP address for which the reverse DNS entry should be set
    --reset             Reset the reverse DNS entry to the default value (true, false)
```

### `hcloud server ssh`

Spawn an SSH connection for the Server

**Usage:**

```
hcloud server ssh [options] <server> [--] [ssh options] [command [argument...]]
```

**Flags:**

```
    --ipv6          Establish SSH connection to IPv6 address (true, false)
-p, --port int      Port for SSH connection (default 22)
-u, --user string   Username for SSH connection (default "root")
```
