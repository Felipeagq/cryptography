# cryptography
```bash
pip install cryptography
```

# Metodo Fernet
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