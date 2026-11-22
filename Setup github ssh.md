## 1. Generate new and add to github account 
```bash
ssh-keygen
cd .ssh
cat id_ed25519.pub
```
Copy the public key to github ssh 

## 2. Copy existing keys onto instance 
```bash
ssh-keygen
cd .ssh
```
Replace contents of id_ed25519 and id_25519.pub with your working setups

## Test SSH 
```bash
ssh -T git@github.com
```

