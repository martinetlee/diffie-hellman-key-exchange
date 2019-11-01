# Diffie-Hellman Key Exchange

This is a basic implementation of the Diffie-Hellman Key Exchange protocol, 

each party has two functions: `dh_keygen` to generate partial key pairs, and `dh_cal_sharedkey` to calculate the shared key with private partial key and the received public partial key. 

Currently the power in the finite field is calculated simply with the python `pow` function and `%` operator. Fast power algorithm should be used when using larger inputs.

The program will output something like below to show that two parties have indeed successfully agreed on a shared key with the algorithm:

```
The public parameters (p, g): (23 ,5)
Alice shared a partial key: 3
Bob shared a partial key: 4
Alice constructed a shared key: 12
Bob constructed a shared key: 12
```
