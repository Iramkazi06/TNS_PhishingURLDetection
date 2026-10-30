# makes practice URLs so we don't need to download a dataset
import random
import pandas as pd


def make_data(n=1000):
    random.seed(42)
    brands = ["paypal", "google", "amazon", "apple", "netflix", "facebook", "sbi"]
    sites = ["wikipedia", "github", "python", "bbc", "reddit", "linkedin", "nasa"]
    paths = ["", "about", "news/article-12", "search?q=cats", "login", "account/settings"]
    bad_paths = ["login", "verify/account", "signin.php", "confirm-password", "update?id=4821"]
    tlds = ["xyz", "top", "ru", "tk", "click"]
    data = []
    for i in range(n):
        # safe url
        site = random.choice(sites + brands)
        if random.random() < 0.1:
            site = site + "-news"
        scheme = random.choice(["https", "https", "https", "http"])
        data.append([f"{scheme}://www.{site}.com/{random.choice(paths)}", 0])

        # phishing url
        brand = random.choice(brands)
        kind = random.choice(["ip", "hyphen", "subdomain", "at", "plain"])
        tld = random.choice(tlds)
        path = random.choice(bad_paths)
        if kind == "ip":
            host = ".".join(str(random.randint(1, 254)) for j in range(4))
        elif kind == "hyphen":
            host = f"secure-{brand}-login.{tld}"
        elif kind == "subdomain":
            host = f"{brand}.com.account-verify.{tld}"
        elif kind == "at":
            host = f"{brand}.com@free-host{random.randint(1, 99)}.{tld}"
        else:
            # looks almost normal
            host = f"www.{brand}-help.com"
            path = random.choice(paths)
        scheme = random.choice(["http", "https"])
        data.append([f"{scheme}://{host}/{path}", 1])

    return pd.DataFrame(data, columns=["url", "label"])
