import hashlib

# MD5("password") = 5f4dcc3b5aa765d61d8327deb882cf99
# 2^53 flops has the supercomputer

# MD5       411 Mb/s
# SHA-1     218 Mb/s
# SHA-256   118 Mb/s
# SHA-512    46 Mb/s
# In 2007, a chosen-prefix collision attack was found against MD5, requiring roughly 2^50 evaluations of the MD5 function
# In 2019, researchers found a chosen-prefix collision attack against SHA-1 with computing complexity between 2^66.9 
# and 269.4 and cost less than 100,000 US dollars. In 2020, researchers reduced the complexity of chosen-prefix collision
# attack against SHA-1 to 2^63.4
# SHA1 is broken in theory.  There's an attack that should produce two colliding files in about 261 SHA1 calls

var = b''
ret = hashlib.md5(var).hexdigest()
print("MD5   :" + ret)

ret = hashlib.sha1(var).hexdigest()
print("SHA1  :" + ret)

ret = hashlib.sha256(var).hexdigest()
print("SHA256:" + ret)

ret = hashlib.sha512(var).hexdigest()
print("SHA512:" + ret)