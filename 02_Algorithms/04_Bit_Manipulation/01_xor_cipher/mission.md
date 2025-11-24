# Mission : XOR Cipher pour Évasion d'AV

## Objectif
Implémenter un chiffreur XOR pour encoder des payloads et éviter la détection par signature antivirus.

## Contexte
Les antivirus utilisent des **signatures** (séquences de bytes) pour détecter les malwares. Si votre malware contient des strings suspectes comme `"cmd.exe"`, `"powershell"`, ou du shellcode connu, il sera bloqué instantanément.

La solution : **XOR Encryption**. On encode ces données avant de compiler le malware, puis on les décode au runtime.

## Votre Mission
Vous devez compléter `cipher.py` pour :
1. Encoder une string/bytes avec une clé XOR (single-byte ou multi-byte).
2. Décoder les données (même opération, grâce aux propriétés du XOR).
3. Tester avec des strings suspectes.

## Contraintes
- Utilisez l'opérateur `^` (XOR bitwise).
- Supportez les clés single-byte (ex: `0x42`) et multi-byte (ex: `b"SECRET"`).
- Le décodage doit utiliser la même fonction que l'encodage.

## Exemple
```python
message = b"cmd.exe"
key = 0x42

encrypted = xor_cipher(message, key)
print(encrypted.hex())  # "252f2604272d27"

decrypted = xor_cipher(encrypted, key)
print(decrypted)  # b"cmd.exe"
```

## Bonus (Avancé)
Implémentez un **Rolling XOR** où la clé change à chaque byte :
```python
# Byte 0 : XOR avec key
# Byte 1 : XOR avec key + 1
# Byte 2 : XOR avec key + 2
# etc.
```

## Lancement
1. Lancez `python3 cipher.py`.
2. Vérifiez que votre encodage/décodage fonctionne correctement.
