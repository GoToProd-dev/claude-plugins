---
name: hcloud-cli
description: Guide for using the Hetzner Cloud CLI (`hcloud`) to manage Hetzner infrastructure from the command line — servers, firewalls, volumes, networks, load balancers, floating/primary IPs, snapshots/images, SSH keys, certificates, DNS zones and records, storage boxes, and raw API calls. Use this whenever the user mentions Hetzner, hcloud, a Hetzner server/VPS, Hetzner DNS, or Hetzner storage boxes, or wants to provision, inspect, resize, snapshot, firewall, or tear down cloud infrastructure that lives on Hetzner — even if they don't name the CLI.
compatibility: Requires the `hcloud` binary (written against v1.70.1) and a Hetzner Cloud API token.
---

# Hetzner Cloud CLI Usage Guide

Help users manage Hetzner Cloud from the command line with the `hcloud` CLI.

> **Core rule for agents: know which project you're touching before you change anything.** An `hcloud` context is bound to exactly one Hetzner Cloud project (one API token). Nothing in the working directory selects it — the CLI uses whatever context is active, or `HCLOUD_TOKEN` if set. Read-only commands are safe to just run; before a create, delete, rebuild, resize or rule change, run `hcloud context active` and make sure it's the project the user means.

## Agent Guidance

### Key Principles

- **Just run read commands.** `list`, `describe`, `server ip`, `metrics` and the `*-type`/`location`/`image` catalogs are free and harmless. Run them instead of asking the user what exists.
- **Look up catalog values, don't guess them.** Server types, locations, images and prices change over time (e.g. older `cx` generations get retired, and datacenters are being replaced by locations). Run `hcloud server-type list`, `hcloud location list` or `hcloud image list --type system` rather than relying on remembered names.
- **A server type existing doesn't mean you can order it.** Types sell out or get deprecated per location, and the default `server-type list` table doesn't show that. Before recommending a type for a create or resize, check that the server's location appears under `LOCATION AVAILABLE`:
  ```bash
  hcloud server-type list -o columns=name,cores,memory,disk,cpu_type,architecture,location_available,deprecated
  ```
  A plan built on an unavailable type fails at the `create`/`change-type` step, after the user has already accepted downtime. If the cheap type isn't available, say so and offer the cheapest one that is.
- **Quote prices from the API, in the account's currency.** `hcloud api /pricing` returns `.pricing.currency` (it may be USD or EUR) and `.pricing.vat_rate`. Per-type prices are in `hcloud server-type describe <type>` for each location. Don't assume euros.
- **Prefer dedicated commands over `hcloud api`.** `hcloud api` exists for endpoints without a command and handles auth for you. Reach for it only when no `hcloud <resource> <verb>` covers the task.
- **Reference resources by name or ID.** Every `<server>`, `<firewall>`, etc. argument accepts either. Names are unique per project, so they're the readable choice in scripts and in what you show the user.
- **Use labels to group things.** Most create commands take `--label key=value`, and every `list` takes `-l/--selector` (e.g. `-l env=staging,app!=legacy`). This is how to find, or clean up, "everything for X".
- **`--help` is authoritative.** The references in this skill come from `hcloud --help`. If the installed version differs (`hcloud version`), trust the live `--help`.

### Authentication and Contexts

There's no OAuth. Each Hetzner Cloud **project** issues its own API tokens (Cloud Console → project → Security → API Tokens; pick Read or Read & Write). A **context** is a named token saved in `~/.config/hcloud/cli.toml`.

```bash
hcloud context list          # ACTIVE / NAME; an empty table means not set up yet
hcloud context active        # name of the context in use
hcloud context use prod      # switch
hcloud --context staging server list   # one-off override
```

`hcloud context create <name>` **prompts for the token on the terminal**, and you can't answer that prompt. Don't ask the user to paste the token into chat, because it would then sit in the transcript. Instead, either:

- ask the user to run it themselves. In Claude Code they can type `! hcloud context create <name>` at the prompt and paste the token into the hidden input, or
- if the token is already in the environment: `hcloud context create --token-from-env <name>` (reads `HCLOUD_TOKEN`).

Precedence is flags → env vars → active context → global config. A stray `HCLOUD_TOKEN` in the environment silently overrides the active context, so check `env | grep HCLOUD_` when the project you see isn't the one you expected. Never echo, log or commit tokens.

