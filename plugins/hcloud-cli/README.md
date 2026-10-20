# hcloud-cli

A Claude Code skill for the [Hetzner Cloud CLI](https://github.com/hetznercloud/cli) (`hcloud`).

> This is an unofficial community plugin. It is not made, endorsed, or supported by Hetzner Online GmbH.

With this plugin installed, Claude can manage Hetzner Cloud infrastructure from your terminal: servers, firewalls, volumes, networks, load balancers, floating and primary IPs, snapshots and images, SSH keys, certificates, DNS zones and records, and storage boxes. It can also make raw API calls with `hcloud api`. The skill loads by itself when you mention Hetzner or hcloud. You can also run it directly with `/hcloud-cli:hcloud-cli`.

It ships a reference for every `hcloud` command, generated from the CLI's own `--help` output. That lets Claude use real flags rather than guess them.

## What it does

- Picks the right context (project) and confirms it before changing anything.
- Asks before deletes and other destructive commands (rebuild, hard reset, replacing firewall rules or DNS record sets). `hcloud` itself never prompts for these.
- Checks that a server type can actually be ordered in your location before recommending it, and keeps resizes on the same CPU architecture.
- Quotes prices from the API in your account's currency, not from memory.
- Uses `-o json` / `-o columns=` output for scripting, and `--hetzner-endpoint` for storage boxes.

## Requirements

- `hcloud` installed and on your `PATH`. The skill was written against v1.70.1.
- A Hetzner Cloud API token, stored with `hcloud context create <name>`. The skill never asks you to paste the token into the chat. Run the `context create` command yourself in a terminal.

## Install

```shell
claude plugin marketplace add GoToProd-dev/claude-plugins
claude plugin install hcloud-cli@gotoprod-tools
```

Or from inside a Claude Code session:

```
/plugin marketplace add GoToProd-dev/claude-plugins
/plugin install hcloud-cli@gotoprod-tools
```

## Updating the command reference

After you upgrade `hcloud`, regenerate the reference files so they match your installed version:

```shell
python3 skills/hcloud-cli/scripts/gen_references.py
```

## License

MIT. See [LICENSE](LICENSE).
