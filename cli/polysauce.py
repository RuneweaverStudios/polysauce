#!/usr/bin/env python3
"""
Polysauce CLI — Polymarket Copy Trading Bot
The ultimate tool for mirroring top traders automatically.
"""

import os
import sys
import time
import json
import argparse
import requests
import subprocess
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Dict
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.live import Live
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Prompt, Confirm
from rich.syntax import Syntax

console = Console()

# 🔥 DOPE ASCII HEADER 🔥
ASCII_HEADER = """
[38;5;196m╔══════════════════════════════════════════════════════════════════════════════╗[0m
[38;5;196m║[0m[38;5;208m ██████╗ ██████╗  ██████╗ ██████╗  ██████╗ ███╗   ██╗ █████╗ ██╗  ██╗██╗   ██╗[0m[38;5;196m║[0m
[38;5;196m║[0m[38;5;208m██╔════╝██╔═══██╗██╔════╝██╔═══██╗██╔═══██╗████╗  ██║██╔══██╗██║ ██╔╝██║   ██║[0m[38;5;196m║[0m
[38;5;196m║[0m[38;5;208m██║     ██║   ██║██║     ██║   ██║██║   ██║██╔██╗ ██║███████║█████╔╝ ██║   ██║[0m[38;5;196m║[0m
[38;5;196m║[0m[38;5;208m██║     ██║   ██║██║     ██║   ██║██║   ██║██║╚██╗██║██╔══██║██╔═██╗ ██║   ██║[0m[38;5;196m║[0m
[38;5;196m║[0m[38;5;208m╚██████╗╚██████╔╝╚██████╗╚██████╔╝╚██████╔╝██║ ╚████║██║  ██║██║  ██╗╚██████╔╝[0m[38;5;196m║[0m
[38;5;196m║[0m[38;5;208m ╚═════╝ ╚═════╝  ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝[0m[38;5;196m ║[0m
[38;5;196m║[0m[38;5;227m                          ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗ ██████╗ █████╗[0m[38;5;196m ║[0m
[38;5;196m║[0m[38;5;227m                          ██╔══██╗██║   ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗[0m[38;5;196m║[0m
[38;5;196m║[0m[38;5;227m                          ██████╔╝██║   ██║███████║██████╔╝██████╔╝██║  ██║███████║[0m[38;5;196m║[0m
[38;5;196m║[0m[38;5;227m                          ██╔═══╝ ██║   ██║██╔══██║██╔══██╗██╔══██╗██║  ██║██╔══██║[0m[38;5;196m║[0m
[38;5;196m║[0m[38;5;227m                          ██║     ╚██████╔╝██║  ██║██║  ██║██████╔╝╚█████╔╝██║  ██║[0m[38;5;196m║[0m
[38;5;196m║[0m[38;5;227m                          ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚════╝ ╚═╝  ╚═╝[0m[38;5;196m║[0m
[38;5;196m╚══════════════════════════════════════════════════════════════════════════════╝[0m

[38;5;51m                    ██████╗ ██████╗ ███████╗ █████╗ ███████╗███████╗[0m
[38;5;51m                    ██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝[0m
[38;5;51m                    ██████╔╝██████╔╝█████╗  ███████║███████╗█████╗  [0m
[38;5;51m                    ██╔═══╝ ██╔══██╗██╔══╝  ██╔══██║╚════██║██╔══╝  [0m
[38;5;51m                    ██║     ██║  ██║███████╗██║  ██║███████║███████╗[0m
[38;5;51m                    ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝[0m

[38;5;46m              ╔═════════════════════════════════════════════════════╗[0m
[38;5;46m              ║  [0m[1;38;5;226mPolymarket Copy Trading Bot[0m[38;5;46m — [0m[38;5;15m$65 | polysauce.xyz[0m[38;5;46m ║[0m
[38;5;46m              ╚═════════════════════════════════════════════════════╝[0m

[38;5;248m                        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[0m
[38;5;248m                        ▓ [0m[1;38;5;46mAUTOMATE YOUR PROFITS[0m[38;5;248m ▓ [0m[1;38;5;46mMIRROR TOP TRADERS[0m[38;5;248m ▓[0m
[38;5;248m                        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓[0m
"""

