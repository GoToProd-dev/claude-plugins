# `hcloud context` — Manage contexts

Generated from `--help` output of hcloud 1.70.1. Global flags (--context, --config, --endpoint, --debug, --quiet, ...) apply to every command and are omitted here.

### `hcloud context active`

Show active context

**Usage:**

```
hcloud context active
```

### `hcloud context create`

Create a new context

**Usage:**

```
hcloud context create [--token-from-env] <name>
```

**Flags:**

```
    --token-from-env   If true, the HCLOUD_TOKEN from the environment will be used without asking
```

### `hcloud context delete`

Delete a context

**Usage:**

```
hcloud context delete <context>
```

### `hcloud context list`

Displays a list of contexts.

Output can be controlled with the -o flag. Use -o noheader to suppress the
table header. Displayed columns and their order can be set with
-o columns=active,name (see available columns below).

**Columns:** active, name

**Usage:**

```
hcloud context list [options]
```

**Flags:**

```
    --allow-sensitive      Allow showing sensitive values in JSON/YAML output (true, false)
-o, --output stringArray   output options: noheader|columns=...|json|yaml
```

### `hcloud context rename`

Rename a context

**Usage:**

```
hcloud context rename <context> <name>
```

### `hcloud context unset`

Unset used context

**Usage:**

```
hcloud context unset
```

### `hcloud context use`

Use a context

**Usage:**

```
hcloud context use <context>
```
