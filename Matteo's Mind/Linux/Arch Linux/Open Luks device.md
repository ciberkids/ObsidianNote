```
cryptsetup open /dev/sda2/ crypthome
```

```
mkdir /mnt/crypthome && mount /dev/mapper/crypthome /mnt/crypthome
```