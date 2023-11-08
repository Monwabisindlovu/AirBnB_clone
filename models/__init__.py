#!/usr/bin/python3
""" Generate and import a unique FileStorage. """


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
