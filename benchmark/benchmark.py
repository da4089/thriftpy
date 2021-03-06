import time

import thriftpy
thriftpy.install_import_hook()

from thriftpy.utils import serialize, deserialize
from thriftpy.protocol import TBinaryProtocolFactory, TCyBinaryProtocolFactory

import addressbook_thrift as addressbook
# import addressbook


def make_addressbook():
    phone1 = addressbook.PhoneNumber()
    phone1.type = addressbook.PhoneType.MOBILE
    phone1.number = b'555-1212'
    phone2 = addressbook.PhoneNumber()
    phone2.type = addressbook.PhoneType.HOME
    phone2.number = b'555-1234'
    person = addressbook.Person()
    person.name = b"Alice"
    person.phones = [phone1, phone2]
    person.created_at = 1400000000

    ab = addressbook.AddressBook()
    ab.people = {person.name: person}
    return ab


def encode(n, proto_factory=TBinaryProtocolFactory()):
    for i in range(n):
        ab = make_addressbook()
        serialize(ab, proto_factory)


def decode(n, proto_factory=TBinaryProtocolFactory()):
    ab = make_addressbook()
    encoded = serialize(ab)
    for i in range(n):
        deserialize(ab, encoded, proto_factory)


def main():
    print("TBinaryProtocol:")

    start = time.time()
    encode(10000)
    end = time.time()
    print(end - start)

    start = time.time()
    decode(10000)
    end = time.time()
    print(end - start)

    print("\nTCyBinaryProtocol:")

    start = time.time()
    encode(10000, TCyBinaryProtocolFactory())
    end = time.time()
    print(end - start)

    start = time.time()
    decode(10000, TCyBinaryProtocolFactory())
    end = time.time()
    print(end - start)


if __name__ == "__main__":
    main()
