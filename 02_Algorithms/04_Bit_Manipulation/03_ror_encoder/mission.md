# Mission : Implémentation de ROR13 Hash

## Objectif
Implémenter l'algorithme **ROR13** utilisé par Metasploit et de nombreux malwares pour cacher les appels à des APIs Windows sensibles.

## Contexte
Votre malware doit appeler des fonctions système (ex: `CreateProcessW`), mais vous ne voulez pas que ces noms apparaissent en clair dans le binaire (détection par signature).

Solution : **API Hashing**. Vous pré-calculez le hash des fonctions, puis au runtime, vous parcourez les exports de la DLL pour trouver la fonction par son hash.

## Votre Mission
Complétez `ror.py` pour :
1. Implémenter la rotation à droite (ROR).
2. Implémenter l'algorithme ROR13 Hash.
3. Calculer les hash de fonctions Windows courantes.
4. Vérifier avec les hash connus de Metasploit.

## Contraintes
- La rotation doit gérer le wraparound des bits.
- Le hash doit être sur **32 bits** (masque 0xFFFFFFFF).
- Les noms de fonctions sont convertis en **MAJUSCULES** avant le hash (insensible à la casse).

## Algorithme ROR (Rotate Right)
```
Pour ROR(valeur, 13) sur 32 bits :
  1. Décaler vers la droite de 13 bits : valeur >> 13
  2. Récupérer les 13 bits perdus et les mettre à gauche : valeur << (32 - 13)
  3. Combiner avec OR : (valeur >> 13) | (valeur << 19)
  4. Masquer à 32 bits : & 0xFFFFFFFF
```

## Hash Attendus (Metasploit)
```python
"CreateProcessW"     -> 0x16b3fe72
"VirtualAlloc"       -> 0x91afca54
"WriteProcessMemory" -> 0xd83d6aa1
"LoadLibraryA"       -> 0x0726774c
```

## Lancement
1. Lancez `python3 ror.py`.
2. Vérifiez que vos hash correspondent aux valeurs Metasploit.
