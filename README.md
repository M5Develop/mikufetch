# mikufetch

A Hatsune Miku-themed system fetch tool for the terminal, written in Python.
If you are looking for a Neofetch alternative that brings your favorite Vocaloid to your terminal, mikufetch is the perfect choice for your Linux rice

```
   ||       ||     runner@hostname
   ||       ||     ─────────────────
  (  \_____/  )    OS        Ubuntu 24.04.2 LTS
  |  (o   o)  |    Kernel    6.14.11
  |     u     |    CPU       AMD EPYC 9B14
  |  ~-----~  |    RAM       4.20GB / 15.6GB
  |   [===]   |    Shell     bash
   \   | |   /     Terminal  xterm-256color
    \  | |  /      Uptime    2d 4h 30m
   /\  | |  /\     Packages  512 (apt)
  /  \_|_|_/  \
 /    MIKU     \
```

![Python](https://img.shields.io/badge/python-3.11+-blue.svg) 
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Stars](https://img.shields.io/github/stars/M5Develop/mikufetch?style=social)
## Features

- **Hatsune Miku ASCII art** rendered in CYAN in your terminal
- **OS & Kernel** — reads from `/etc/os-release` and `platform.release()`
- **CPU** — fast direct read from `/proc/cpuinfo`, falls back to `platform.processor()`
- **RAM** — used / total via `psutil`
- **Shell** — bulletproof detection: checks `$SHELL`, then `/proc/self/exe`, then parent PID
- **Terminal** — reads `$TERM_PROGRAM`, `$COLORTERM`, and `$TERM`
- **Uptime** — calculated from `psutil.boot_time()`, displayed as `Xd Xh Xm`
- **Package count** — supports `apt`, `pacman`, `dnf`, and `apk`

## Installation

### From source

```bash
pip install mikufetch
```

Then run from anywhere:

```bash
mikufetch
```

### Development mode

```bash
pip install -e mikufetch
```

## Requirements

- Python 3.11+
- `psutil >= 7.2.2`

## Project structure

```
mikufetch/
├── mikufetch/
│   ├── __init__.py
│   ├── main.py        # System info logic and rendering
│   └── ascii_art.py   # Miku ASCII art
├── pyproject.toml
└── README.md
```

## License

MIT
