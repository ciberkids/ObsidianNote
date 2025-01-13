
# How to load dynamic Environment variables

If you are writing a quadlet for systemd and you neet to pass inside the container a Environment variable with information that can be read only a runtime then the easiest way is to use the 


> [!NOTE] Systemd
> ExecStartPre=

> 
```bash
[Service]  
ExecStartPre=podman login --authfile /root/.config/containers/auth.json registry.gitlab.com  

ExecStartPre=/bin/bash -c "/bin/systemctl set-environment HOST_IP=$(hostname -I | awk '{print $1}')"  

ExecStartPre=/bin/bash -c "/bin/systemctl set-environment DATAPRODUCT_ID=1"
```

In the `[Container]` section then you can use this:

```
[Container]  
ContainerName=SendDataContract  
  
Environment=DMM_ADDRESS=""  
Environment=DMM_CLIENT_API_KEY=""  
Environment=DATAPRODUCT_ID=${DATAPRODUCT_ID}  
Environment=HOST_IP=${HOST_IP}
```