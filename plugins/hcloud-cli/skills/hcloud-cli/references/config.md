# `hcloud config` — Manage configuration

Generated from `--help` output of hcloud 1.70.1. Global flags (--context, --config, --endpoint, --debug, --quiet, ...) apply to every command and are omitted here.

## `hcloud config`

```
This command allows you to manage options for the Hetzner Cloud CLI. Options can be set inside the
configuration file, through environment variables or with flags. 

The hierarchy for configuration sources is as follows (from highest to lowest priority):
1. Flags
2. Environment variables
3. Configuration file (context)
4. Configuration file (global)
5. Default values
```

### `hcloud config add`

Add values to a list. For a list of all available configuration options, run 'hcloud help config'.

**Usage:**

```
hcloud config add <key> <value>...
```

**Flags:**

```
    --global   Set the value globally (for all contexts) (true, false)
```

### `hcloud config get`

Get a configuration value. For a list of all available configuration options, run 'hcloud help config'.

**Usage:**

```
hcloud config get <key>
```

**Flags:**

```
    --allow-sensitive   Allow showing sensitive values (true, false)
    --global            Get the value globally (true, false)
```

### `hcloud config list`

List configuration values

**Usage:**

```
hcloud config list
```

**Flags:**

```
-a, --all                  Also show default values (true, false)
    --allow-sensitive      Allow showing sensitive values (true, false)
-g, --global               Only show global values (true, false)
-o, --output stringArray   output options: noheader|columns=...|json|yaml
```

### `hcloud config remove`

Remove values from a list. For a list of all available configuration options, run 'hcloud help config'.

**Usage:**

```
hcloud config remove <key> <value>...
```

**Flags:**

```
    --global   Remove the value(s) globally (for all contexts) (true, false)
```

### `hcloud config set`

Set a configuration value. For a list of all available configuration options, run 'hcloud help config'.

**Usage:**

```
hcloud config set <key> <value>...
```

**Flags:**

```
    --global   Set the value globally (for all contexts) (true, false)
```

### `hcloud config unset`

Unset a configuration value. For a list of all available configuration options, run 'hcloud help config'.

**Usage:**

```
hcloud config unset <key>
```

**Flags:**

```
    --global   Unset the value globally (for all contexts) (true, false)
```
