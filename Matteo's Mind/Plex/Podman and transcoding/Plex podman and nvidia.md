
1) Install portainer.io
	   https://www.youtube.com/watch?v=FrMdyMJ9FaQ&t=182s
1) Follow this video if you want to use `portainer`
	   https://www.youtube.com/watch?v=Pv0oL2bSNDc


the command neede are:
```bash
--device nvidia.com/gpu=all --security-opt=label=disable
```

that in quadlets translated to:

```bash
AddDevice=nvidia.com/gpu=all
SecurityLabelDisable=true


```https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html