# cryptography
```bash
pip install cryptography
```

## Metodo Fernet
```python
>>>from cryptography.fernet import Fernet
>>>key = Fernet.generate_key()
>>>f = Fernet(key)
t>>>oken = f.encrypt(b"my deep dark secret")
>>>token
b'...'
>>>f.decrypt(token)
b'my deep dark secret'
```

## Metodo MultiFernet
```python
>>>from cryptography.fernet import Fernet, MultiFernet
>>>key1 = Fernet(Fernet.generate_key())
>>>key2 = Fernet(Fernet.generate_key())
>>>f = MultiFernet([key1, key2])
>>>token = f.encrypt(b"Secret message!")
>>>token
b'...'
>>>f.decrypt(token)
b'Secret message!'
```