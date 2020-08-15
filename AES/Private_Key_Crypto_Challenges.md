# Challenges with Private Key Cryptography

* Private key used for encryption and decryption; a private key must be exchanged between those communicating. This can possibly compromise the key and add enormous challenges to distributing the key between users.
* Every pair in the network must have a distinct private key for secure communication. If there are N users in a given network, where everyone can communicate with each other, there must be n(n-1) / 2 private keys!
* Not always straightforward to understand whether something was meant to be sent or recieved.