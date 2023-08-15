import hashlib

class URLShortener:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}

    def shorten_url(self, url):
        # Generate a hash of the URL
        hash_object = hashlib.md5(url.encode())
        hash_hex = hash_object.hexdigest()

        # Take the first 8 characters of the hash as the short code
        short_code = hash_hex[:8]

        # Store the mapping
        self.url_to_code[url] = short_code
        self.code_to_url[short_code] = url

        return short_code

    def expand_url(self, short_code):
        return self.code_to_url.get(short_code, "Short code not found")

# Example usage
url_shortener = URLShortener()

original_url = "https://www.example.com/very_long_url_that_needs_shortening"
short_code = url_shortener.shorten_url(original_url)
print("Shortened URL:", short_code)

expanded_url = url_shortener.expand_url(short_code)
print("Expanded URL:", expanded_url)
