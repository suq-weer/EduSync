import config
from client.network import Network


if __name__ == '__main__':
    i = config.General()
    i.input_password_book(Network("get_info_software_codeBook.php"))
    print(i.password_book)
