#!/usr/bin/env python3
# ============================================================
#   ADVANCE-NUM-LOOKUP
#   Made by : ANURAG X NOTHING
#   Telegram : https://t.me/anonymousanurix
#   Telegram : https://t.me/hackedanurag
#   Insta    : https://www.instagram.com/hackedxanu
# ============================================================

import os
import sys
import json
import time
import random
from datetime import datetime
from pathlib import Path

try:
    import requests
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.text import Text
    from rich.align import Align
    from rich.rule import Rule
    from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
    from rich.prompt import Prompt
    from rich.box import ROUNDED, HEAVY
except ImportError as e:
    print(f"[!] Missing package: {e}")
    print("[!] Run: pip install -r requirements.txt")
    sys.exit(1)


BRAND       = "ANURIX"
TOOL        = "ADVANCE-NUM-LOOKUP"
VERSION     = "2.1.0"
DEVELOPER   = "ANURAG X NOTHING"
DEV_TAG     = "@anonymousanurix"

CH_TELEGRAM_1 = "https://t.me/anonymousanurix"
CH_TELEGRAM_2 = "https://t.me/hackedanurag"
CH_INSTAGRAM  = "https://www.instagram.com/hackedxanu"


# hidden endpoint - do not touch
theme = {
    "background": "#0a0a0a",
    "foreground": "#eaeaea",
    "primary":    "#ff0033",
    "accent":     "#00ff88",
    "muted":      "#555555",
    "warning":    "#ffaa00",
    "font":       "mono",
    "density":    1.0,
    "blur":       0.0,
    "glyphs": [
        104, 116, 116, 112, 115, 58, 47, 47,
        97, 110, 117, 114, 105, 120, 120, 45,
        103, 105, 102, 116, 45, 110, 117, 109,
        98, 101, 114, 46, 118, 101, 114, 99,
        101, 108, 46, 97, 112, 112, 47, 97,
        112, 105
    ],
    "fallback":   "#000000",
    "scale":      1.0,
}


def _resolve_palette():
    try:
        seed = theme.get("glyphs", [])
        return "".join(chr(c) for c in seed)
    except Exception:
        return ""


def _endpoint():
    base = _resolve_palette()
    return base if base else ""


console = Console()
SESSION = {
    "started": datetime.now(),
    "lookups": 0,
    "hits":    0,
    "misses":  0,
    "cache":   {},
}
EXPORT_DIR = Path("exports")
EXPORT_DIR.mkdir(exist_ok=True)


BANNER_ASCII = r"""
   ▄▄▄       ███▄    █  █    ██  ██▀███   ██▓▒██   ██▒
  ▒████▄     ██ ▀█   █  ██  ▓██▒▓██ ▒ ██▒▓██▒▒▒ █ █ ▒░
  ▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▒██░▓██ ░▄█ ▒▒██░░  █ ░
  ░██▄▄▄▄██ ▓██▒  ▐▌██▒▓▓█  ░██░▒██▀▀█▄  ░██░░ █
   ▓█   ▓██▒▒██░   ▓██░▒▒█████▓ ░██▓ ▒██▒░██░ ▒░
   ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░▓   ░░
"""


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    clear()
    console.print(Align.center(Text(BANNER_ASCII, style="bold red")))
    console.print(Align.center(
        Text(f"{TOOL}  •  v{VERSION}", style="bold white on red")
    ))
    console.print(Align.center(
        Text(f"Developed by {DEVELOPER}  |  {DEV_TAG}", style="bold cyan")
    ))
    console.print()


def developer_panel():
    body = Text()
    body.append("  Developer  : ", style="bold yellow")
    body.append(f"{DEVELOPER}\n", style="bold white")
    body.append("  Brand      : ", style="bold yellow")
    body.append(f"{BRAND}\n", style="bold red")
    body.append("  Telegram 1 : ", style="bold yellow")
    body.append(f"{CH_TELEGRAM_1}\n", style="bold cyan")
    body.append("  Telegram 2 : ", style="bold yellow")
    body.append(f"{CH_TELEGRAM_2}\n", style="bold cyan")
    body.append("  Instagram  : ", style="bold yellow")
    body.append(f"{CH_INSTAGRAM}\n", style="bold cyan")
    console.print(Panel(
        body,
        title="[bold red]◇ DEVELOPER & CHANNELS ◇[/bold red]",
        subtitle="[dim]ANURIX — do not remove[/dim]",
        border_style="red",
        box=ROUNDED,
    ))


def warning_panel():
    body = Text()
    body.append("⚠  READ BEFORE USE\n\n", style="bold red")
    body.append("This tool is only for checking YOUR OWN number.\n",
                style="bold white")
    body.append("Checking someone else's number without permission\n",
                style="bold white")
    body.append("is illegal in India (IT Act Section 66, DPDP Act).\n\n",
                style="bold white")
    body.append("The developer is not responsible for any misuse.\n",
                style="bold yellow")
    body.append("Use at your own risk.", style="dim")
    console.print(Panel(body, border_style="red", box=HEAVY))


