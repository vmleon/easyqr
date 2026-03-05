# Easy QR Generator

Generate QR codes from the command line.

## Setup (one time only)

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
# -> my-page.png
```

```sh
python easyqr.py "https://example.com"
# -> example.png
```

Specify a custom filename:

```sh
python easyqr.py "https://example.com" my-code.png
```