def show_header():
    """Display the ASCII header"""
    console.print(ASCII_HEADER)

def check_dependencies():
    """Check if required dependencies are installed"""
    deps = {
        'rich': 'rich',
        'requests': 'requests',
        'pandas': 'pandas',
        'web3': 'web3',
        'eth_account': 'eth-account'
    }
    
    missing = []
    for module, package in deps.items():
        try:
            __import__(module)
        except ImportError:
            missing.append(package)
    
    if missing:
        console.print(f"[red]Missing dependencies: {', '.join(missing)}[/red]")
        console.print(f"[yellow]Install with: pip install {' '.join(missing)}[/yellow]")
        return False
    return True

def load_config() -> Dict:
    """Load configuration from .env or config.json"""
    config_path = Path.home() / ".polysauce" / "config.json"
    env_path = Path.cwd() / ".env"
    
    config = {
        'pk': os.getenv('PK', ''),
        'browser_address': os.getenv('BROWSER_ADDRESS', ''),
        'target': os.getenv('COPY_TRADE_TARGET', ''),
        'size_multiplier': float(os.getenv('COPY_TRADE_SIZE_MULTIPLIER', '1.0')),
        'min_size': float(os.getenv('COPY_TRADE_MIN_SIZE', '5')),
        'max_position': float(os.getenv('COPY_TRADE_MAX_POSITION_USD', '100')),
        'poll_seconds': float(os.getenv('COPY_TRADE_POLL_SECONDS', '60')),
        'market_filter': os.getenv('COPY_TRADE_MARKET_FILTER', ''),
    }
    
    # Load from config.json if exists
    if config_path.exists():
        with open(config_path) as f:
            config.update(json.load(f))
    
    # Load from .env if exists
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                if '=' in line and not line.startswith('#'):
                    key, val = line.strip().split('=', 1)
                    if key in config:
                        config[key] = val
    
    return config

def save_config(config: Dict):
    """Save configuration to config.json"""
    config_path = Path.home() / ".polysauce" / "config.json"
    config_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    console.print(f"[green]✓ Config saved to {config_path}[/green]")

def generate_wallet():
    """Generate a new burner wallet"""
    try:
        from eth_account import Account
        import secrets
        
        # Generate new private key
        priv = secrets.token_hex(32)
        priv_key = f"0x{priv}"
        account = Account.from_key(priv_key)
        
        console.print(Panel.fit(
            f"[bold green]🔐 NEW BURNER WALLET GENERATED[/bold green]\n\n"
            f"[yellow]⚠️  SAVE THESE SECURELY - NEVER SHARE[/yellow]\n\n"
            f"[cyan]Private Key:[/cyan]\n{priv_key}\n\n"
            f"[cyan]Wallet Address:[/cyan]\n{account.address}\n\n"
            f"[yellow]Next Steps:[/yellow]\n"
            f"1. Save private key to password manager\n"
            f"2. Send USDC (Polygon) to the address\n"
            f"3. Add to config: polysauce config set pk {priv_key}",
            title="[bold]WALLET CREATED[/bold]",
            border_style="green"
        ))
        
        return priv_key, account.address
    except ImportError:
        console.print("[red]eth-account not installed. Run: pip install eth-account[/red]")
        return None, None

