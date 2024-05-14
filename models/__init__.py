#!/usr/bin/python3
import sys
sys.path.append('..')

from engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
