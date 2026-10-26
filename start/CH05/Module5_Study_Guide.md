# Module 5 Study Guide: Cryptography

**Module 5 Quiz:** 10 questions, 10 pts, no time limit, unlimited attempts.
**Due:** Sun Oct 25, 11:59 PM.

Based on the Module 4 quiz, expect True/False questions plus "what does this expression evaluate to?" questions.

---

## 1. Characters are numbers (ASCII)

| Range | Characters |
|---|---|
| 0–31 | invisible control characters (tab = 9, newline = 10) |
| 32 | space |
| 48–57 | `'0'`–`'9'` (the **character** `'0'` is 48, not 0) |
| 65–90 | `'A'`–`'Z'` |
| 97–122 | `'a'`–`'z'` |

- Uppercase and lowercase letters are exactly **32 apart**: `ord('a') - ord('A') == 32`.
- ASCII covers 0–127. Python actually uses **Unicode**, and its first 128 values are the same as ASCII.

| Expression | Result | Why |
|---|---|---|
| `ord('a')` | `97` | character → number |
| `chr(97)` | `'a'` | number → character |
| `chr(ord('a') + 1)` | `'b'` | shifting is just math |
| `ord('ab')` | **TypeError** | `ord()` takes exactly one character |
| `chr(ord('z') + 13)` | `'\x87'` (not a letter!) | this is why ROT13 needs the `- 26` wrap |

## 2. ROT13 (a Caesar cipher with shift 13)

- Each letter moves forward 13 places: `a→n`, `n→a`, `hello → uryyb`.
- 13 + 13 = 26, so **running it twice gives back the original**. The same function encrypts and decrypts.
- It has **no key**, so anyone who knows the method can reverse it. There are only 25 possible shifts, so it falls to brute force or frequency analysis instantly.
- It's **obfuscation, not encryption**.
- In `Rot13.py`: `.lower()` first, then `ord()`, check the 97–122 range, add 13, wrap if over 122, then `chr()`. Non-letters pass through unchanged.

## 3. Encoding is not encryption

| | Has a key? | Purpose | Example |
|---|---|---|---|
| **Encoding** (Base64, ASCII, UTF-8) | No | change the *format* so data can be stored or sent | `base64.b64encode(b"Hello")` → `SGVsbG8=` |
| **Obfuscation** (ROT13) | No | hide from a casual glance | `uryyb` |
| **Encryption** (Fernet/AES) | **Yes** | keep data *secret* | `gAAAAABq...` |
| **Hashing** (SHA-256, MD5) | No | one-way fingerprint; can't be reversed | coming up in CH06 (passwords) |

Base64 output often ends in `=` or `==` padding. Anyone can decode it.

## 4. `str` vs `bytes`: `.encode()` and `.decode()`

```python
text = "Hello"           # str
data = text.encode()     # b'Hello'  -> bytes (UTF-8 by default)
back = data.decode()     # 'Hello'   -> str again
type(data)               # <class 'bytes'>
```

- The `b` prefix means **bytes**.
- Crypto libraries work on bytes. `Fernet(key).encrypt("text")` gives **`TypeError: data must be bytes`**.
- `.encode()` goes str → bytes, **before** encrypting.
- `.decode()` goes bytes → str, **after** encrypting or decrypting, so the result prints cleanly.

## 5. Modules, libraries, pip

- `import base64` imports the whole module, which you then use as `base64.b64encode(...)`.
- `from cryptography.fernet import Fernet` imports one name, which you then use as `Fernet(...)`.
- **PyPI** (pypi.org) is the public repository of Python packages. **pip / pip3** installs them: `pip3 install cryptography`.
- If a package is missing, the import fails with `ModuleNotFoundError`.
- `ord`, `chr`, `len`, and `print` are **built-ins**, so they need no import.

## 6. Fernet: symmetric encryption

- **Symmetric** means the **same key** encrypts and decrypts. **Asymmetric** uses a public/private key pair (RSA, for example).
- `Fernet.generate_key()` returns 32 random bytes, shown as 44 base64 characters ending in `=`.
- Under the hood, Fernet uses **AES-128** for secrecy and **HMAC-SHA256** to detect tampering.
- A token always starts with **`gAAAAA`**.
- Encrypting the same message twice gives **different** tokens, because Fernet adds a random IV and a timestamp.
- A wrong key or a tampered token raises **`InvalidToken`**, not garbage text.
- Lose the key and the data is **gone**: there's no recovery.

## 7. The big principle: don't roll your own crypto

- **Kerckhoffs's principle:** a system should stay secure even if everything about it *except the key* is public.
- Public algorithms (AES) have been attacked by experts for decades and survived. A homemade scheme has been tested by one person.
- "What is hard for you could be easy for someone else." Use vetted libraries.

## 8. Strings review (you missed one of these on the Module 4 quiz)

```text
 N  o     w  a  y  !
 0  1  2  3  4  5  6     <- index
-7 -6 -5 -4 -3 -2 -1     <- negative index
```

| Expression | Result |
|---|---|
| `text[3:6]` | `'way'`: the stop index (6) is **not included** |
| `text[3:]` | `'way!'` |
| `text[-1]` | `'!'` |
| `len(text)` | `7` |
| `text[::-1]` | `'!yaw oN'` (reverses the string) |

Strings are **immutable**. `final_message = final_message + c` builds a *new* string every time.

---

## Self-test (answers below)

1. T/F: Base64 is a form of encryption.
2. `chr(65)` evaluates to ____.
3. T/F: ROT13 applied twice returns the original text.
4. What does `"abc".encode()` return?
5. T/F: Fernet is asymmetric encryption.
6. Which raises an error: `ord("A")`, `ord("AB")`, or `chr(66)`?
7. What happens if you decrypt a Fernet token with the wrong key?
8. T/F: In a well-designed cryptosystem, the algorithm should be secret.
9. `ord('a') - ord('A')` = ____.
10. What command installs the cryptography library?

<details><summary>Answers</summary>

1. **False.** It's an encoding: no key, and anyone can reverse it.
2. `'A'`
3. **True.** 13 + 13 = 26.
4. `b'abc'` (bytes)
5. **False.** It's symmetric: one shared key.
6. `ord("AB")`
7. It raises `cryptography.fernet.InvalidToken`.
8. **False.** Only the **key** should be secret (Kerckhoffs's principle).
9. `32`
10. `pip3 install cryptography`

</details>

---

## Reflection talking points (Code Review, Part 4: write these in your own words)

**Q21: ROT13 vs Fernet.** Think about:
- whether each one has a key
- how many guesses it would take to break each one
- whether the same operation encrypts and decrypts
- what happens with a wrong key: `InvalidToken` vs. "just run it again"
- whether encrypting the same message twice gives the same output
- tamper detection (HMAC)

**Q22: Why not roll your own?** Think about:
- Kerckhoffs's principle
- public algorithms that have been tested by many experts vs. untested homemade ones
- subtle bugs you can't see yourself
- ROT13 *feels* scrambled but breaks instantly

**Q23: Most surprising thing.** Pick what actually stood out to you. Some candidates:
- letters are just numbers
- Fernet giving a different token every time
- how few lines real encryption takes compared with ROT13
- Base64 *looking* encrypted but not being encrypted
