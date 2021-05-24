from models.engine.file_storage import FileStorage

# storage is an instance of filestorage
storage = FileStorage()

# storage reloads the json file at program init
storage.reload()
