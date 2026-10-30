# turns a URL (text) into numbers the model can use
import re
from urllib.parse import urlparse

words = ["login", "verify", "secure", "account", "update", "bank", "confirm", "password"]
columns = ["length", "dots", "hyphens", "subdomains", "has_ip", "has_at",
           "https", "digits", "bad_words"]


def get_features(url):
    p = urlparse(url if "://" in url else "http://" + url)
    host = p.hostname or ""
    is_ip = bool(re.match(r"^\d+\.\d+\.\d+\.\d+$", host))
    return [
        len(url),
        url.count("."),
        url.count("-"),
        0 if is_ip else max(0, len(host.split(".")) - 2),
        int(is_ip),
        int("@" in url),
        int(p.scheme == "https"),
        sum(c.isdigit() for c in url),
        sum(w in url.lower() for w in words),
    ]
