# `hcloud load-balancer` — Manage Load Balancers

Generated from `--help` output of hcloud 1.70.1. Global flags (--context, --config, --endpoint, --debug, --quiet, ...) apply to every command and are omitted here.

### `hcloud load-balancer add-label`

Add a label to a Load Balancer

**Usage:**

```
hcloud load-balancer add-label [--overwrite] <load-balancer> <label>...
```

**Flags:**

```
-o, --overwrite   Overwrite label if it exists already (true, false)
```

### `hcloud load-balancer change-algorithm`

Changes the algorithm of a Load Balancer

**Usage:**

```
hcloud load-balancer change-algorithm --algorithm-type <round_robin|least_connections> <load-balancer>
```

**Flags:**

```
    --algorithm-type string   New Load Balancer algorithm (round_robin, least_connections) (required)
```

### `hcloud load-balancer change-type`

Change type of a Load Balancer

**Usage:**

```
hcloud load-balancer change-type <load-balancer> <load-balancer-type>
```

### `hcloud load-balancer create`

Create a Load Balancer

**Usage:**

```
hcloud load-balancer create [options] --name <name> --type <type>
```

**Flags:**

```
    --algorithm-type string       Algorithm Type name (round_robin or least_connections)
    --enable-protection strings   Enable protection (delete) (default: none)
    --label stringToString        User-defined labels ('key=value') (can be specified multiple times) (default [])
    --location string             Location (ID or name)
    --name string                 Load Balancer name (required)
    --network string              Name or ID of the Network the Load Balancer should be attached to on creation
    --network-zone string         Network Zone
-o, --output stringArray          output options: json|yaml
    --primary-ipv4 string         Primary IPv4 (ID or name) to assign to the Load Balancer
    --primary-ipv6 string         Primary IPv6 (ID or name) to assign to the Load Balancer
    --type string                 Load Balancer Type (ID or name) (required)
```

### `hcloud load-balancer delete`

Delete a Load Balancer

**Usage:**

```
hcloud load-balancer delete <load-balancer>...
```

### `hcloud load-balancer describe`

Describe a Load Balancer

**Usage:**

```
hcloud load-balancer describe [options] <load-balancer>
```

**Flags:**

```
    --expand-targets       Expand all label_selector targets (true, false)
-o, --output stringArray   output options: json|yaml|format
```

### `hcloud load-balancer list`

Displays a list of Load Balancer.

Output can be controlled with the -o flag. Use -o noheader to suppress the
table header. Displayed columns and their order can be set with
-o columns=age,created (see available columns below).

**Columns:** age, created, health, id, ipv4, ipv6, labels, location, name, network_zone, protection, type

**Usage:**

```
hcloud load-balancer list [options]
```

**Flags:**

```
-o, --output stringArray   output options: noheader|columns=...|json|yaml
-l, --selector string      Selector to filter by labels
-s, --sort strings         Determine the sorting of the result
```

### `hcloud load-balancer remove-label`

Remove a label from a Load Balancer

**Usage:**

```
hcloud load-balancer remove-label <load-balancer> (--all | <label>...)
```

**Flags:**

```
-a, --all    Remove all labels
```

### `hcloud load-balancer update`

Update a Load Balancer

**Usage:**

```
hcloud load-balancer update [options] <load-balancer>
```

**Flags:**

```
    --name string   Load Balancer name
```

### `hcloud load-balancer disable-protection`

Disable resource protection for a Load Balancer

**Usage:**

```
hcloud load-balancer disable-protection <load-balancer> delete
```

### `hcloud load-balancer enable-protection`

Enable resource protection for a Load Balancer

**Usage:**

```
hcloud load-balancer enable-protection <load-balancer> delete
```

### `hcloud load-balancer add-target`

Add a target to a Load Balancer

**Usage:**

```
hcloud load-balancer add-target [options] (--server <server> | --label-selector <label-selector> | --ip <ip>) <load-balancer>
```

**Flags:**

```
    --ip string               Use the passed IP address as target
    --label-selector string   Label Selector
    --server string           Name or ID of the server
    --use-private-ip          Determine if the Load Balancer should connect to the target via the network (true, false)
```

### `hcloud load-balancer remove-target`

Remove a target from a Load Balancer

**Usage:**

```
hcloud load-balancer remove-target [options] <load-balancer>
```

**Flags:**

```
    --ip string               IP address of an IP target
    --label-selector string   Label Selector
    --server string           Name or ID of the server
```

### `hcloud load-balancer add-service`

Add a service to a Load Balancer

**Usage:**

```
hcloud load-balancer add-service [options] (--protocol http | --protocol tcp --listen-port <1-65535> --destination-port <1-65535> | --protocol https --http-certificates <ids>) <load-balancer>
```

**Flags:**

