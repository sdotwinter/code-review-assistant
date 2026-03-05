# Code Review Assistant

[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ea4aaa?logo=githubsponsors)](https://github.com/sponsors/sdotwinter)

Code Review Assistant is a lightweight Python CLI that performs pre-review checks on Python/JS/TS codebases.
It flags common issues before a human reviewer looks at a PR.

## Features
- Scan source files for TODO/FIXME markers
- Detect debug statements (`print`, `console.log`)
- Catch bare `except:` blocks
- Report long lines (>120 chars)
- Output findings as table, summary, or JSON

## Usage
```bash
cd /home/sean/.openclaw/workspace/app-factory-hub/projects/code-review-assistant
python3 main.py scan /path/to/repo
python3 main.py summary /path/to/repo
python3 main.py suggest /path/to/repo
```

## Project Files
- `main.py` - entry point
- `cli.py` - command interface
- `review_engine.py` - scanning and rules
- `reporter.py` - formatting output
- `requirements.txt` - dependencies

## Sponsorware
This project is distributed as **Sponsorware**.

- Personal evaluation/non-commercial use is allowed.
- Commercial usage and advanced rule packs require sponsorship.
- Suggested support tiers: **$7 / $14 / $50** via GitHub Sponsors.
