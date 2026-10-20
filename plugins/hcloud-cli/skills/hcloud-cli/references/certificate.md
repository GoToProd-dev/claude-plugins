# `hcloud certificate` — Manage Certificates

Generated from `--help` output of hcloud 1.70.1. Global flags (--context, --config, --endpoint, --debug, --quiet, ...) apply to every command and are omitted here.

### `hcloud certificate add-label`

Add a label to a Certificate

**Usage:**

```
hcloud certificate add-label [--overwrite] <certificate> <label>...
```

**Flags:**

```
-o, --overwrite   Overwrite label if it exists already (true, false)
```

### `hcloud certificate create`

Create or upload a Certificate

**Usage:**

```
hcloud certificate create [options] --name <name> (--type managed --domain <domain> | --type uploaded --cert-file <file> --key-file <file>)
```

**Flags:**

```
    --cert-file string       File containing the PEM encoded certificate (required if type is uploaded)
    --domain strings         One or more domains the Certificate is valid for.
    --key-file string        File containing the PEM encoded private key for the certificate (required if type is uploaded)
    --label stringToString   User-defined labels ('key=value') (can be specified multiple times) (default [])
    --name string            Certificate name (required)
-o, --output stringArray     output options: json|yaml
-t, --type string            Type of Certificate to create. Valid choices: uploaded, managed (default "uploaded")
```

### `hcloud certificate delete`

Delete a Certificate

**Usage:**

```
hcloud certificate delete <certificate>...
```

### `hcloud certificate describe`

Describe a Certificate

**Usage:**

```
hcloud certificate describe [options] <certificate>
```

**Flags:**

```
-o, --output stringArray   output options: json|yaml|format
```

### `hcloud certificate list`

Displays a list of Certificates.

Output can be controlled with the -o flag. Use -o noheader to suppress the
table header. Displayed columns and their order can be set with
-o columns=age,created (see available columns below).

**Columns:** age, created, domain_names, fingerprint, id, issuance_status, labels, name, not_valid_after, not_valid_before, renewal_status, type

**Usage:**

```
hcloud certificate list [options]
```

**Flags:**

```
-o, --output stringArray   output options: noheader|columns=...|json|yaml
-l, --selector string      Selector to filter by labels
-s, --sort strings         Determine the sorting of the result
```

### `hcloud certificate remove-label`

Remove a label from a Certificate

**Usage:**

```
hcloud certificate remove-label <certificate> (--all | <label>...)
```

**Flags:**

```
-a, --all    Remove all labels
```

### `hcloud certificate retry`

Retry a managed Certificate's issuance

**Usage:**

```
hcloud certificate retry <certificate>
```

### `hcloud certificate update`

Update a Certificate

**Usage:**

```
hcloud certificate update [options] <certificate>
```

**Flags:**

```
    --name string   Certificate Name
```
