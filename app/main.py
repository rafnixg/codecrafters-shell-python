"""Main module of the app."""

import os
import subprocess
import sys

from pathlib import Path


def check_command(command: str) -> bool:
    """Check if the command exists in the PATH."""
    return get_command_path(command) is not None


def get_command_path(command: str) -> str:
    """Get the command path."""
    for path in os.environ["PATH"].split(os.pathsep):
        command_path = Path(path) / command
        if command_path.exists():
            return str(command_path)
    return None


def run_os_command(command: str, args: list) -> None:
    """Run an external command from the PATH with the given arguments"""
    command_path = get_command_path(command)
    subprocess.run([command_path] + args, check=True)
    sys.stdout.flush()


def handle_exit(args: list) -> None:
    """Handle the exit command."""
    sys.exit(0)


def handle_not_found(command: str) -> None:
    """Handle the command not found."""
    sys.stderr.write(f"{command}: command not found\n")
    sys.stderr.flush()


def handle_echo(args: list) -> None:
    """Handle the echo command."""
    sys.stdout.write(" ".join(args) + "\n")
    sys.stdout.flush()


def handle_type(args: list) -> None:
    """Handle the type command."""
    command = args[0]
    if command in get_commands():
        sys.stdout.write(f"{command} is a shell builtin\n")
    elif check_command(command):
        command_path = get_command_path(command)
        sys.stdout.write(f"{command} is {command_path}\n")
    else:
        sys.stdout.write(f"{command}: not found\n")


def print_prompt() -> None:
    """Print the prompt."""
    sys.stdout.write("$ ")
    sys.stdout.flush()


def get_commands() -> dict:
    """Get the list of commands."""
    return {"exit": handle_exit, "echo": handle_echo, "type": handle_type}


def get_user_input() -> tuple[str, list[str]]:
    """Get the user input and return the command and the arguments."""
    user_input = input().split()
    command = user_input[0] if len(user_input) > 0 else ""
    args = user_input[1:] if len(user_input) > 1 else []
    return command, args


def main():
    """Main entry point of the app."""
    command_list = get_commands()
    while True:
        # Print the prompt
        print_prompt()
        # Get the input command and arguments
        command, args = get_user_input()
        # Check if the command is empty
        if not command:
            continue
        # Check if the command is in the list of commands
        if command in command_list:
            # Execute the command
            command_list[command](args)
            continue
        # Check if the command exists in the PATH
        if not check_command(command):
            handle_not_found(command)
            continue
        # Run the os command
        run_os_command(command, args)


if __name__ == "__main__":
    main()
    sys.exit(0)
