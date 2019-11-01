# Diffie-Hellman key exchange

# https://docs.python.org/3.6/library/secrets.html#module-secrets
import secrets


def dh_keygen(p, g):
    """ Given prime p and generator g,
    generates a private_partial_key and the public_partial_key that is used to exchange in an insecure channel

    Keyword arguments:
        p, prime number of the finite field
        g, the generator of this finite field
    """
    private_partial_key = secrets.randbelow(p)
    public_partial_key = pow(g, private_partial_key) % p
    return [private_partial_key, public_partial_key]


def dh_cal_sharedkey(public_partial_key, private_partial_key, p):
    """ Given a received public_partial_key and a local secret private_partial_key, construct a shared key

    Keyword arguments:
        public_partial_key, partial_key that is received via insecure channel
        private_partial_key, partial_key that was constructed locally and kept secret
        p, prime number of the finite field
    """
    shared_key = pow(public_partial_key, private_partial_key) % p
    return shared_key


p = 23
g = 5

[alice_private_partial_key, alice_public_partial_key] = dh_keygen(p, g)
[bob_private_partial_key, bob_public_partial_key] = dh_keygen(p, g)
alice_constructed_shared_key = dh_cal_sharedkey(bob_public_partial_key, alice_private_partial_key, p)
bob_constructed_shared_key = dh_cal_sharedkey(alice_public_partial_key, bob_private_partial_key, p)

print("The public parameters (p, g): (" + str(p) + " ," + str(g) + ")")
print("Alice shared a partial key: " + str(alice_public_partial_key))
print("Bob shared a partial key: " + str(bob_public_partial_key))
print("Alice constructed a shared key: " + str(alice_constructed_shared_key))
print("Bob constructed a shared key: " + str(bob_constructed_shared_key))
