import config
from client.network import Network, NetworkResource

if __name__ == '__main__':
    i = config.General()
    i.input_password_book(Network(NetworkResource.GET_INFO_SOFTWARE_CODEBOOK))
    print(i.password_book)
