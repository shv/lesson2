from threading import Lock

class validationException(Exception):
    def __init__(self, code):
        pass
    pass

class URLConverter():
    database_dict = dict()
    domain_prefix = "http://short.com"
    insert_lock = Lock()
    def __init(self):
        self.insert_lock = Lock()

    def validateUrl(self, url) -> bool:
        return True

    def validateKeyword(self, keyword) -> bool:
        return True
        # raise validationException()

    def addUrl(self, source_url, keyword) -> str:
        if self.validateUrl(source_url) and self.validateKeyword(keyword):
            new_url = f"{self.domain_prefix}/{keyword}"
            with self.insert_lock:
                if new_url in self.database_dict:
                    raise validationException()
                self.database_dict[new_url] = source_url
            return new_url
        raise validationException()

    def getUrl(self, short_url) -> str:
        return self.database_dict.get(short_url, "")
