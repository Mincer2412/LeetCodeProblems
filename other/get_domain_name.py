def domain_name(url):
    # return url.replace('www.', '').replace('http://', '').replace('https://', '').split('.')[0]
    return url.split("://")[-1].split(".")[-2]


print(domain_name("http://google.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("www.xakep.ru"))
print(domain_name("https://youtube.com"))
