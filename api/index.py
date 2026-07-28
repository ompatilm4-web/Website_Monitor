import os
import sys

# Make sure the project root (one level up from /api) is importable so
# "import core..." inside main.py resolves correctly on Vercel.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from main import app  # noqa: E402  (Flask app instance, used as the WSGI handler)

# Vercel's Python runtime looks for a WSGI-compatible "app" object.
