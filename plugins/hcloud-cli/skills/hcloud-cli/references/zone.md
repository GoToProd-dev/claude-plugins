# `hcloud zone` — Manage DNS Zones and Zone RRSets (records)

Generated from `--help` output of hcloud 1.70.1. Global flags (--context, --config, --endpoint, --debug, --quiet, ...) apply to every command and are omitted here.

### `hcloud zone add-label`

Add a label to a Zone

**Usage:**

```
hcloud zone add-label [--overwrite] <zone> <label>...
```

**Flags:**

```
-o, --overwrite   Overwrite label if it exists already (true, false)
```

### `hcloud zone change-primary-nameservers`

Changes the primary nameservers of a secondary Zone.

Input file has to be in JSON format. You can find the schema at
https://docs.hetzner.cloud/reference/cloud#zone-actions-change-a-zones-primary-nameservers

**Example file content:**

```
[
{
  "address": "203.0.113.10"
},
{
  "address": "203.0.113.11",
  "port": 5353
},
{
  "address": "203.0.113.12",
  "tsig_algorithm": "hmac-sha256",
  "tsig_key": "example-key"
}
]
```

**Usage:**

```
hcloud zone change-primary-nameservers --primary-nameservers-file <file> <zone>
```

**Flags:**

```
    --primary-nameservers-file string   JSON file containing the new primary nameservers. (use - to read from stdin)
```

### `hcloud zone change-ttl`

Changes the default Time To Live (TTL) of a Zone

**Usage:**

```
hcloud zone change-ttl --ttl <ttl> <zone>
```

**Flags:**

```
    --ttl int   Default Time To Live (TTL) of the Zone (required) (default 3600)
```

### `hcloud zone create`

Create a Zone

**Usage:**

```
hcloud zone create [options] --name <name> [--mode secondary --primary-nameservers <file>]
```

**Flags:**

```
    --enable-protection strings         Enable protection (delete) (default: none)
    --label stringToString              User-defined labels ('key=value') (can be specified multiple times) (default [])
    --mode string                       Mode of the Zone (primary, secondary) (default "primary")
    --name string                       Zone name (required)
-o, --output stringArray                output options: json|yaml
    --primary-nameservers-file string   JSON file containing the new primary nameservers. (See 'hcloud zone change-primary-nameservers -h' for help)
    --ttl int                           Default Time To Live (TTL) of the Zone
    --zonefile string                   Zone file in BIND (RFC 1034/1035) format (use - to read from stdin)
```

### `hcloud zone delete`

Delete a Zone

**Usage:**

```
hcloud zone delete <zone>...
```

### `hcloud zone describe`

Describe a Zone

**Usage:**

```
hcloud zone describe [options] <zone>
```

**Flags:**

```
-o, --output stringArray   output options: json|yaml|format
```

### `hcloud zone list`

Displays a list of Zones.

Output can be controlled with the -o flag. Use -o noheader to suppress the
table header. Displayed columns and their order can be set with
-o columns=age,authoritative_nameservers (see available columns below).

**Columns:** age, authoritative_nameservers, created, id, labels, mode, name, name_idna, primary_nameservers, protection, record_count, registrar, status, ttl

**Usage:**

```
hcloud zone list [options]
```

**Flags:**

```
    --mode string          Only Zones with this mode are displayed
-o, --output stringArray   output options: noheader|columns=...|json|yaml
-l, --selector string      Selector to filter by labels
-s, --sort strings         Determine the sorting of the result
```

### `hcloud zone remove-label`

Remove a label from a Zone

**Usage:**

```
hcloud zone remove-label <zone> (--all | <label>...)
```

**Flags:**

```
-a, --all    Remove all labels
```

### `hcloud zone disable-protection`

Disable resource protection for a Zone

**Usage:**

```
hcloud zone disable-protection <zone> delete
```

### `hcloud zone enable-protection`

Enable resource protection for a Zone

**Usage:**

```
hcloud zone enable-protection <zone> delete
```

### `hcloud zone export-zonefile`

Returns a generated Zone file in BIND (RFC 1034/1035) format

**Usage:**

```
hcloud zone export-zonefile [options] <zone>
```

**Flags:**

```
-o, --output stringArray   output options: json|yaml
```

### `hcloud zone import-zonefile`

Imports a zone file, replacing all Zone RRSets

**Usage:**

```
hcloud zone import-zonefile --zonefile <file> <zone>
```

**Flags:**

```
-o, --output stringArray   output options: json|yaml
    --zonefile string      Zone file in BIND (RFC 1034/1035) format (use - to read from stdin)
```

### `hcloud zone add-records`

