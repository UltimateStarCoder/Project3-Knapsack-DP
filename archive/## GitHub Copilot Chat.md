## GitHub Copilot Chat

- Extension Version: 0.22.2 (prod)
- VS Code: vscode/1.95.2
- OS: Mac

## Network

User Settings:
```json
  "github.copilot.advanced": {
    "debug.useElectronFetcher": true,
    "debug.useNodeFetcher": false
  }
```

Connecting to https://api.github.com:
- DNS ipv4 Lookup: 140.82.112.5 (5 ms)
- DNS ipv6 Lookup: ::ffff:140.82.112.5 (22 ms)
- Electron Fetcher (configured): timed out after 10 seconds
- Node Fetcher: HTTP 200 (147 ms)
- Helix Fetcher: HTTP 200 (282 ms)

Connecting to https://api.individual.githubcopilot.com/_ping:
- DNS ipv4 Lookup: 140.82.112.22 (48 ms)
- DNS ipv6 Lookup: ::ffff:140.82.112.22 (1 ms)
- Electron Fetcher (configured): HTTP 200 (146 ms)
- Node Fetcher: HTTP 200 (158 ms)
- Helix Fetcher: HTTP 200 (168 ms)

## Documentation

In corporate networks: [Troubleshooting firewall settings for GitHub Copilot](https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-firewall-settings-for-github-copilot).