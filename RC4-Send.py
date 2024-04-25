import random

def key_random_choice(choices, index):
    key_index = index % len(choices)
    return choices[key_index]
def initialize_state(key):
    """Initializes the state array for RC4 given a key."""
    key_length = len(key)
    S = list(range(256))
    j = 0

    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
        # print(key[i % key_length])
    return S
def PRGA(S, N):
    """Generates N bytes of keystream from the state array."""
    i = j = 0
    keystream = []

    for _ in range(N):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        keystream.append(K)

    return keystream
def rc4_encrypt(plaintext, key, index):
    """Encrypts a plaintext using RC4."""
    key = [int(c) for c in key]
    S = initialize_state(key)
    keystream = PRGA(S, 1)
    ciphertext = plaintext ^ keystream[0]
    return ciphertext, index

# Generate a list of 10 predefined keys
possible_keys = [111, 112, 113, 114, 115, 116, 117, 0, 98, 114]

# Get an index from user input
index = random.randint(0, 9)
# Select a "random" key from the list based on the index
selected_key = key_random_choice(possible_keys, index)
print(f"Selected Key: {selected_key}")

# Example usage with a single byte plaintext
plaintext = 52  # Example plaintext (a single byte for simplicity)
ciphertext, index = rc4_encrypt(plaintext, str(selected_key), index)
print(f"Ciphertext: {ciphertext}, index: {index}")
