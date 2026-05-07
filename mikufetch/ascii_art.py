CYAN  = "\033[96m"
RED   = "\033[91m"
WHITE = "\033[97m"
RESET = "\033[0m"

MIKU_LINES = [
    r"   ||       ||   ",
    r"   ||       ||   ",
    r"  (  \_____/  )  ",
    r"  |  (^   ^)  |  ",
    r"  |     u     |  ",
    r"  |  ~-----~  |  ",
    r"  |   [===]   |  ",
    r"   \   | |   /   ",
    r"    \  | |  /    ",
    r"   /\  | |  /\   ",
    r"  /  \_|_|_/  \  ",
    r" /   MIKU  39  \  ",
]

TETO_LINES = [
    r"   /\       /\  ",
    r"  /  \_____/  \ ",
    r" | drill  hair | ",
    r"  \  (>w<)  /  ",
    r"   |  ___  |   ",
    r"   | [===] |   ",
    r"   |  | |  |   ",
    r"    \ | | /    ",
    r"   /\| | |/\   ",
    r"  /  \| |/  \  ",
    r" / KASANE TETO \ ",
    r"/   UTAU  100  \ ",
]

MIKU_ART = [f"{CYAN}{line}{RESET}" for line in MIKU_LINES]
TETO_ART = [f"{RED}{line}{RESET}"  for line in TETO_LINES]

ARTS = {
    "miku": MIKU_ART,
    "teto": TETO_ART,
}