# Git stuff

## Merge master to branch
```
git checkout dmgr2      # gets you "on branch dmgr2"
git fetch origin        # gets you up to date with origin
git merge origin/master
```

## Certificate auth with exlipse

- In your Eclipse go to `Window > Preferences > General > Network Connections > SSH2` (or just type "SSH2" in preferences window filter box).

- In "Key Management" tab press "Generate RSA Key..." button. Optionally you can add comment (usually e-mail address) and passphrase to your key. 
    - Do not use a passphrase
    - passphrase may not work

- Copy your generated public key (in a box just below "Generate RSA Key..." button) and add it to your GitHub account.
- Press "Save Private Key..." button to save your private RSA key into file. By default keys are stored in SSH2 home directory (see "General" tab) - probably `~/.ssh`
    - name the key anything you want - `id_rsa_e`
    - This will save files `id_rsa_e` and `id_rsa_e.pub` to `~/.ssh`
- That's it! Now you should be able to push your code to GitHub repo.