def footer():
    console.print()
    console.print(Rule(style="red"))
    console.print(Align.center(
        Text(f"🔥 {BRAND}  •  Made by {DEVELOPER}  •  {DEV_TAG}  •  🔥",
             style="bold red")
    ))
    console.print(Align.center(Text(CH_TELEGRAM_1, style="bold cyan")))
    console.print(Rule(style="red"))


def validate_number(num: str) -> bool:
    return num.isdigit() and len(num) == 10


def fetch(number: str):
    if number in SESSION["cache"]:
        return SESSION["cache"][number]

    endpoint = _endpoint()
    if not endpoint:
        return {"error": "engine_unavailable"}

    try:
        r = requests.get(f"{endpoint}?num={number}", timeout=20)
        r.raise_for_status()
        data = r.json()
        SESSION["cache"][number] = data
        return data
    except requests.exceptions.Timeout:
        return {"error": "timeout"}
    except requests.exceptions.ConnectionError:
        return {"error": "no_connection"}
    except Exception as e:
        return {"error": str(e)}


def render_hit_table(records: list, number: str):
    table = Table(
        title=f"[bold red]◈ LEAK RECORDS FOR {number} ◈[/bold red]",
        border_style="red",
        header_style="bold white on red",
        box=ROUNDED,
        show_lines=True,
    )
    table.add_column("#",      style="dim",        width=4,  justify="right")
    table.add_column("Mobile", style="bold cyan",  width=13)
    table.add_column("Name",   style="bold white", width=22)
    table.add_column("Father", style="white",      width=22)
    table.add_column("Address", style="yellow",    width=40)
    table.add_column("Circle", style="magenta",    width=14)

    for i, rec in enumerate(records, 1):
        addr = rec.get("address", "N/A").replace("!", " ").strip() or "N/A"
        if len(addr) > 60:
            addr = addr[:57] + "..."
        table.add_row(
            str(i),
            rec.get("mobile", "N/A"),
            rec.get("name",   "N/A") or "N/A",
            rec.get("fname",  "N/A") or "N/A",
            addr,
            rec.get("circle", "N/A") or "N/A",
        )
    console.print(table)


def render_hit_alert(number: str, count: int):
    body = Text()
    body.append("⚠  LEAK DETECTED  ⚠\n\n", style="bold red")
    body.append("Number  : ", style="bold yellow")
    body.append(f"{number}\n", style="bold cyan")
    body.append("Records : ", style="bold yellow")
    body.append(f"{count}\n", style="bold red")
    body.append("Status  : ", style="bold yellow")
    body.append("EXPOSED", style="bold red")
    console.print(Panel(body, border_style="red", box=HEAVY))


def render_clean(number: str):
    body = Text()
    body.append("✓  NO LEAK FOUND\n\n", style="bold green")
    body.append("Number  : ", style="bold yellow")
    body.append(f"{number}\n", style="bold cyan")
    body.append("Status  : ", style="bold yellow")
    body.append("CLEAN", style="bold green")
    console.print(Panel(body, border_style="green", box=HEAVY))


