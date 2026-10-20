# `hcloud storage-box` — Manage Storage Boxes

Generated from `--help` output of hcloud 1.70.1. Global flags (--context, --config, --endpoint, --debug, --quiet, ...) apply to every command and are omitted here.

### `hcloud storage-box add-label`

Add a label to a Storage Box

**Usage:**

```
hcloud storage-box add-label [--overwrite] <storage-box> <label>...
```

**Flags:**

```
-o, --overwrite   Overwrite label if it exists already (true, false)
```

### `hcloud storage-box change-type`

Requests a Storage Box to be upgraded or downgraded to another Storage Box Type.
Please note that it is not possible to downgrade to a Storage Box Type that offers less disk space than you are currently using.

**Usage:**

```
hcloud storage-box change-type <storage-box> <storage-box-type>
```

### `hcloud storage-box create`

Create a new Storage Box

**Usage:**

```
hcloud storage-box create [options] --name <name> --type <type> --location <location> --password <password>
```

**Flags:**

```
    --enable-protection strings   Enable protection (delete) (default: none)
    --enable-samba                Whether the Samba subsystem should be enabled (true, false)
    --enable-ssh                  Whether the SSH subsystem should be enabled (true, false)
    --enable-webdav               Whether the WebDAV subsystem should be enabled (true, false)
    --enable-zfs                  Whether the ZFS Snapshot folder should be visible (true, false)
    --label stringToString        User-defined labels ('key=value') (can be specified multiple times) (default [])
    --location string             Location (ID or name) (required)
    --name string                 Storage Box name (required)
-o, --output stringArray          output options: json|yaml
    --password string             The password that will be set for this Storage Box (required)
    --reachable-externally        Whether the Storage Box should be accessible from outside the Hetzner network (true, false)
    --ssh-key stringArray         SSH public keys in OpenSSH format or as the ID or name of an existing SSH key
    --type string                 Storage Box Type (ID or name) (required)
```

### `hcloud storage-box delete`

Delete a Storage Box

**Usage:**

```
hcloud storage-box delete <storage-box>...
```

### `hcloud storage-box describe`

Describe a Storage Box

**Usage:**

```
hcloud storage-box describe [options] <storage-box>
```

**Flags:**

```
-o, --output stringArray   output options: json|yaml|format
```

### `hcloud storage-box folders`

List folders of a Storage Box

**Usage:**

```
hcloud storage-box folders <storage-box>
```

**Flags:**

```
-o, --output stringArray   output options: json|yaml
    --path string          Relative path for which the listing is to be made
```

### `hcloud storage-box list`

Displays a list of Storage Boxes.

Output can be controlled with the -o flag. Use -o noheader to suppress the
table header. Displayed columns and their order can be set with
-o columns=age,created (see available columns below).

**Columns:** age, created, id, labels, location, name, server, size, status, system, type, username

**Usage:**

```
hcloud storage-box list [options]
```

**Flags:**

```
-o, --output stringArray   output options: noheader|columns=...|json|yaml
-l, --selector string      Selector to filter by labels
-s, --sort strings         Determine the sorting of the result
```

### `hcloud storage-box remove-label`

Remove a label from a Storage Box

**Usage:**

```
hcloud storage-box remove-label <storage-box> (--all | <label>...)
```

**Flags:**

```
-a, --all    Remove all labels
```

### `hcloud storage-box update`

Update a Storage Box

**Usage:**

```
hcloud storage-box update [options] <storage-box>
```

**Flags:**

```
    --name string   Storage Box name
```

### `hcloud storage-box disable-protection`

Disable resource protection for a Storage Box

**Usage:**

```
hcloud storage-box disable-protection <storage-box> delete
```

### `hcloud storage-box enable-protection`

Enable resource protection for a Storage Box

**Usage:**

```
hcloud storage-box enable-protection <storage-box> delete
```

### `hcloud storage-box disable-snapshot-plan`

Disable automatic snapshots for a Storage Box

**Usage:**

```
hcloud storage-box disable-snapshot-plan <storage-box>
```

