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
        pairs = self.file_config.strip().split('\n')
        dfile_config = dict(item.split(' -> ') for item in pairs)

        self.fis_path = self._multipleReplace(path,dfile_config)

    def _multipleReplace(self, path, dfile_config):
        for old, new in dfile_config.items():
            path = path.replace(old,new)
        return path