Add records to a Zone RRSet.

If the Zone RRSet doesn't exist, it will automatically be created.

The optional records file has to be in JSON format. You can find the schema at https://docs.hetzner.cloud/reference/cloud#zone-rrset-actions-set-records-of-an-rrset

**Example file content:**

```
[
{
  "value": "198.51.100.1",
  "comment": "My web server at Hetzner Cloud."
},
{
  "value": "198.51.100.2",
  "comment": "My other server at Hetzner Cloud."
}
]
```

**Usage:**

```
hcloud zone add-records (--record <value>... | --records-file <file>) <zone> <name> <type>
```

**Flags:**

```
    --record stringArray    List of records (can be specified multiple times, conflicts with --records-file)
    --records-file string   JSON file containing the records (conflicts with --record)
    --ttl int               Time To Live (TTL) of the Zone RRSet
```

### `hcloud zone remove-records`

Remove records from a Zone RRSet.

If the Zone RRSet doesn't contain any records, it will automatically be deleted.

The optional records file has to be in JSON format. You can find the schema at https://docs.hetzner.cloud/reference/cloud#zone-rrset-actions-set-records-of-an-rrset

**Example file content:**

```
[
{
  "value": "198.51.100.1",
  "comment": "My web server at Hetzner Cloud."
},
{
  "value": "198.51.100.2",
  "comment": "My other server at Hetzner Cloud."
}
]
```

**Usage:**

```
hcloud zone remove-records (--record <value>... | --records-file <file>) <zone> <name> <type>
```

**Flags:**

```
    --record stringArray    List of records (can be specified multiple times, conflicts with --records-file)
    --records-file string   JSON file containing the records (conflicts with --record)
```

## `hcloud zone rrset`

```
For more details, see the documentation for Zones https://docs.hetzner.cloud/reference/cloud#zones
or Zone RRSets https://docs.hetzner.cloud/reference/cloud#zone-rrsets.

TXT records format must consist of one or many quoted strings of 255 characters. If the
user provider TXT records are not quoted, they will be formatted for you.
```

### `hcloud zone rrset add-label`

Add a label to a Zone RRSet

**Usage:**

```
hcloud zone rrset add-label [--overwrite] <zone> <name> <type> <label>...
```

**Flags:**

```
-o, --overwrite   Overwrite label if it exists already (true, false)
```

### `hcloud zone rrset change-ttl`

Changes the Time To Live (TTL) of a Zone RRSet

**Usage:**

```
hcloud zone rrset change-ttl (--ttl <ttl> | --unset) <zone> <name> <type>
```

**Flags:**

```
    --ttl int   Time To Live (TTL) of the Zone RRSet (required)
    --unset     Unset the Time To Live of Zone RRSet (use the Zone default TTL instead)
```

### `hcloud zone rrset create`

Create a Zone RRSet.

The optional records file has to be in JSON format. You can find the schema at https://docs.hetzner.cloud/reference/cloud#zone-rrset-actions-set-records-of-an-rrset

**Example file content:**

```
[
{
  "value": "198.51.100.1",
  "comment": "My web server at Hetzner Cloud."
},
{
  "value": "198.51.100.2",
  "comment": "My other server at Hetzner Cloud."
}
]
```

**Usage:**

```
hcloud zone rrset create [options] --name <name> --type <A|AAAA|CAA|CNAME|DS|HINFO|HTTPS|MX|NS|PTR|RP|SOA|SRV|SVCB|TLSA|TXT> (--record <record>... | --records-file <file>) <zone>
```

**Flags:**

```
    --label stringToString   User-defined labels ('key=value') (can be specified multiple times) (default [])
    --name string            Name of the Zone RRSet (required)
-o, --output stringArray     output options: json|yaml
    --record stringArray     List of records (can be specified multiple times, conflicts with --records-file)
    --records-file string    JSON file containing the records (conflicts with --record)
    --ttl int                Time To Live (TTL) of the RRSet
    --type string            Type of the Zone RRSet (required)
```

### `hcloud zone rrset delete`

Delete a Zone RRSet

**Usage:**

```
hcloud zone rrset delete <zone> <name> <type>
```

### `hcloud zone rrset describe`

Describe a Zone RRSet

**Usage:**

```
hcloud zone rrset describe [options] <zone> <name> <type>
```

**Flags:**

```
-o, --output stringArray   output options: json|yaml|format
```

### `hcloud zone rrset list`

Displays a list of Zone RRSets.

Output can be controlled with the -o flag. Use -o noheader to suppress the
table header. Displayed columns and their order can be set with
-o columns=id,labels (see available columns below).