### Output and Context Window Tips

- **`-o json`** (or `-o yaml`) on `list`, `describe` and most `create` commands gives full data. Pipe it into `jq`.
- **`-o columns=a,b,c`** picks table columns, and **`-o noheader`** drops the header. Each list command's reference entry shows its available columns. For example: `hcloud server list -o columns=name,status,ipv4,type,location`.
- **`-o format='{{...}}'`** on `describe` applies a Go template, which is good for pulling out one value: `hcloud server describe web-1 -o format='{{.PublicNet.IPv4.IP}}'`. `hcloud server ip web-1` is shorter for the common case.
- **`-s/--sort`** sorts lists (`-s created:desc`), and `--status` filters servers by state.
- `hcloud all list` (optionally `--paid`) lists everything in the project in one call. It's a good first look at an unfamiliar project or a cost audit.
- `--quiet` prints only errors. Use it in scripts where the progress output is noise.

### Safety Rules

- **Deletes never prompt.** `hcloud server delete web-1` is immediate and irreversible, and the same goes for volumes, images, primary IPs, firewalls, zones and storage boxes. Confirm with the user first, naming the resource and the context/project.
- **Destructive-but-not-delete commands:** `server rebuild` wipes the disk, `server reset` is a hard reset, `server poweroff` is a hard power cut (use `shutdown` for a graceful ACPI stop), `zone rrset set-records` *replaces* a record set, `firewall replace-rules` replaces all rules, and `storage-box rollback-snapshot` overwrites live data. Confirm these too.
- **Things cost money.** Servers, volumes, primary/floating IPs, load balancers, snapshots and storage boxes are billed hourly from creation. **A powered-off server is still billed**; only deleting it stops the charge. Say so when you create something, and suggest labels so it's easy to find and remove later.
- **Deleting a server can release its IP.** Primary IPs with auto-delete go away with the server, and the address can't be reclaimed. If the user cares about keeping an IP, check `hcloud primary-ip list` first.
- **Use protection for production.** `hcloud server enable-protection <server> delete rebuild` (similar commands exist for volumes, IPs, images, networks, zones and storage boxes) makes accidental deletion fail until protection is disabled.
- **SSH keys over root passwords.** Creating a server without `--ssh-key` makes the API generate a root password, which the CLI prints. Pass `--ssh-key`, or set a default once with `hcloud config set default-ssh-keys <key-name>`.

### Errors

Any non-zero exit means failure, and the reason is on stderr (prefixed `hcloud:`). The usual causes:

| Symptom | Likely cause / action |
|---|---|
| `no active context or token` / `unauthorized` | No context or a revoked token. Have the user create a context (see above). |
| `forbidden` on a mutation | The token is Read-only. The user needs a Read & Write token. |
| `not found` | Wrong name/ID, **or the wrong project/context**. Check `hcloud context active` before concluding it doesn't exist. |
| `uniqueness_error` | That name is already taken in the project. |
| `resource_unavailable` / `placement_error` | That server type is sold out in that location. Try another `--location`. |
| `server ... is running` on `change-type` | Run `hcloud server shutdown` first, then retry. |
| `protected` | Delete/rebuild protection is on. Disable it only if the user really means it. |

`--debug` (or `--debug-file path`) shows the raw HTTP exchange when an error is unclear.

## Workflow Patterns

### First Look at a Project

```bash
hcloud context active
hcloud all list                                    # every resource, grouped by type
hcloud server list -o columns=name,status,ipv4,type,location,labels
```

### Create a Server

```bash
# 1. Pick real values from the catalogs
hcloud location list
hcloud server-type list
hcloud image list --type system -o columns=name,description,architecture

# 2. Make sure an SSH key is uploaded (create one from the user's public key if needed)
hcloud ssh-key list
hcloud ssh-key create --name laptop --public-key-from-file ~/.ssh/id_ed25519.pub

# 3. Create. It waits until the server is running and prints its IPs.
hcloud server create --name web-1 --type <type> --image ubuntu-24.04 --location <loc> \
  --ssh-key laptop --firewall web --label env=staging --label app=shop \
  --user-data-from-file cloud-init.yml

# 4. Connect
hcloud server ssh web-1                  # wraps ssh as root to the public IPv4
hcloud server ssh web-1 -- uptime        # run one command
```

