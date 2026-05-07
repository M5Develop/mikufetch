import psutil
import platform
import os
import time
import getpass
import subprocess
import argparse
import random

from mikufetch.ascii_art import MIKU_ART, TETO_ART, ARTS, CYAN, RED, WHITE, RESET

BOLD = "\033[1m"
DIM  = "\033[2m"


def get_distro() -> str:
    if platform.system() == "Linux":
        try:
            with open("/etc/os-release") as f:
                for line in f:
                    if line.startswith("PRETTY_NAME"):
                        return line.split("=", 1)[1].strip().strip('"')
        except Exception:
            pass
    return platform.system()


def get_cpu_info() -> str:
    if platform.system() == "Linux":
        try:
            with open("/proc/cpuinfo") as f:
                for line in f:
                    if line.startswith("model name"):
                        return line.split(":", 1)[1].strip()
        except Exception:
            pass
    return platform.processor() or "Unknown CPU"


def get_shell() -> str:
    shell_env = os.environ.get("SHELL", "")
    if shell_env:
        name = shell_env.split("/")[-1]
        if name not in ("sh", ""):
            return name
    skip = {"sh", "python", "python3", "python3.11", "python3.12", ""}
    pid = os.getppid()
    for _ in range(5):
        try:
            resolved = os.readlink(f"/proc/{pid}/exe")
            name = resolved.split("/")[-1]
            if name not in skip:
                return name
            with open(f"/proc/{pid}/status") as f:
                for line in f:
                    if line.startswith("PPid:"):
                        pid = int(line.split()[1])
                        break
        except Exception:
            break
    return shell_env.split("/")[-1] if shell_env else "sh"


def get_terminal() -> str:
    for var in ("TERM_PROGRAM", "TERMINAL", "COLORTERM", "TERM"):
        val = os.environ.get(var, "")
        if val:
            return val
    return "unknown"


def get_uptime() -> str:
    seconds = int(time.time() - psutil.boot_time())
    days,    remainder = divmod(seconds, 86400)
    hours,   remainder = divmod(remainder, 3600)
    minutes, _         = divmod(remainder, 60)
    parts = []
    if days:
        parts.append(f"{days}d")
    if hours:
        parts.append(f"{hours}h")
    parts.append(f"{minutes}m")
    return " ".join(parts)


def get_packages() -> str:
    managers = {
        "apt":    ["dpkg-query", "-f", "${binary:Package}\n", "-W"],
        "pacman": ["pacman", "-Qq"],
        "dnf":    ["rpm", "-qa"],
        "apk":    ["apk", "info"],
    }
    for mgr, cmd in managers.items():
        try:
            result = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                timeout=3,
            )
            count = len(result.stdout.decode(errors="ignore").strip().splitlines())
            if count > 0:
                return f"{count} ({mgr})"
        except Exception:
            continue
    return "N/A"


def get_sys_info() -> dict:
    return {
        "user":     getpass.getuser(),
        "host":     platform.node(),
        "os":       get_distro(),
        "kernel":   platform.release().split("-")[0],
        "cpu":      get_cpu_info(),
        "ram": (
            f"{round(psutil.virtual_memory().used  / 1024**3, 2)}GB"
            f" / "
            f"{round(psutil.virtual_memory().total / 1024**3, 2)}GB"
        ),
        "shell":    get_shell(),
        "terminal": get_terminal(),
        "uptime":   get_uptime(),
        "packages": get_packages(),
    }


def build_info_lines(info: dict, color: str) -> list[str]:
    label = lambda k: f"{color}{BOLD}{k}{RESET}{WHITE}"
    sep   = f"{DIM}@{RESET}"
    return [
        f"{BOLD}{info['user']}{sep}{info['host']}{RESET}",
        f"{DIM}{'─' * (len(info['user']) + len(info['host']) + 1)}{RESET}",
        f"{label('OS')}        {info['os']}",
        f"{label('Kernel')}    {info['kernel']}",
        f"{label('CPU')}       {info['cpu']}",
        f"{label('RAM')}       {info['ram']}",
        f"{label('Shell')}     {info['shell']}",
        f"{label('Terminal')}  {info['terminal']}",
        f"{label('Uptime')}    {info['uptime']}",
        f"{label('Packages')}  {info['packages']}",
    ]


def main():
    parser = argparse.ArgumentParser(
        prog="mikufetch",
        description="🎵 System fetch tool — Miku & Teto edition"
    )
    parser.add_argument(
        "--art", "-a",
        choices=["miku", "teto"],
        default=None,
        help="Choose character: miku (default) or teto"
    )
    parser.add_argument(
        "--teto", "-t",
        action="store_true",
        help="Kasane Teto mode 🔴"
    )
    parser.add_argument(
        "--random", "-r",
        action="store_true",
        help="Random character"
    )
    args = parser.parse_args()

    if args.random:
        choice = random.choice(["miku", "teto"])
    elif args.teto:
        choice = "teto"
    elif args.art:
        choice = args.art
    else:
        choice = "miku"

    art   = ARTS[choice]
    color = RED if choice == "teto" else CYAN

    info       = get_sys_info()
    info_lines = build_info_lines(info, color)

    rows       = max(len(art), len(info_lines))
    art_lines  = art        + ["                   "] * (rows - len(art))
    info_lines = info_lines + [""]                   * (rows - len(info_lines))

    print()
    for art_line, info_line in zip(art_lines, info_lines):
        print(f"{art_line}  {info_line}{RESET}")
    print()


if __name__ == "__main__":
    main()