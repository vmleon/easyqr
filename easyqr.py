#!/usr/bin/env python3
import sys
import os
import re
from urllib.parse import urlparse
import qrcode


def filename_from_url(url):
    parsed = urlparse(url)
    # Use the last non-empty path segment, or fall back to the hostname
    path = parsed.path.rstrip("/")
    name = os.path.basename(path) if path else parsed.hostname or "qrcode"
    # Strip existing extension, sanitize, and collapse repeated separators
    name = os.path.splitext(name)[0]
    name = re.sub(r"[^\w\-.]", "_", name)
    name = re.sub(r"_+", "_", name).strip("_")
    return (name or "qrcode") + ".png"


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {os.path.basename(sys.argv[0])} <url> [output.png]")
        sys.exit(1)

    url = sys.argv[1]
    output = sys.argv[2] if len(sys.argv) > 2 else filename_from_url(url)

    if not output.endswith(".png"):
        output += ".png"

    img = qrcode.make(url, box_size=10)
    img.save(output)
    print(f"QR code saved to {output}")

if __name__ == "__main__":
    main()
