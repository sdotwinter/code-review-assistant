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

## Sponsorship

This project follows the App Factory sponsorship model:

### $5/month - Supporter
- Sponsor badge on your GitHub profile
- Monthly sponsor update

### $25/month - Builder Circle
- Everything in Supporter
- Name listed in project Sponsors section (monthly refresh)
- Access to private sponsor Discord channel

### $100/month - Priority Maintainer
- Everything in Builder Circle
- Priority bug triage for your reports (max 2 issues/month)
- Response target: within 5 business days

### $1,000/month - Operator Advisory
- Everything in Priority Maintainer
- Dedicated async advisory support
- Service boundary: guidance and review only (no custom development included)

### $5,000 one-time - Custom Project Engagement
- Custom contract engagement
- Discovery required before kickoff
- Scope, timeline, and deliverables agreed in writing

Sponsor: https://github.com/sponsors/sdotwinter

