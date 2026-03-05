# Easy QR Generator

Generate QR codes from the command line.

## Requirements

- [Python 3](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

## Setup (one time only)

Clone the repository:

```sh
git clone https://github.com/vmleon/easyqr.git
```

```sh
cd easyqr
```

Create a virtual environment:

```sh
python3 -m venv venv
```

Activate it:

```sh
source venv/bin/activate
```

Install dependencies:

```sh
pip install -r requirements.txt
```

## Usage

Activate the virtual environment:

```sh
source venv/bin/activate
```

Generate a QR code (filename is derived from the URL):

```sh
python easyqr.py "https://example.com/my-page"
# -> output/my-page.png
```

```sh
python easyqr.py "https://example.com"
# -> output/example.png
```

Specify a custom filename:

```sh
python easyqr.py "https://example.com" my-code.png
# -> output/my-code.png
```

The `output/` folder is created automatically if it doesn't exist.
