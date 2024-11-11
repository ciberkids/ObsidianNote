If you have a dual graphic card like intel integrated (iGPU) e a discrete one nvidia (dGPU)

very often you have a hybrid situation.

what you want is to force one provider (potentially the iGPU) to be the engine for wayland and the discrete to be used on demand

normally this happen automatically but sometimes it breaks.

in order to fix it you can TRY to do the following

1) download and install this https://github.com/bayasdev/envycontrol
2) try to set up `-s integrate` -> reboot
3) try setup `-s hybrid` -> reboot
4) try to start wayland

it should work.


for starting an app with the dGPU use this in front of the `executable` you want to run:

```
__NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia __VK_LAYER_NV_optimus=NVIDIA_only
```

example:
```
__NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia __VK_LAYER_NV_optimus=NVIDIA_only glxinfo | egrep "OpenGL vendor|OpenGL renderer"
```
the executable in the example is `glxinfo` you can change it to `steam` for instance.

try with and without the "prefix" and you will see the renderer change from `intel` to `nvidia` 