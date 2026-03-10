# 🐚 codecrafters-shell-python

[![progress-banner](https://backend.codecrafters.io/progress/shell/32df0c49-474a-4313-baf0-2953234a6d6c)](https://app.codecrafters.io/users/rafnixg?r=2qF)
![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A POSIX-compatible shell implementation written in Python, built as part of the
["Build Your Own Shell" Challenge](https://app.codecrafters.io/courses/shell/overview) on CodeCrafters.

> **Note**: If you're viewing this repo on GitHub, head over to
> [codecrafters.io](https://codecrafters.io) to try the challenge yourself!

---

## ✨ Features

- **Interactive REPL loop** — displays a `$ ` prompt and reads user input continuously.
- **Built-in commands:**
  - `echo <args>` — prints arguments to standard output.
  - `type <command>` — identifies whether a command is a shell builtin or an external executable (and shows its path).
  - `exit` — exits the shell with status code `0`.
- **External command execution** — discovers and runs any executable found on the system `PATH`.
- **Command not found handling** — writes a clear error message to `stderr` when a command cannot be resolved.

---

## 📁 Project Structure

```
.
├── app/
│   └── main.py        # Shell implementation (Shell class + entry point)
├── your_shell.sh      # Script used by CodeCrafters to invoke the shell
├── Pipfile            # Python dependency manifest
├── Pipfile.lock       # Locked dependency versions
└── codecrafters.yml   # CodeCrafters configuration (Python 3.12)
```

---

## 🚀 Getting Started

### Prerequisites

- Python **3.12**
- [Pipenv](https://pipenv.pypa.io/en/latest/)

### Installation

```sh
# Clone the repository
git clone https://github.com/rafnixg/codecrafters-shell-python.git
cd codecrafters-shell-python

# Install dependencies
pipenv install
```

### Running the shell

```sh
./your_shell.sh
```

You will be greeted with the `$ ` prompt. Type any of the supported commands:

```
$ echo Hello, World!
Hello, World!
$ type echo
echo is a shell builtin
$ type ls
ls is /bin/ls
$ ls -la
... (output of ls)
$ exit
```

---

## 🛠️ How It Works

The core logic lives in `app/main.py` inside the `Shell` class:

1. **`main()`** — Starts the REPL loop, printing the prompt and reading input on each iteration.
2. **`get_user_input()`** — Splits raw input into a command token and a list of arguments.
3. **Built-in dispatch** — If the command matches a key in the `commands` dict, the corresponding handler is called directly.
4. **PATH lookup** — For unknown commands, `get_command_path()` walks each directory in `$PATH` and checks for an executable file.
5. **`run_os_command()`** — Delegates execution to `subprocess.run()` for external programs.
6. **Error handling** — Unresolvable commands are reported on `stderr` via `handle_not_found()`.

---

## 📬 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to open an [issue](https://github.com/rafnixg/codecrafters-shell-python/issues) or submit a pull request.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
