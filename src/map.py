class Map:
    data = []
    @staticmethod
    def parse(file_path: str):
        _map = Map()
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                _map.data.append([*line])
        return _map