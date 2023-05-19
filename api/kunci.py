import blowfish,base64, json, binascii
from struct import pack

class Kunci:
    def __init__(self) -> None:
        self.kunci = "3ncRypt3dFr4m3w0rk0p3r4t10n022!@"
        
    def unpad(self, data):
        last_byte = data[-1]
        data = data[: -(last_byte if type(last_byte) is int else ord(last_byte))]
        return data
    
    def pad(self, data):
        bs = 8
        plen = bs - len(data) % bs
        padding = [plen] * plen
        padding = pack("b" * plen, *padding)
        return data + padding

    def encrypt(self, data) -> bytes:
        data = bytes(data,'ascii')
        secret = bytes(self.kunci, "ascii")
        data = self.pad(data)
        cipher = blowfish.Cipher(secret)
        data_encrypted = b"".join(cipher.encrypt_ecb((data)))
        return base64.b64encode(data_encrypted)
    
    def decrypt(self, data) -> dict:
        data = binascii.hexlify(base64.b64decode(data))
        secret = bytes(self.kunci, "ascii")
        cipher = blowfish.Cipher(secret)
        data_decrypted = b"".join(cipher.decrypt_ecb(binascii.unhexlify(data)))
        data_unpad = self.unpad(data_decrypted)
        data_decode = data_unpad.decode('ascii')
        # data_json = data_unpad.decode("utf-8").replace("'", '"')
        return json.loads(data_unpad.decode('unicode_escape'))