"""Main module of the app."""

import os
import subprocess
import sys

from pathlib import Path

class Shell:
    """Shell class to handle the shell commands.
    Example:
        $ echo Hello World
        Hello World
        $ type echo
        echo is a shell builtin
        $ type ls
        ls is /bin/ls
        $ exit
        
    """

    commands: dict = {}
    command: str = ""
    args: list[str] = []

    def __init__(self):
        self.commands = {
            "exit": self.handle_exit,
            "echo": self.handle_echo,
            "type": self.handle_type,
        }

    def get_user_input(self) -> tuple[str, list[str]]:
        """Get the user input and return the command and the arguments."""
        user_input = input().split()
        command = user_input[0] if len(user_input) > 0 else ""
        args = user_input[1:] if len(user_input) > 1 else []
        self.command = command
        self.args = args
        return command, args

    def handle_not_found(self, command: str) -> None:
        """Handle the command not found."""
        sys.stderr.write(f"{command}: command not found\n")
        sys.stderr.flush()

    def run_os_command(self, command: str, args: list) -> None:
        """Run an external command from the PATH with the given arguments"""
        command_path = self.get_command_path(command)
        subprocess.run([command_path] + args, check=True)
        sys.stdout.flush()

    def check_command(self, command: str) -> bool:
        """Check if the command exists in the PATH."""
        return self.get_command_path(command) is not None

    def get_command_path(self, command: str) -> str:
        """Get the command path."""
        for path in os.environ["PATH"].split(os.pathsep):
            command_path = Path(path) / command
            if command_path.exists():
                return str(command_path)
        return None

    def handle_exit(self, args: list) -> None:
        """Handle the exit command."""
        sys.exit(0)

    def handle_echo(self, args: list) -> None:
        """Handle the echo command."""
        sys.stdout.write(" ".join(args) + "\n")
        sys.stdout.flush()

    def handle_type(self, args: list) -> None:
        """Handle the type command."""
        command = args[0]
        if command in self.commands:
            sys.stdout.write(f"{command} is a shell builtin\n")
        elif self.check_command(command):
            command_path = self.get_command_path(command)
            sys.stdout.write(f"{command} is {command_path}\n")
        else:
            sys.stdout.write(f"{command}: not found\n")

    def print_prompt(self) -> None:
        """Print the prompt."""
        sys.stdout.write("$ ")
        sys.stdout.flush()

    @staticmethod
    def run():
        """Run the shell."""
        Shell().main()

    def main(self):
        """Main entry point of the app."""
        while True:
            # Print the prompt
            self.print_prompt()
            # Get the input command and arguments
            self.get_user_input()
            # Check if the command is empty
            if not self.command:
                continue
            # Check if the command is in the list of commands
            if self.command in self.commands:
                # Execute the command
                self.commands[self.command](self.args)
                continue
            # Check if the command exists in the PATH
            if not self.check_command(self.command):
                self.handle_not_found(self.command)
                continue
            # Run the os command
            self.run_os_command(self.command, self.args)


def main():
    """Main entry point of the app."""

    Shell.run()


if __name__ == "__main__":
    main()
    sys.exit(0)