`--image` accepts a system image name, a snapshot ID, or an app image. `--without-ipv4` saves the IPv4 charge on IPv6-only setups.

### Firewalls

```bash
hcloud firewall create --name web --label app=shop
hcloud firewall add-rule web --direction in --protocol tcp --port 22  --source-ips 203.0.113.4/32 --description ssh
hcloud firewall add-rule web --direction in --protocol tcp --port 443 --source-ips 0.0.0.0/0 --source-ips ::/0
hcloud firewall apply-to-resource web --type server --server web-1
hcloud firewall apply-to-resource web --type label_selector --label-selector app=shop   # every matching server, now and later
hcloud firewall describe web
```

Rules are allow-lists: once a firewall is applied, inbound traffic that matches no rule is dropped. Before applying a firewall to a running server, make sure SSH stays allowed, or the user loses access.

### Resize, Rescue, Snapshot

```bash
# Resize: pick a target that's available in the server's location and has the same
# architecture. change-type can't move between x86 and Arm (cax*); that needs a new server.
hcloud server describe web-1 -o format='{{.ServerType.Name}} {{.ServerType.Architecture}} {{.Location.Name}}'
hcloud server-type list -o columns=name,cores,memory,disk,cpu_type,architecture,location_available,deprecated
# The server must be off. --keep-disk keeps the disk size so you can downgrade later.
hcloud server shutdown web-1
hcloud server change-type web-1 <new-type> --keep-disk
hcloud server poweron web-1

# Snapshot (billed per GB) — take one before risky changes
hcloud server create-image web-1 --type snapshot --description "before upgrade" --label app=shop
hcloud image list --type snapshot

# Rescue system for a broken boot
hcloud server enable-rescue web-1 --ssh-key laptop && hcloud server reboot web-1
```

### Volumes and Networks

```bash
hcloud volume create --name data --size 50 --server web-1 --automount --format ext4
hcloud volume resize data --size 100        # grow only; then grow the filesystem on the server

hcloud network create --name internal --ip-range 10.0.0.0/16
hcloud network add-subnet internal --type cloud --network-zone eu-central --ip-range 10.0.1.0/24
hcloud server attach-to-network web-1 --network internal
```

### DNS Zones and Records

Records are managed as **RRSets**, one per (name, type) pair, which can hold several values. Use `@` for the zone apex.

```bash
hcloud zone list
hcloud zone rrset list example.com
hcloud zone add-records example.com www A --record 198.51.100.1        # appends to the set
hcloud zone set-records example.com @ A --record 198.51.100.1          # replaces the whole set
hcloud zone rrset remove-records example.com www A --record 198.51.100.1
hcloud zone export-zonefile example.com                                # BIND format, good for backups
```

Prefer `add-records`/`remove-records` for targeted edits, because `set-records` overwrites whatever is there.

### Load Balancer

```bash
hcloud load-balancer-type list
hcloud load-balancer create --name lb --type <type> --location <loc>
hcloud load-balancer add-service lb --protocol http --listen-port 80 --destination-port 8080
hcloud load-balancer add-target lb --label-selector app=shop        # or --server web-1
hcloud load-balancer describe lb      # check target health here
```

### Clean Up by Label

```bash
hcloud server list -l env=preview -o noheader -o columns=name      # show the user first
# after they confirm:
hcloud server list -l env=preview -o noheader -o columns=name | xargs -r hcloud server delete
hcloud all list --paid -l env=preview                              # verify nothing billable is left
```

### Raw API Access

```bash
hcloud api /servers                                  # path is relative to the API endpoint
hcloud api /servers -v label_selector=env=prod -v per_page=50
hcloud api /servers/123/actions/poweron -X POST
echo '{"name":"renamed"}' | hcloud api /servers/123 -X PUT -d -
```

Storage boxes (and other Hetzner-wide products) live on a separate API, `https://api.hetzner.com/v1` (`--hetzner-endpoint`). The `storage-box` commands handle this for you.

## Command Index

Each group has a reference file with every subcommand's usage, flags, list columns and examples: `references/<group>.md`. Read the one you need instead of guessing flags, since many commands have required flags that differ between resources.

