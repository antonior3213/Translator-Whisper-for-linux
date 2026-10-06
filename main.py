"""Punto de entrada: ejecuta este archivo desde la terminal o IDE."""

import os

from transcriptor.app import Transcriptor  # noqa: E402

if __name__ == "__main__":
    Transcriptor().mainloop()