```
    --destination-port int                     Destination port of the service on the targets
    --health-check-http-domain string          The domain we request when performing a http health check
    --health-check-http-path string            The path we request when performing a http health check
    --health-check-http-response string        The response we expect to determine a target as healthy
    --health-check-http-status-codes strings   List of status codes we expect to determine a target as healthy
    --health-check-http-tls                    Determine if the health check should verify if the target answers with a valid TLS certificate (true, false)
    --health-check-interval duration           The interval the health check is performed (default 15s)
    --health-check-port int                    The port the health check is performed over
    --health-check-protocol string             The protocol the health check is performed over
    --health-check-retries int                 Number of retries after a health check is marked as failed (default 3)
    --health-check-timeout duration            The timeout after a health check is marked as failed (default 10s)
    --http-certificates strings                IDs or names of Certificates which should be attached to this Load Balancer
    --http-cookie-lifetime duration            Sticky Sessions: Lifetime of the cookie
    --http-cookie-name string                  Sticky Sessions: Cookie Name we set
    --http-redirect-http                       Redirect all traffic on port 80 to port 443 (true, false)
    --http-sticky-sessions                     Enable Sticky Sessions (true, false)
    --http-timeout-idle duration               Idle timeout for HTTP connections (30s-300s)
    --listen-port int                          Listen port of the service
    --protocol string                          Protocol of the service (required)
    --proxy-protocol                           Enable proxyprotocol (true, false)
```

### `hcloud load-balancer delete-service`

Deletes a service from a Load Balancer

**Usage:**

```
hcloud load-balancer delete-service --listen-port <1-65535> <load-balancer>
```

**Flags:**

```
    --listen-port int   The listen port of the service you want to delete (required)
```

### `hcloud load-balancer update-service`

Updates a service from a Load Balancer

**Usage:**

```
hcloud load-balancer update-service [options] --listen-port <1-65535> <load-balancer>
```

**Flags:**

```
    --destination-port int                     Destination port of the service on the targets
    --health-check-http-domain string          The domain we request when performing a http health check
    --health-check-http-path string            The path we request when performing a http health check
    --health-check-http-response string        The response we expect to determine a target as healthy
    --health-check-http-status-codes strings   List of status codes we expect to determine a target as healthy
    --health-check-http-tls                    Determine if the health check should verify if the target answers with a valid TLS certificate (true, false)
    --health-check-interval duration           The interval the health check is performed (default 15s)
    --health-check-port int                    The port the health check is performed over
    --health-check-protocol string             The protocol the health check is performed over
    --health-check-retries int                 Number of retries after a health check is marked as failed (default 3)
    --health-check-timeout duration            The timeout after a health check is marked as failed (default 10s)
    --http-certificates strings                IDs or names of Certificates which should be attached to this Load Balancer
    --http-cookie-lifetime duration            Sticky Sessions: Lifetime of the cookie
    --http-cookie-name string                  Sticky Sessions: Cookie Name which will be set
    --http-redirect-http                       Enable or disable redirect all traffic on port 80 to port 443 (true, false)
    --http-sticky-sessions                     Enable or disable (with --http-sticky-sessions=false) Sticky Sessions (true, false)
    --http-timeout-idle duration               Idle timeout for HTTP connections (30s-300s)
    --listen-port int                          The listen port of the service that you want to update (required)
    --protocol string                          The protocol to use for load balancing traffic
    --proxy-protocol                           Enable or disable (with --proxy-protocol=false) Proxy Protocol (true, false)
```

### `hcloud load-balancer attach-to-network`

Attach a Load Balancer to a Network

**Usage:**

```
hcloud load-balancer attach-to-network [--ip <ip>] --network <network> <load-balancer>
```

**Flags:**

```
    --ip ip            IP address to assign to the Load Balancer (auto-assigned if omitted)
    --ip-range ipNet   IP range in CIDR block notation of the subnet to attach to (auto-assigned if omitted)
-n, --network string   Network (ID or name) (required)
```

### `hcloud load-balancer detach-from-network`

Detach a Load Balancer from a Network

**Usage:**

```
hcloud load-balancer detach-from-network --network <network> <load-balancer>
```

**Flags:**

```
-n, --network string   Network (ID or name) (required)
```

### `hcloud load-balancer disable-public-interface`

Disable the public interface of a Load Balancer

**Usage:**

```
hcloud load-balancer disable-public-interface <load-balancer>
```

### `hcloud load-balancer enable-public-interface`

Enable the public interface of a Load Balancer

**Usage:**

```
hcloud load-balancer enable-public-interface <load-balancer>
```

### `hcloud load-balancer metrics`

[ALPHA] Metrics from a Load Balancer

**Usage:**

```
hcloud load-balancer metrics [options] (--type <open_connections|connections_per_second|requests_per_second|bandwidth>)... <load-balancer>
```

**Flags:**

```
    --end string           ISO 8601 timestamp
-o, --output stringArray   output options: json|yaml
    --start string         ISO 8601 timestamp
    --type strings         Types of metrics you want to show
```

### `hcloud load-balancer set-rdns`

Change reverse DNS of a Load Balancer

**Usage:**

```
hcloud load-balancer set-rdns [--ip <ip>] (--hostname <hostname> | --reset) <load-balancer>
```

**Flags:**

```
-r, --hostname string   Hostname to set as a reverse DNS PTR entry
-i, --ip ip             IP address for which the reverse DNS entry should be set
    --reset             Reset the reverse DNS entry to the default value (true, false)
```
