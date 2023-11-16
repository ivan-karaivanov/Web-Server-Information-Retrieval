import requests


def fetch():
    with open("recon.txt", "r") as urls:
        for url in urls:
            url = url.strip()
            print("Footprint report for " + url + " Web Server:")
            req = requests.get(url)
            result = dict(req.headers)
            for item, value in result.items():
                print(item + " : " + value + "\n")


# Call the function
fetch()