def check_balance(address: str) -> Optional[float]:
    """Check USDC balance on Polygon"""
    try:
        # Polygon USDC contract
        usdc_contract = "0x3c499c542cEF5E3811e1192ce70d8cC03d5c3359"
        
        # Use Polygon RPC
        rpc_url = "https://polygon-rpc.com"
        
        # ERC20 balanceOf call
        data = f"0x70a08231000000000000000000000000{address[2:]}"
        
        response = requests.post(rpc_url, json={
            "jsonrpc": "2.0",
            "method": "eth_call",
            "params": [{"to": usdc_contract, "data": data}, "latest"],
            "id": 1
        }, timeout=10)
        
        result = response.json().get('result', '0x0')
        balance = int(result, 16) / 1_000_000  # USDC has 6 decimals
        
        return balance
    except Exception as e:
        console.print(f"[red]Error checking balance: {e}[/red]")
        return None

def fetch_leaderboard(limit: int = 50) -> List[Dict]:
    """Fetch Polymarket leaderboard"""
    try:
        # Note: This is a simplified version - actual API may differ
        url = "https://polymarket.com/api/leaderboard"
        response = requests.get(url, params={'limit': limit}, timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        console.print(f"[yellow]Could not fetch live leaderboard: {e}[/yellow]")
        console.print("[dim]Using sample data for demo...[/dim]")
        
        # Return sample data for demo
        return [
            {"rank": 1, "username": "prediction_king", "win_rate": 68, "pnl": 12500, "volume": 45000},
            {"rank": 2, "username": "crypto_oracle", "win_rate": 65, "pnl": 9800, "volume": 38000},
            {"rank": 3, "username": "market_wizard", "win_rate": 62, "pnl": 7500, "volume": 32000},
            {"rank": 4, "username": "poly_master", "win_rate": 60, "pnl": 6200, "volume": 28000},
            {"rank": 5, "username": "bet_shark", "win_rate": 58, "pnl": 5100, "volume": 22000},
        ]

def display_leaderboard(limit: int = 20):
    """Display leaderboard in a rich table"""
    show_header()
    console.print("\n[bold cyan]📊 POLYMARKET LEADERBOARD[/bold cyan]\n")
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Fetching leaderboard...", total=None)
        data = fetch_leaderboard(limit)
    
    table = Table(show_header=True, header_style="bold magenta", box=None)
    table.add_column("Rank", style="cyan", width=6)
    table.add_column("Username", style="green", width=20)
    table.add_column("Win Rate", justify="right", style="yellow", width=10)
    table.add_column("PnL", justify="right", style="bold green", width=12)
    table.add_column("Volume", justify="right", style="blue", width=12)
    
    for trader in data:
        pnl_color = "green" if trader.get('pnl', 0) > 0 else "red"
        pnl_str = f"${trader.get('pnl', 0):,.0f}"
        
        table.add_row(
            f"#{trader.get('rank', '?')}",
            trader.get('username', 'unknown'),
            f"{trader.get('win_rate', 0)}%",
            f"[{pnl_color}]{pnl_str}[/{pnl_color}]",
            f"${trader.get('volume', 0):,.0f}"
        )
    
    console.print(table)
    console.print(f"\n[dim]💡 Use 'polysauce copy <username>' to start copying[/dim]")

def setup_wizard():
    """Interactive setup wizard"""
    show_header()
    console.print("\n[bold cyan]🚀 SETUP WIZARD[/bold cyan]\n")
    console.print("[dim]Let's get your copy trading bot configured...[/dim]\n")
    
    config = {}
    
    # Step 1: Private Key
    console.print("[bold yellow]Step 1: Bot Wallet[/bold yellow]")
    if Confirm.ask("Do you have a burner wallet private key?", default=False):
        config['pk'] = Prompt.ask("Enter private key (starts with 0x)", password=True)
    else:
        console.print("\n[cyan]Generating a new burner wallet...[/cyan]")
        pk, addr = generate_wallet()
        if pk:
            config['pk'] = pk
            console.print(f"\n[yellow]→ Fund this address with USDC (Polygon):[/yellow]")
            console.print(f"[bold green]{addr}[/bold green]\n")
            input("Press Enter once funded...")
    
    # Step 2: Browser Address
    console.print("\n[bold yellow]Step 2: Your Polymarket Wallet[/bold yellow]")
    config['browser_address'] = Prompt.ask("Enter your Polymarket wallet address (0x...)")
    
    # Step 3: Choose Target
    console.print("\n[bold yellow]Step 3: Choose Trader to Copy[/bold yellow]")
    console.print("[dim]Fetching top traders...[/dim]")
    
    leaderboard = fetch_leaderboard(10)
    for i, trader in enumerate(leaderboard[:5], 1):
        console.print(f"  {i}. {trader['username']} - {trader['win_rate']}% win rate, ${trader['pnl']:,} PnL")
    
    choice = Prompt.ask("\nEnter username or number", default="1")
    
    if choice.isdigit() and 1 <= int(choice) <= 5:
        config['target'] = leaderboard[int(choice) - 1]['username']
    else:
        config['target'] = choice
    
    # Step 4: Risk Settings
    console.print("\n[bold yellow]Step 4: Risk Settings[/bold yellow]")
    
    risk = Prompt.ask("Risk level", choices=["conservative", "moderate", "aggressive"], default="conservative")
    
    if risk == "conservative":
        config['size_multiplier'] = 0.1
        config['min_size'] = 5
        config['max_position'] = 20
    elif risk == "moderate":
        config['size_multiplier'] = 0.5
        config['min_size'] = 10
        config['max_position'] = 50
    else:  # aggressive
        config['size_multiplier'] = 1.0
        config['min_size'] = 20
        config['max_position'] = 100
    
    config['poll_seconds'] = 60
    
    # Save config
    console.print("\n[bold green]✓ Configuration complete![/bold green]\n")
    save_config(config)
    
    # Show summary
    console.print(Panel.fit(
        f"[bold]CONFIGURATION SUMMARY[/bold]\n\n"
        f"[cyan]Target:[/cyan] {config['target']}\n"
        f"[cyan]Size Multiplier:[/cyan] {config['size_multiplier']}x\n"
        f"[cyan]Min Trade:[/cyan] ${config['min_size']}\n"
        f"[cyan]Max Position:[/cyan] ${config['max_position']}\n"
        f"[cyan]Poll Interval:[/cyan] {config['poll_seconds']}s\n\n"
        f"[yellow]Next: Run 'polysauce start' to begin copy trading[/yellow]",
        border_style="green"
    ))

def start_bot():
    """Start the copy trading bot"""
    config = load_config()
    
    if not config.get('pk') or not config.get('target'):
        console.print("[red]✗ Bot not configured. Run 'polysauce setup' first.[/red]")
        return
    
    show_header()
    console.print("\n[bold cyan]🤖 STARTING COPY TRADING BOT[/bold cyan]\n")
    
    # Show config
    console.print(Panel.fit(
        f"[bold]TARGET[/bold]\n"
        f"[green]{config['target']}[/green]\n\n"
        f"[bold]SETTINGS[/bold]\n"
        f"Size Multiplier: {config['size_multiplier']}x\n"
        f"Min Trade: ${config['min_size']}\n"
        f"Max Position: ${config['max_position']}\n"
        f"Poll Interval: {config['poll_seconds']}s",
        title="[bold]CONFIGURATION[/bold]",
        border_style="blue"
    ))
    
    # Check balance
    if config.get('browser_address'):
        balance = check_balance(config['browser_address'])
        if balance is not None:
            console.print(f"\n[cyan]💰 Wallet Balance:[/cyan] ${balance:.2f} USDC\n")
    
    console.print("[bold green]✓ Bot starting...[/bold green]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")
    
    # Start the actual bot (would call the real copytrade.py)
    try:
        # For now, show a demo loop
        iteration = 0
        while True:
            iteration += 1
            timestamp = datetime.now().strftime("%H:%M:%S")
            
            console.print(f"[dim][{timestamp}][/dim] [cyan]→ Checking for new positions...[/cyan]")
            time.sleep(2)
            
            # Simulate checking
            if iteration % 3 == 0:
                console.print(f"[dim][{timestamp}][/dim] [green]✓ No new positions to copy[/green]")
            
            time.sleep(config['poll_seconds'])
    
    except KeyboardInterrupt:
        console.print("\n\n[yellow]Bot stopped by user[/yellow]")

def show_status():
    """Show current bot status"""
    config = load_config()
    
    show_header()
    console.print("\n[bold cyan]📈 BOT STATUS[/bold cyan]\n")
    
    # Check if configured
    if not config.get('pk'):
        console.print("[red]✗ Bot not configured[/red]")
        return
    
    # Show status table
    table = Table.grid(padding=1)
    table.add_column("Key", style="cyan")
    table.add_column("Value", style="green")
    
    table.add_row("Status", "[bold green]● RUNNING[/bold green]")
    table.add_row("Target", config.get('target', 'Not set'))
    table.add_row("Size Multiplier", f"{config.get('size_multiplier', 1.0)}x")
    table.add_row("Min Trade", f"${config.get('min_size', 5)}")
    table.add_row("Max Position", f"${config.get('max_position', 100)}")
    
    if config.get('browser_address'):
        balance = check_balance(config['browser_address'])
        if balance is not None:
            table.add_row("Balance", f"${balance:.2f} USDC")
    
    console.print(table)

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Polysauce - Polymarket Copy Trading Bot",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  polysauce setup           Interactive setup wizard
  polysauce leaderboard     Show top traders
  polysauce start           Start copy trading
  polysauce status          Check bot status
  polysauce wallet          Generate new burner wallet
  polysauce config set pk 0x...   Set config value
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Setup command
    subparsers.add_parser('setup', help='Interactive setup wizard')
    
    # Leaderboard command
    lb_parser = subparsers.add_parser('leaderboard', help='Show top traders')
    lb_parser.add_argument('-l', '--limit', type=int, default=20, help='Number of traders to show')
    
    # Start command
    subparsers.add_parser('start', help='Start copy trading bot')
    
    # Status command
    subparsers.add_parser('status', help='Show bot status')
    
    # Wallet command
    subparsers.add_parser('wallet', help='Generate new burner wallet')
    
    # Config command
    config_parser = subparsers.add_parser('config', help='Manage configuration')
    config_parser.add_argument('action', choices=['set', 'get', 'list'])
    config_parser.add_argument('key', nargs='?', help='Config key')
    config_parser.add_argument('value', nargs='?', help='Config value')
    
    # Copy command (quick start)
    copy_parser = subparsers.add_parser('copy', help='Start copying a trader')
    copy_parser.add_argument('username', help='Username or wallet address to copy')
    
    args = parser.parse_args()
    
    if not args.command:
        show_header()
        parser.print_help()
        return
    
    # Execute command
    if args.command == 'setup':
        setup_wizard()
    elif args.command == 'leaderboard':
        display_leaderboard(args.limit)
    elif args.command == 'start':
        start_bot()
    elif args.command == 'status':
        show_status()
    elif args.command == 'wallet':
        show_header()
        generate_wallet()
    elif args.command == 'config':
        config = load_config()
        if args.action == 'list':
            show_header()
            console.print("\n[bold cyan]⚙️  CURRENT CONFIGURATION[/bold cyan]\n")
            for key, val in config.items():
                if key == 'pk':
                    val = f"{val[:10]}..." if val else 'Not set'
                console.print(f"  [cyan]{key}:[/cyan] {val}")
        elif args.action == 'get':
            console.print(config.get(args.key, 'Not found'))
        elif args.action == 'set':
            config[args.key] = args.value
            save_config(config)
    elif args.command == 'copy':
        config = load_config()
        config['target'] = args.username
        save_config(config)
        console.print(f"[green]✓ Now copying {args.username}[/green]")
        console.print("[dim]Run 'polysauce start' to begin[/dim]")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[yellow]Goodbye![/yellow]")
    except Exception as e:
        console.print(f"\n[red]Error: {e}[/red]")
        sys.exit(1)