**Columns:** id, labels, name, protection, records, ttl, type

**Usage:**

```
hcloud zone rrset list [options] <zone>
```

**Flags:**

```
-o, --output stringArray   output options: noheader|columns=...|json|yaml
-l, --selector string      Selector to filter by labels
-s, --sort strings         Determine the sorting of the result
    --type strings         Only Zone RRSets with one of these types are displayed
```

### `hcloud zone rrset remove-label`

Remove a label from a Zone RRSet

**Usage:**

```
hcloud zone rrset remove-label <zone> <name> <type> (--all | <label>...)
```

**Flags:**

```
-a, --all    Remove all labels
```

### `hcloud zone rrset disable-protection`

Disable resource protection for a Zone RRSet

**Usage:**

```
hcloud zone rrset disable-protection <zone> <name> <type> change
```

### `hcloud zone rrset enable-protection`

Enable resource protection for a Zone RRSet

**Usage:**

```
hcloud zone rrset enable-protection <zone> <name> <type> change
```

### `hcloud zone rrset add-records`

Add records to a Zone RRSet.

If the Zone RRSet doesn't exist, it will automatically be created.

The optional records file has to be in JSON format. You can find the schema at https://docs.hetzner.cloud/reference/cloud#zone-rrset-actions-set-records-of-an-rrset

**Example file content:**

```
[
{
  "value": "198.51.100.1",
  "comment": "My web server at Hetzner Cloud."
},
{
  "value": "198.51.100.2",
  "comment": "My other server at Hetzner Cloud."
}
]
```

**Usage:**

```
hcloud zone rrset add-records (--record <value>... | --records-file <file>) <zone> <name> <type>
```

**Flags:**

```
    --record stringArray    List of records (can be specified multiple times, conflicts with --records-file)
    --records-file string   JSON file containing the records (conflicts with --record)
    --ttl int               Time To Live (TTL) of the Zone RRSet
```

### `hcloud zone rrset remove-records`

Remove records from a Zone RRSet.

If the Zone RRSet doesn't contain any records, it will automatically be deleted.

The optional records file has to be in JSON format. You can find the schema at https://docs.hetzner.cloud/reference/cloud#zone-rrset-actions-set-records-of-an-rrset

**Example file content:**

```
[
{
  "value": "198.51.100.1",
  "comment": "My web server at Hetzner Cloud."
},
{
  "value": "198.51.100.2",
  "comment": "My other server at Hetzner Cloud."
}
]
```

**Usage:**

```
hcloud zone rrset remove-records (--record <value>... | --records-file <file>) <zone> <name> <type>
```

**Flags:**

```
    --record stringArray    List of records (can be specified multiple times, conflicts with --records-file)
    --records-file string   JSON file containing the records (conflicts with --record)
```

### `hcloud zone rrset set-records`

Set the records of a Zone RRSet.

- If the Zone RRSet doesn't exist, it will be created.
- If the Zone RRSet already exists, its records will be replaced.
- If the provided records are empty, the Zone RRSet will be deleted.

The optional records file has to be in JSON format. You can find the schema at https://docs.hetzner.cloud/reference/cloud#zone-rrset-actions-set-records-of-an-rrset

**Example file content:**

```
[
{
  "value": "198.51.100.1",
  "comment": "My web server at Hetzner Cloud."
},
{
  "value": "198.51.100.2",
  "comment": "My other server at Hetzner Cloud."
}
]
```

**Usage:**

```
hcloud zone rrset set-records (--record <value>... | --records-file <file>) <zone> <name> <type>
```

**Flags:**

```
    --record stringArray    List of records (can be specified multiple times, conflicts with --records-file)
    --records-file string   JSON file containing the records (conflicts with --record)
```

### `hcloud zone set-records`

Set the records of a Zone RRSet.

- If the Zone RRSet doesn't exist, it will be created.
- If the Zone RRSet already exists, its records will be replaced.
- If the provided records are empty, the Zone RRSet will be deleted.

The optional records file has to be in JSON format. You can find the schema at https://docs.hetzner.cloud/reference/cloud#zone-rrset-actions-set-records-of-an-rrset

**Example file content:**

```
[
{
  "value": "198.51.100.1",
  "comment": "My web server at Hetzner Cloud."
},
{
  "value": "198.51.100.2",
  "comment": "My other server at Hetzner Cloud."
}
]
```

**Usage:**

```
hcloud zone set-records (--record <value>... | --records-file <file>) <zone> <name> <type>
```

**Flags:**

```
    --record stringArray    List of records (can be specified multiple times, conflicts with --records-file)
    --records-file string   JSON file containing the records (conflicts with --record)
```
