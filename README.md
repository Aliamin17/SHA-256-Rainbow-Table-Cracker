The main aim of this project is to establish a python code that creates a rainbow table for the password that
has been hashed using a one-way funcƟon (SHA256). The code generates passwords consisƟng of a
lower cases and upper cases and special characters, which are then taken to be hashed using SHA256. In
that case a rainbow table is generated so to be able recover the original password for a given set of
SHA256 hashes. One-way hash methods like SHA256 have grown in popularity as a password security
method in recent years. AƩackers can, however, uƟlize a number of methods to decode the hashed
password and recover the original plaintext password in the event of a data breach. One of his methods
is the use of rainbow tables. EssenƟally, this is a table of pre-generated hashes and the accompanying
passwords.
The applicaƟon we present aims to construct a rainbow table of passwords for SHA256
hashes by generaƟng and hashing a large number of passwords. The soŌware generates passwords
consisƟng of lower and upper-case alphabets and special characters to increase the complexity and
security of the passwords. The efficiency of the algorithm used in this applicaƟon is calculated based on
the data structure used to store the precomputed table, and the Ɵme required to generate the table.