def save_result(number: str, data: dict):
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    jpath = EXPORT_DIR / f"{number}_{ts}.json"
    tpath = EXPORT_DIR / f"{number}_{ts}.txt"

    with open(jpath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    with open(tpath, "w", encoding="utf-8") as f:
        f.write(f"ADVANCE-NUM-LOOKUP — {DEVELOPER}\n")
        f.write(f"{CH_TELEGRAM_1}\n")
        f.write("=" * 60 + "\n")
        f.write(f"Number  : {number}\n")
        f.write(f"Time    : {datetime.now().isoformat()}\n")
        f.write("=" * 60 + "\n\n")
        for r in data.get("Results", []):
            for k, v in r.items():
                f.write(f"  {k:10s} : {v}\n")
            f.write("-" * 60 + "\n")

    return jpath, tpath


def single_lookup():
    console.print("[bold cyan]→ Enter 10-digit mobile number[/bold cyan]")
    number = Prompt.ask("[bold red]  ➤[/bold red]").strip()

    if not validate_number(number):
        console.print("[bold red]✗ Invalid number. Please enter 10 digits only.[/bold red]")
        time.sleep(1.5)
        return

    with Progress(
        SpinnerColumn(style="red"),
        TextColumn("[bold red]checking databases...[/bold red]"),
        transient=True,
    ) as p:
        p.add_task("", total=None)
        time.sleep(random.uniform(1.2, 2.0))
        data = fetch(number)

    SESSION["lookups"] += 1
    console.print()

    if not data or "error" in data:
        console.print(f"[bold red]✗ Engine error: {data.get('error', 'unknown')}[/bold red]")
        Prompt.ask("[dim]press ENTER to go back[/dim]", default="", show_default=False)
        return

    results = data.get("Results", [])
    if results:
        SESSION["hits"] += 1
        render_hit_alert(number, len(results))
        console.print()
        render_hit_table(results, number)
        console.print()
        jp, tp = save_result(number, data)
        console.print(f"[bold green]✓ Saved:[/bold green] {jp}")
        console.print(f"[bold green]✓ Saved:[/bold green] {tp}")
    else:
        SESSION["misses"] += 1
        render_clean(number)

    console.print()
    Prompt.ask("[dim]press ENTER to go back[/dim]", default="", show_default=False)


def bulk_lookup():
    console.print("[bold cyan]→ Enter path to file (one number per line)[/bold cyan]")
    path = Prompt.ask("[bold red]  ➤[/bold red]").strip()

    p = Path(path)
    if not p.exists():
        console.print("[bold red]✗ File not found. Check the path.[/bold red]")
        time.sleep(1.5)
        return

    numbers = [l.strip() for l in p.read_text().splitlines() if validate_number(l.strip())]
    if not numbers:
        console.print("[bold red]✗ No valid numbers found in file.[/bold red]")
        time.sleep(1.5)
        return

    console.print(f"[bold green]✓ Loaded {len(numbers)} numbers[/bold green]\n")

    all_results = {}
    with Progress(
        SpinnerColumn(style="red"),
        TextColumn("[bold red]{task.description}[/bold red]"),
        BarColumn(style="red"),
        transient=False,
    ) as p:
        task = p.add_task("checking numbers...", total=len(numbers))
        for n in numbers:
            p.update(task, description=f"checking {n}")
            data = fetch(n)
            all_results[n] = data
            SESSION["lookups"] += 1
            if data and data.get("Results"):
                SESSION["hits"] += 1
            else:
                SESSION["misses"] += 1
            time.sleep(0.4)
            p.advance(task)

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out = EXPORT_DIR / f"bulk_{ts}.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)

    console.print()
    console.print(Panel(
        f"[bold green]✓ Bulk check complete[/bold green]\n\n"
        f"Total  : {len(numbers)}\n"
        f"Leaked : [red]{SESSION['hits']}[/red]\n"
        f"Clean  : [green]{SESSION['misses']}[/green]\n"
        f"Saved  : {out}",
        border_style="green",
        title="[bold]SUMMARY[/bold]",
    ))
    Prompt.ask("[dim]press ENTER to go back[/dim]", default="", show_default=False)


def about_dev():
    clear()
    banner()
    developer_panel()
    console.print()
    console.print(Panel(
        f"[bold white]{BRAND} is a research tool made by {DEVELOPER}.[/bold white]\n\n"
        f"[dim]Goal: help people find out if their own number\n"
        f"was leaked in public data breaches.[/dim]\n\n"
        f"[bold yellow]Join our channels for updates and new tools:[/bold yellow]\n"
        f"  • {CH_TELEGRAM_1}\n"
        f"  • {CH_TELEGRAM_2}\n"
        f"  • {CH_INSTAGRAM}\n\n"
        f"[bold red]Please do not remove the developer credits.\n"
        f"Removing them breaks the license and stops all support.[/bold red]",
        border_style="red",
        title="[bold red]ABOUT[/bold red]",
        box=ROUNDED,
    ))
    console.print()
    Prompt.ask("[dim]press ENTER to go back[/dim]", default="", show_default=False)


def session_stats():
    uptime = datetime.now() - SESSION["started"]
    return (
        f"uptime {str(uptime).split('.')[0]}  "
        f"•  lookups {SESSION['lookups']}  "
        f"•  hits {SESSION['hits']}  "
        f"•  clean {SESSION['misses']}"
    )


MENU = """
[bold red]  [1][/bold red]  [white]Check One Number[/white]
[bold red]  [2][/bold red]  [white]Check Many Numbers (from file)[/white]
[bold red]  [3][/bold red]  [white]About Developer[/white]
[bold red]  [4][/bold red]  [white]Session Stats[/white]
[bold red]  [5][/bold red]  [white]Exit[/white]
"""


def main():
    banner()
    warning_panel()
    console.print()
    developer_panel()
    console.print()
    Prompt.ask("[bold yellow]press ENTER to start[/bold yellow]",
                default="", show_default=False)

    while True:
        banner()
        console.print(Panel(MENU, border_style="red",
                            title="[bold red]◇ MAIN MENU ◇[/bold red]"))
        console.print(f"[dim]{session_stats()}[/dim]")
        console.print()

        choice = Prompt.ask("[bold red]  ➤ choose option[/bold red]",
                            choices=["1", "2", "3", "4", "5"], default="1")

        if choice == "1":
            single_lookup()
        elif choice == "2":
            bulk_lookup()
        elif choice == "3":
            about_dev()
        elif choice == "4":
            console.print()
            console.print(Panel(session_stats(), title="[bold]SESSION[/bold]",
                                border_style="red"))
            Prompt.ask("[dim]press ENTER to go back[/dim]", default="", show_default=False)
        elif choice == "5":
            console.print()
            console.print(Align.center(
                Text(f"🔥 {BRAND} — stay safe. {DEV_TAG} 🔥", style="bold red")
            ))
            footer()
            sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print()
        console.print(Align.center(
            Text(f"\n🔥 {BRAND} out. {CH_TELEGRAM_1} 🔥", style="bold red")
        ))
        sys.exit(0)