### `hcloud storage-box enable-snapshot-plan`

Enable automatic snapshots for a Storage Box

Allowed values for --day-of-week are:
- Sunday, Sun, 0, 7
- Monday, Mon, 1
- Tuesday, Tue, 2
- Wednesday, Wed, 3
- Thursday, Thu, 4
- Friday, Fri, 5
- Saturday, Sat, 6

**Usage:**

```
hcloud storage-box enable-snapshot-plan [options] <storage-box>
```

**Flags:**

```
    --day-of-month int     Day of the month the Snapshot Plan should be executed on. Not specified means every day
    --day-of-week string   Day of the week the Snapshot Plan should be executed on. Not specified means every day
    --hour int             Hour the Snapshot Plan should be executed on (UTC)
    --max-snapshots int    Maximum amount of Snapshots that should be created by this Snapshot Plan
    --minute int           Minute the Snapshot Plan should be executed on (UTC)
```

### `hcloud storage-box rollback-snapshot`

Rolls back the Storage Box to the given Snapshot

**Usage:**

```
hcloud storage-box rollback-snapshot --snapshot <snapshot> <storage-box>
```

**Flags:**

```
    --snapshot string   The name or ID of the snapshot to roll back to
```

### `hcloud storage-box snapshot add-label`

Add a label to a Storage Box Snapshot

**Usage:**

```
hcloud storage-box snapshot add-label [--overwrite] <storage-box> <snapshot> <label>...
```

**Flags:**

```
-o, --overwrite   Overwrite label if it exists already (true, false)
```

### `hcloud storage-box snapshot create`

Create a Storage Box Snapshot

**Usage:**

```
hcloud storage-box snapshot create [--description <description>] <storage-box>
```

**Flags:**

```
    --description string     Description of the Storage Box Snapshot
    --label stringToString   User-defined labels ('key=value') (can be specified multiple times) (default [])
-o, --output stringArray     output options: json|yaml
```

### `hcloud storage-box snapshot delete`

Delete a Storage Box Snapshot

**Usage:**

```
hcloud storage-box snapshot delete <storage-box> <snapshot>...
```

### `hcloud storage-box snapshot describe`

Describe a Storage Box Snapshot

**Usage:**

```
hcloud storage-box snapshot describe [options] <storage-box> <snapshot>
```

**Flags:**

```
-o, --output stringArray   output options: json|yaml|format
```

### `hcloud storage-box snapshot list`

Displays a list of Storage Box Snapshots.

Output can be controlled with the -o flag. Use -o noheader to suppress the
table header. Displayed columns and their order can be set with
-o columns=age,created (see available columns below).

**Columns:** age, created, description, id, is_automatic, labels, name, size, size_filesystem

**Usage:**

```
hcloud storage-box snapshot list [options] <storage-box>
```

**Flags:**

```
    --automatic            Only show automatic snapshots (true, false)
-o, --output stringArray   output options: noheader|columns=...|json|yaml
-l, --selector string      Selector to filter by labels
-s, --sort strings         Determine the sorting of the result
```

### `hcloud storage-box snapshot remove-label`

Remove a label from a Storage Box Snapshot

**Usage:**

```
hcloud storage-box snapshot remove-label <storage-box> <snapshot> (--all | <label>...)
```

**Flags:**

```
-a, --all    Remove all labels
```

### `hcloud storage-box snapshot update`

Update a Storage Box Snapshot

**Usage:**

```
hcloud storage-box snapshot update [options] <storage-box> <snapshot>
```

**Flags:**

```
    --description string   Description of the Storage Box Snapshot
```

### `hcloud storage-box reset-password`

Reset the password of a Storage Box

**Usage:**

```
hcloud storage-box reset-password --password <password> <storage-box>
```

**Flags:**

```
    --password string   New password for the Storage Box
```

### `hcloud storage-box subaccount change-home-directory`

Update access settings of the Storage Box Subaccount

**Usage:**

```
hcloud storage-box subaccount change-home-directory --home-directory <home-directory> <storage-box> <subaccount>
```