| Group | Purpose | Subcommands |
|---|---|---|
| `all` | Commands that apply to all resources | list |
| `api` | Make raw API call | (single command) |
| `certificate` | Manage Certificates | add-label, create, delete, describe, list, remove-label, retry, update |
| `config` | Manage configuration | add, get, list, remove, set, unset |
| `context` | Manage contexts | active, create, delete, list, rename, unset, use |
| `datacenter` | View Datacenters (deprecated) | describe, list |
| `firewall` | Manage Firewalls | add-label, create, delete, describe, list, remove-label, update, add-rule, delete-rule, replace-rules, apply-to-resource, remove-from-resource |
| `floating-ip` | Manage Floating IPs | add-label, create, delete, describe, list, remove-label, update, disable-protection, enable-protection, assign, unassign, set-rdns |
| `image` | Manage Images | add-label, delete, describe, list, remove-label, update, disable-protection, enable-protection |
| `iso` | View ISOs | describe, list |
| `load-balancer` | Manage Load Balancers | add-label, change-algorithm, change-type, create, delete, describe, list, remove-label, update, disable-protection, enable-protection, add-target, remove-target, add-service, delete-service, update-service, attach-to-network, detach-from-network, disable-public-interface, enable-public-interface, metrics, set-rdns |
| `load-balancer-type` | View Load Balancer Types | describe, list |
| `location` | View Locations | describe, list |
| `network` | Manage Networks | add-label, change-ip-range, create, delete, describe, list, remove-label, update, disable-protection, enable-protection, add-route, expose-routes-to-vswitch, remove-route, add-subnet, remove-subnet, list-members |
| `placement-group` | Manage Placement Groups | add-label, create, delete, describe, list, remove-label, update |
| `primary-ip` | Manage Primary IPs | add-label, create, delete, describe, list, remove-label, update, disable-protection, enable-protection, assign, unassign, set-rdns |
| `server` | Manage Servers | add-label, change-type, create, create-image, delete, describe, list, rebuild, remove-label, update, disable-protection, enable-protection, disable-rescue, enable-rescue, poweroff, poweron, reboot, reset, shutdown, attach-to-network, change-alias-ips, detach-from-network, attach-iso, detach-iso, add-to-placement-group, remove-from-placement-group, disable-backup, enable-backup, ip, metrics, request-console, reset-password, set-rdns, ssh |
| `server-type` | View Server Types | describe, list |
| `ssh-key` | Manage SSH Keys | add-label, create, delete, describe, list, remove-label, update |
| `storage-box` | Manage Storage Boxes | add-label, change-type, create, delete, describe, folders, list, remove-label, update, disable-protection, enable-protection, disable-snapshot-plan, enable-snapshot-plan, rollback-snapshot, snapshot add-label, snapshot create, snapshot delete, snapshot describe, snapshot list, snapshot remove-label, snapshot update, reset-password, subaccount change-home-directory, subaccount create, subaccount delete, subaccount describe, subaccount list, subaccount reset-password, subaccount update, subaccount update-access-settings, update-access-settings |
| `storage-box-type` | View Storage Box Types | describe, list |
| `volume` | Manage Volumes | add-label, create, delete, describe, list, remove-label, resize, update, disable-protection, enable-protection, attach, detach |
| `zone` | Manage DNS Zones and Zone RRSets (records) | add-label, change-primary-nameservers, change-ttl, create, delete, describe, list, remove-label, disable-protection, enable-protection, export-zonefile, import-zonefile, add-records, remove-records, rrset add-label, rrset change-ttl, rrset create, rrset delete, rrset describe, rrset list, rrset remove-label, rrset disable-protection, rrset enable-protection, rrset add-records, rrset remove-records, rrset set-records, set-records |

## Global Options

These apply to every command: `--context <name>`, `--config <path>`, `--quiet`, `--debug`, `--debug-file <path>`, `--http-timeout <dur>`, `--poll-interval <dur>`, `--endpoint` / `--hetzner-endpoint` (API base URLs), `--no-experimental-warnings`.

Preferences can be stored with `hcloud config set [--global] <key> <value>`, for example `default-ssh-keys`, `quiet`, or `sort.server name`. Run `hcloud help config` for the full list, or see `references/config.md`.

## Maintaining This Skill

The `references/` files are generated from the installed CLI. After upgrading `hcloud`, regenerate them and update the version in the frontmatter:

```bash
python3 scripts/gen_references.py
```
