# `hcloud all` — Commands that apply to all resources

Generated from `--help` output of hcloud 1.70.1. Global flags (--context, --config, --endpoint, --debug, --quiet, ...) apply to every command and are omitted here.

### `hcloud all list`

List all resources in the project. This does not include static/public resources like Locations, public ISOs, etc.

**Listed resources are:**

```
 - Servers
 - Images
 - Placement Groups
 - Primary IPs
 - ISOs
 - Volumes
 - Load Balancer
 - Floating IPs
 - Networks
 - Firewalls
 - Certificates
 - SSH Keys
 - Storage Boxes
 - Zones
```

**Usage:**

```
hcloud all list [options]
```

**Flags:**

```
-o, --output stringArray   output options: json|yaml
    --paid                 Only list resources that cost money (true, false)
-l, --selector string      Selector to filter by labels
```
