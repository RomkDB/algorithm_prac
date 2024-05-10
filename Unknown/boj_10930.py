# 백준 10930번 SHA-256
import hashlib

s = input()
encode_s = s.encode()
answer = hashlib.sha256(encode_s).hexdigest()

print(answer)