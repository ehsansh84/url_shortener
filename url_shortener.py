class URLShortener:
    def __init__(self):
        self.url_mapping = {}
        self.counter = 0

    def shorten_url(self, url):
        if not self.is_valid_url(url):
            return None

        if url in self.url_mapping:
            return self.url_mapping[url]

        short_url = f"http://shrt.ir/{self.counter}"
        self.url_mapping[url] = short_url
        self.url_mapping[short_url] = url
        self.counter += 1
        return short_url

    def expand_short_url(self, short_url):
        return self.url_mapping.get(short_url, None)

    def is_valid_url(self, url):
        # Basic URL validation (you can customize this as needed)
        return url.startswith("http://") or url.startswith("https://")

