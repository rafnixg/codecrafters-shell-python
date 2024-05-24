"""Main module of the app."""

import sys


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
    else:
        sys.stdout.write(f"{command} not found\n")


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
        if command not in command_list:
            handle_not_found(command)
            continue
        # Execute the command
        command_list[command](args)


if __name__ == "__main__":
    main()
    sys.exit(0)
