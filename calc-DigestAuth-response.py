import hashlib

username = "hoge"
realm = "digest"
http_method = "GET"
uri = "hoge/hoge"
nonce = "hogehogehoghoehoge"
cnonce = "hogehoge"
nc = "hoge_number"
qop = "auth"
a1_md5 = "hogehoge"
a2 = http_method + ":" + uri

a2_md5 = hashlib.md5(a2.encode('utf-8')).hexdigest()
response = hashlib.md5(
    ":".join([a1_md5, nonce, nc, cnonce, qop, a2_md5]).encode('utf-8')).hexdigest()
print(response)
