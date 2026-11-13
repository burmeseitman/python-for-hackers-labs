# Python for Hackers — Course Labs

Safe, hands-on Python labs for the Burmese Stack **Python for Hackers** course.

This repository is a software engineer's learning-and-building journey. It is not a collection of tools for testing public systems. Run labs only on data and systems you own or are explicitly authorized to use.

## Course structure

```text
python-for-hackers-labs/
├── episodes/
│   ├── ep-01-intro-local-log-analyzer/  # available now
│   └── ep-01-python-setup-data-basics/  # prepared for the next episode
└── docs/                                # shared course guidance
```

## Start here

```bash
cd episodes/ep-01-intro-local-log-analyzer
python3 log_analyzer.py
```

Expected output:

```text
Failed login events: 3
  alice: 2
  bob: 1
```

## Episode convention

Each episode folder should include:

- `README.md` — purpose, setup, run steps, boundaries, and expected result.
- Source files — small, readable Python programs.
- Fixtures — fictional, local test data only.
- `tests/` — automated checks when the episode introduces behavior worth preserving.

Do not commit credentials, personal data, production logs, or data from systems you do not own.
