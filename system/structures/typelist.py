class my_list:
    def __init__(self, object: any) -> None:
        self.list = list()
        self.type = object
    
    def fill_list(self, array: list) -> None:
        if 'from_json' in dir(self.type):
            for obj in array:
                value = self.type(); value.from_json(obj)
                self.list.append(value)
        else:
            self.list = array    