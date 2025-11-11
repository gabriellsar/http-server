class HttpRequest():
    def __init__(self, data):
        self._sliptData(data)

    def _sliptData(self, dat):
        nl_index = dat.find('\n')

        ldat = dat[:nl_index].split()
        self.method = ldat[0]
        self.path = ldat[1]
        self.version = ldat[2]
