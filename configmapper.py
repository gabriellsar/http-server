import os

class ConfigMapper:
    def __init__(self, path):
        with open("map.txt") as f:
            self.file_config = f.read()
        self._getFile(path)

        if os.path.exists(self.fis_path): 
            self.status = 200
        else:
            self.status = 404

    def _getFile(self, path):
        print(path)

        pairs = self.file_config.strip().split('\n')
        dfile_config = dict(item.split(' -> ') for item in pairs)

        sorted_keys = sorted(dfile_config.keys(), key=len, reverse=True)

        self.fis_path = path
        for key in sorted_keys:
            if path.startswith(key):
                self.fis_path = path.replace(key, dfile_config[key], 1)
                break

        print(f"fis -> {self.fis_path}")


