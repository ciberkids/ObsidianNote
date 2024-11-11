
1. install usb stick with arch linux
2. boot from usb 
	1. you can now also unplug it after boot
3. run `fdisk -l` to find partition with linux installation (ie /dev/sda3 Linux Filesystem)
4. mount partition: `mount /dev/sda3 /mnt`
	1. if the drive is encrypted read this [[Open Luks device]]
6. arch chroot into it: `arch-chroot /mnt`
7. (IF any) mount /boot partition otherwise the initramfs will be saved in the wrong `/boot`
8. rebuild initramfs: `mkinitcpio -p linux` (if that doesn't work yes try `pacman -S linux` only)
9. shutdown, unplug usb, reboot