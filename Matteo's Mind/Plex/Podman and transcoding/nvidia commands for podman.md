When the kernel is updated most likely you need to do this.

this generates the definition for podman
```bash
sudo nvidia-ctk cdi generate --output=/etc/cdi/nvidia.yaml
```
this test if the graphic card is avaiable in the container
```bash
podman run --rm --device nvidia.com/gpu=all --security-opt=label=disable ubuntu nvidia-smi -L

```