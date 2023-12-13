from Crypto.Hash import keccak


keccak_hash = keccak.new(digest_bits=256)

keccak_hash.update(b'matin')

print (keccak_hash.hexdigest())