# mikufetch 🎵

A Hatsune Miku & Kasane Teto themed system fetch tool for the terminal, written in Python.

If you are looking for a Neofetch alternative that brings your favorite Vocaloid to your terminal, **mikufetch** is the perfect choice for your Linux rice 🌸

```
   ||       ||     runner@hostname
   ||       ||     ─────────────────
  (  \_____/  )    OS        Ubuntu 24.04.2 LTS
  |  (^   ^)  |    Kernel    6.14.11
  |     u     |    CPU       AMD EPYC 9B14
  |  ~-----~  |    RAM       4.20GB / 15.6GB
  |   [===]   |    Shell     bash
   \   | |   /     Terminal  xterm-256color
    \  | |  /      Uptime    2d 4h 30m
   /\  | |  /\     Packages  512 (apt)
  /  \_|_|_/  \
 /   MIKU  39  \
```

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Stars](https://img.shields.io/github/stars/M5Develop/mikufetch?style=social)
![PyPI](https://img.shields.io/pypi/v/m5-mikufetch)

---

## Features

- **Hatsune Miku** ASCII art rendered in **CYAN** 💙
- **Kasane Teto** ASCII art rendered in **RED** ❤️
- **Random mode** — let fate decide your character
- **OS & Kernel** — reads from `/etc/os-release` and `platform.release()`
- **CPU** — fast direct read from `/proc/cpuinfo`, falls back to `platform.processor()`
- **RAM** — used / total via `psutil`
- **Shell** — bulletproof detection: checks `$SHELL`, then `/proc/self/exe`, then parent PID
- **Terminal** — reads `$TERM_PROGRAM`, `$COLORTERM`, and `$TERM`
- **Uptime** — calculated from `psutil.boot_time()`, displayed as `Xd Xh Xm`
- **Package count** — supports `apt`, `pacman`, `dnf`, and `apk`

---

## Installation

```bash
pip install m5-mikufetch
```

Then run from anywhere:

```bash
mikufetch
```

---

## Usage

```bash
# Default — Hatsune Miku 💙
mikufetch

# Kasane Teto mode 🔴
mikufetch --teto
mikufetch -t

# Pick manually
mikufetch --art miku
mikufetch --art teto

# Random character
mikufetch --random
mikufetch -r
```

---

## Requirements

- Python 3.11+
- `psutil >= 5.9`
- Linux (macOS/Windows partial support)

---

## Project structure

```
mikufetch/
├── mikufetch/
│   ├── __init__.py
│   ├── main.py        # System info logic, CLI, and rendering
│   └── ascii_art.py   # Miku & Teto ASCII art
├── pyproject.toml
├── nfpm.yaml
└── README.md
```

---

## Development

```bash
git clone https://github.com/M5Develop/mikufetch
cd mikufetch
pip install -e .
mikufetch --teto
```

---

## License

MIT — made with 💙❤️ by [M5Dev](https://github.com/M5Develop)

Miku & Teto ASCII art are fan-made. Not affiliated with Crypton Future Media or TWINDRILL.
