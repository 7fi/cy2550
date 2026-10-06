# Project 2

## 1.1
1.1.1 What -pbkdf2 does.\\
It is a way of generating a strong key and initialization vector using only the password supplied. It does this by salting and then hashing the password over and over until it generates a secure output.

1.1.2 Why encrypting with a passphrase requires it.\\
Because the passphrase could otherwise potentially be brute forced and are generally not good encryption keys. 

## 1.2
1.2.1 Why the checksums are different.\\
The checksums are different because each run has a different initialization vector randomly created. 

1.2.2 What would be wrong with an encryption scheme where the two encrypted files were identical.\\
This would be deterministic encryption and have all of the problems with ECB that we discussed in class including patterns leaking through, knowing two files have the same contents just from the checksums, replay attacks, plus they are vulerable to frequency analysis and other plaintext attacks. 

## 1.3
1.3.1 How many distinct blocks does each encryption produce, and how many times does the most common ECB block repeat?\\
3 blocks for ecb and the most common block repeats 24 times
37 blocks for .cbc

1.3.2 AES-256 is not broken and your passphrase was not weak. What exactly did ECB leak? To an attacker who never learns your key, what information is that worth?\\
It leaked the underlying pattern of the plaintext. The attacker can tell that there are large repeated blocks in the plaintext without decoding it at all. The information can be helpful to an attacker because it can allow frequency analysis, visual information can leak through from uncompressed images, and blocks can be manipulated or replayed by the attacker.

1.3.3 You are told a system encrypts database records with AES. What is one question you would ask before believing the records are protected?\\
Which cypher block mode was used and how is the IV generated? 

## 2.2
2.2.1 Why the SHA-256 hash does not protect your colleague.\\
SHA-256 does not require a key, and does not provide any authenticity or tamper protection for a file. An attacker could intercept and tamper with the file, and as long as they calculate a new valid hash and send the new file and new hash, the recipient will not know anything has happened. 

2.2.2 What changes when you use an HMAC instead.\\
HMAC requires a secret key so if you have the key and you can decrypt the message you can know that the file was not tampered with, and the person who encrypted it also has the same secret key.

2.2.3 What the attacker can and cannot do in each situation (SHA-256 and HMAC).\\
With SHA-256 the attacker can modify or replace the content of the message, and recompute a new hash. They cannot find a different file that produces the same hash as the original file. \\
With HMAC the attacker can potentially block the message from coming through with a DoS attack or perform a replay attack. They cannot modify the message without detection, or get the secret key from the message alone.

## 3.3
3.3.1 The keyserver would not publish your email address until you clicked a verification link sent by email. What does this check prove? What does it not prove?\\
It proves that the email is a valid email that can be used by someone. It does not prove that the someone validating the link is actually the person claiming to register the key.

3.3.2 You downloaded a public key claiming to belong to a classmate. The fingerprint is 40 hexadecimal characters. Describe a procedure for checking that the key really belongs to your classmate in a way that would defeat an attacker who controls the network between you. Explain why your procedure works.\\
One way is to have both of you generate a fingerprint and then meet up in person somewhere with no possibility of being overheard by an attacker. Then compare the fingerprints and if they match you know the key really belongs to them. 

## 4.2
4.2.1 What is contained in each packet?\\
the public enc packet contains the header key and a session key.\\
the encrypted data packet contains the rest of the bulk message

4.2.2 Why does GPG use this approach instead of encrypting the entire message with RSA?\\
The 4096 RSA key can only encrypt bytes smaller than 512 bytes so it can't do large messages. It is also faster this way and more performant. 

4.2.3 What is this construction called?\\
Hybrid Encryption

## 4.3
4.3.1 Which key is used for signing?\\
the sender's private key

4.3.2 Which key is used for verifying?\\
the senders public key

4.3.3 Which key is used for encryption?\\
In this specific case with the commands I used, the message isn't actually encrypted so none. However, in general it would use the recipient's public key. 

4.3.4 Which key is used for decryption?\\
Again, with the commands I used the message isn't encrypted so none. However, in general it would be the recipient's private key.

4.3.5 What is one security property provided by signing that encryption does not include?\\
authenticity and integrity. The recipient can confirm who signed it and that it was not modified. 

## 5.1
5.1.1 Your GPG key is RSA-4096, while your SSH key is Ed25519, which is roughly a 256-bit elliptic curve key. Explain in two sentences why the much smaller Ed25519 key is not necessarily the weaker key.\\
RSA is built on multiplication and prime numbers, which computers are getting much better at reversing, hence the need for large keys. However Ed25519 is built on geometry along a curved graph, which we don't have any shortcuts for brute forcing so it can be more secure while being smaller. 

## 7.1
7.1.1 Which AI assistant you used.\\
I used gemini flash-lite hoping that a "worse" model might produce code with more defects.

7.1.2 The exact prompt you used.\\
I used the same prompt that was given: "Write me a Python function that encrypts a file with AES.”

## 7.2
1. What is wrong?\\
It is assuming the key is a strong random key, but not enforcing it. 

2. What could an attacker do because of it?\\
An attacker who can guess or brute-force the password could decrypt the file. AES-256 itself would not protect the data if the key is weak.

3. Which lecture concept does the defect violate.\\
Secure key management

If you follow the example usage though, this isn't even an issue. And other than that, I would actually argue this implementation is pretty secure. If the attacker has access to the host machine, there are a few tricky things they could do by loading large files to run out of RAM, filling up the storage of the machine to corrupt the output, or manipulating the output path to override other files, but the actual implementation seems good to me. It handles the IV correctly, doesn't use ECB, and properly calls the encryption function.


## 7.3
I honestly don't think that the function requires any changes. I thought about it for a long time and tried to find any vulnerabilities but as long as you call it with a proper good key as the example usage defines, then it passes all of the security issues that I was looking for. I think this part was designed with older models in mind that would frequently generate less secure code such as the example on the lecture slides using a hard coded key and ECB. 
