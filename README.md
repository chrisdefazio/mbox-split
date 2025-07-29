# Mbox Split

A Python utility to split large mbox files into smaller chunks for easier processing and management.

## Features

- Splits large mbox files into smaller chunks of configurable size
- Progress tracking during processing
- Configurable output directory and chunk size
- Handles large files efficiently with memory-conscious processing

## Usage

1. Update the `INPUT_MBOX` variable in `mbox-split.py` to point to your mbox file
2. Optionally adjust `MESSAGES_PER_CHUNK` to change the number of messages per chunk (default: 5000)
3. Run the script:

```bash
python mbox-split.py
```

## Configuration

- `INPUT_MBOX`: Path to the input mbox file
- `OUTPUT_DIR`: Directory where chunk files will be saved (default: "mbox_chunks")
- `MESSAGES_PER_CHUNK`: Number of messages per chunk file (default: 5000)
- `PROGRESS_EVERY`: How often to show progress updates (default: 1000 messages)

## Output

The script creates numbered chunk files in the format `chunk_XXX.mbox` where XXX is a zero-padded three-digit number.

## Requirements

- Python 3.x
- Standard library modules: `mailbox`, `os`, `time`

## License

Private project - not for public distribution. 