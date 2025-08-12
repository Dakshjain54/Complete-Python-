import multiprocessing
import requests

def downlodeFile(url, name):
    print(f"start downloading {name}")
    responce = requests.get(url)
    open(f"28.2.MP files/file{name}.jpg", "wb").write(responce.content)
    print(f"finished downloading {name}")

if __name__ == "__main__":
    url = "https://picsum.photos/200/300"

    pros = []
    for i in range(5):
        # downlodeFile(url, i)
        p = multiprocessing.Process(target=downlodeFile, args=[url, i])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()