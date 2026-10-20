# `hcloud datacenter` — View Datacenters (deprecated)

Generated from `--help` output of hcloud 1.70.1. Global flags (--context, --config, --endpoint, --debug, --quiet, ...) apply to every command and are omitted here.

## `hcloud datacenter`

```
The 'hcloud datacenter ...' commands are deprecated and will be removed after 1 Oct. 2026.
After this date, requests to the datacenters API endpoints will return HTTP 410 Gone.

See https://docs.hetzner.cloud/changelog#2026-06-02-datacenters-deprecated for more details.
```

### `hcloud datacenter describe`

The 'hcloud datacenter ...' commands are deprecated and will be removed after 1 Oct. 2026.
After this date, requests to the datacenters API endpoints will return HTTP 410 Gone.

See https://docs.hetzner.cloud/changelog#2026-06-02-datacenters-deprecated for more details.

**Usage:**

```
hcloud datacenter describe [options] <datacenter>
```

**Flags:**

```
-o, --output stringArray   output options: json|yaml|format
```

### `hcloud datacenter list`

The 'hcloud datacenter ...' commands are deprecated and will be removed after 1 Oct. 2026.
After this date, requests to the datacenters API endpoints will return HTTP 410 Gone.

See https://docs.hetzner.cloud/changelog#2026-06-02-datacenters-deprecated for more details.

Displays a list of Datacenters.

Output can be controlled with the -o flag. Use -o noheader to suppress the
table header. Displayed columns and their order can be set with
-o columns=description,id (see available columns below).

**Columns:** description, id, location, name

**Usage:**

```
hcloud datacenter list [options]
```

**Flags:**

```
-o, --output stringArray   output options: noheader|columns=...|json|yaml
-l, --selector string      Selector to filter by labels
-s, --sort strings         Determine the sorting of the result
```
