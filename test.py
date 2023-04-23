from rich.console import Console
from rich.panel import Panel

def main():
    # Set up the info panel
    console = Console()
    title = Panel("Info Panel", style="bold")
    cpu_usage = "CPU usage: [bold green]50%[/]"
    memory_usage = "Memory usage: [bold yellow]75%[/]"
    disk_usage = "Disk usage: [bold blue]40%[/]"
    content = "\n".join([cpu_usage, memory_usage, disk_usage])
    panel = Panel(content, title=title)

    # Print the info panel to the console
    console.print(panel)

main()