**Flags:**

```
    --home-directory string   Home directory of the Subaccount. Will be created if it doesn't exist yet
```

### `hcloud storage-box subaccount create`

Create a Storage Box Subaccount

**Usage:**

```
hcloud storage-box subaccount create [options] --password <password> --home-directory <home-directory> <storage-box>
```

**Flags:**

```
    --description string      Description for the Subaccount
    --enable-samba            Whether the Samba subsystem should be enabled (true, false)
    --enable-ssh              Whether the SSH subsystem should be enabled (true, false)
    --enable-webdav           Whether the WebDAV subsystem should be enabled (true, false)
    --home-directory string   Home directory for the Subaccount (required)
    --label stringToString    User-defined labels ('key=value') (can be specified multiple times) (default [])
    --name string             Name for the Subaccount
-o, --output stringArray      output options: json|yaml
    --password string         Password for the Subaccount (required)
    --reachable-externally    Whether the Storage Box should be accessible from outside the Hetzner network (true, false)
    --readonly                Whether the Subaccount should be read-only (true, false)
```

### `hcloud storage-box subaccount delete`

Delete a Storage Box Subaccount

**Usage:**

```
hcloud storage-box subaccount delete <storage-box> <subaccount>...
```

### `hcloud storage-box subaccount describe`

Describe a Storage Box Subaccount

**Usage:**

```
hcloud storage-box subaccount describe [options] <storage-box> <subaccount>
```

**Flags:**

```
-o, --output stringArray   output options: json|yaml|format
```

### `hcloud storage-box subaccount list`

Displays a list of Storage Box Subaccounts.

Output can be controlled with the -o flag. Use -o noheader to suppress the
table header. Displayed columns and their order can be set with
-o columns=age,created (see available columns below).

**Columns:** age, created, description, home_directory, id, labels, name, server, username

**Usage:**

```
hcloud storage-box subaccount list [options] <storage-box>
```

**Flags:**

```
-o, --output stringArray   output options: noheader|columns=...|json|yaml
-l, --selector string      Selector to filter by labels
-s, --sort strings         Determine the sorting of the result
```

### `hcloud storage-box subaccount reset-password`

Reset the password of a Storage Box Subaccount

**Usage:**

```
hcloud storage-box subaccount reset-password --password <password> <storage-box> <subaccount>
```

**Flags:**

```
    --password string   New password for the Storage Box Subaccount
```

### `hcloud storage-box subaccount update`

Update a Storage Box Subaccount

**Usage:**

```
hcloud storage-box subaccount update [options] <storage-box> <subaccount>
```

**Flags:**

```
    --description string   Description of the Storage Box Subaccount
    --name string          Name of the Storage Box Subaccount
```

### `hcloud storage-box subaccount update-access-settings`

Update access settings of the Storage Box Subaccount

**Usage:**

```
hcloud storage-box subaccount update-access-settings [options] <storage-box> <subaccount>
```

**Flags:**

```
    --enable-samba           Whether the Samba subsystem should be enabled (true, false)
    --enable-ssh             Whether the SSH subsystem should be enabled (true, false)
    --enable-webdav          Whether the WebDAV subsystem should be enabled (true, false)
    --reachable-externally   Whether the Storage Box should be accessible from outside the Hetzner network (true, false)
    --readonly               Whether the Subaccount should be read-only (true, false)
```

### `hcloud storage-box update-access-settings`

Update access settings of the primary Storage Box account

**Usage:**

```
hcloud storage-box update-access-settings [options] <storage-box>
```

**Flags:**

```
    --enable-samba           Whether the Samba subsystem should be enabled (true, false)
    --enable-ssh             Whether the SSH subsystem should be enabled (true, false)
    --enable-webdav          Whether the WebDAV subsystem should be enabled (true, false)
    --enable-zfs             Whether the ZFS Snapshot folder should be visible (true, false)
    --reachable-externally   Whether the Storage Box should be accessible from outside the Hetzner network (true, false)
```
