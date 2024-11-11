
path in home directory:
```
~/.config/containers/systemd
```

path in system
```
/etc/containers/systemd
```

the difference between the two path is that when using the home directory podman and systemd are in userspace 

the sock for podman are:

userspace: `/run/user/1000/podman/podman.sock`
system: `run/podman/podman.sock`



it is possible to create 

`.container` files for definition of container
`.volume` files for the definition of volumes
`.network` files for the definition of networks
