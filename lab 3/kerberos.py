from Crypto.Cipher import AES


class Client:
    def __init__(self):
        self.key_client_as = 'simsimpani001001' # client password

    def request_to_as(self):
        request = 'I need a TGT plz'.encode()
        Cipher = AES.new(self.key_client_as, AES.MODE_ECB)
        return Cipher.encrypt(request)


class AuthenticationServer:
    def __init__(self):
        self.key_client_as = 'simsimpani001001' #client password in AS database
        self.key_as_tgs = 'keyforgivingtgsx' # key shared by as and tgs
        self.Cipher1 = AES.new(self.key_client_as, AES.MODE_ECB)
        self.Cipher2 = AES.new(self.key_as_tgs, AES.MODE_ECB)

    def send_tgt(self, request):
        decrypted_request = self.Cipher1.decrypt(request)
        if decrypted_request == 'I need a TGT plz'.encode():
            tgt = 'Here is your tgt'.encode()
            return self.Cipher2.encrypt(tgt)
        else:
            return 'Sorry, Access denied'


class TicketGrantingServer:
    def __init__(self):
        self.key_as_tgs = 'keyforgivingtgsx' # key shared by as and tgs
        self.key_tgs_server = 'keyforgivingtokn' # key shared by tgs and server
        self.Cipher1 = AES.new(self.key_as_tgs, AES.MODE_ECB)
        self.Cipher2 = AES.new(self.key_tgs_server, AES.MODE_ECB)

    def send_token(self, tgt):
        decrypted_tgt = self.Cipher1.decrypt(tgt)
        if decrypted_tgt == 'Here is your tgt'.encode():
            token = 'Here is the tokn'.encode()
            return self.Cipher2.encrypt(token)
        else:
            return 'Sorry, Access denied'


class Server:
    def __init__(self):
        self.key_tgs_server = 'keyforgivingtokn' # key shared by tgs and server
        self.Cipher = AES.new(self.key_tgs_server, AES.MODE_ECB)

    def access(self, token):
        decrypted_token = self.Cipher.decrypt(token)
        if decrypted_token == 'Here is the tokn'.encode():
            return 'ACCESS GRANTED'
        else:
            return 'ACCESS DENIED'


if __name__ == '__main__':
    request = Client().request_to_as()
    print('Client request:', request)
    tgt = AuthenticationServer().send_tgt(request)
    print('Ticket Granting token:', tgt)
    token = TicketGrantingServer().send_token(tgt)
    print('Token:', token)
    access_status = Server().access(token)
    print(access_status)
