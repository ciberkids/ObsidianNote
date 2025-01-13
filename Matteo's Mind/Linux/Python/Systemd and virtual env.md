
an example of a systemd service that can call a script in a virtual env is like following:

```ini
[Unit]
Description=My Python Script

[Service]
ExecStart=/root/python_virtual_envs/nvidia-checks/venv/bin/python /path/to/your/script.py

[Install]
WantedBy=multi-user.target
```
