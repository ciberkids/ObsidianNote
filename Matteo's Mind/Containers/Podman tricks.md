## Quadlets (systemd containers)

In the quadlet the `--privileged` modifiers doesn't exists here two methods for replicating it

1)
 ```bash
Unmask=all  
SecurityLabelDisable=true  
AddCapability=all  
SeccompProfile=unconfined
```

2)    Or you can do
``` bash
PodmanArgs=--privileged
```