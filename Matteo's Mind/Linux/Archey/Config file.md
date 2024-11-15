ref: https://github.com/HorlogeSkynet/archey4?tab=readme-ov-file
```json
{  
       "allow_overriding": true,  
       "parallel_loading": true,  
       "suppress_warnings": false,  
       "entries_color": "",  
       "honor_ansi_color": true,  
       "logo_style": "",  
       "entries_icon": false,  
       "entries": [  
               { "type": "User" },  
               { "type": "Hostname" },  
               { "type": "Model" },  
               { "type": "Distro" },  
               {  
                       "type": "Kernel",  
                       "check_version": false  
               },  
               { "type": "Uptime" },  
               {  
                       "type": "LoadAverage",  
                       "decimal_places": 2,  
                       "warning_threshold": 1.0,  
                       "danger_threshold": 2.0  
               },  
               { "type": "Processes" },  
               { "type": "WindowManager" },  
               { "type": "DesktopEnvironment" },  
               { "type": "Shell" },  
               {  
                       "type": "Terminal",  
                       "use_unicode": true  
               },  
               {  
                       "type": "Packages",  
                       "combine_total": false,  
                       "one_line": true,  
                       "show_zeros": false  
               },  
               {  
                       "type": "Temperature",  
                       "char_before_unit": " ",  
                       "sensors_chipsets": [],  
                       "sensors_excluded_subfeatures": [],  
                       "use_fahrenheit": false  
               },  
               {  
                       "type": "CPU",  
                       "one_line": false,  
                       "show_cores": true  
               },  
               {  
                       "type": "GPU",  
                       "one_line": false,  
                       "max_count": 2  
               },  
               {  
                       "type": "Custom",  
                       "name": "Podman GPU",  
                       "icon": "\ue735",  
                       "shell": true,  
                       "command": "podman run --rm --device nvidia.com/gpu=all --security-opt=label=disable ubuntu nvidia-smi -L",  
                       "check": true,  
                       "log_stderr": true,  
                       "one_line": true  
               },  
               {  
                       "type": "RAM",  
                       "warning_use_percent": 33.3,  
                       "danger_use_percent": 66.7  
               },  
               {  
                       "type": "Disk",  
                       "show_filesystems": ["local"],  
                       "combine_total": true,  
                       "disk_labels": null,  
                       "hide_entry_name": null,  
                       "warning_use_percent": 50,  
                       "danger_use_percent": 75  
               },  
               {  
                       "type": "LAN_IP",  
                       "one_line": true,  
                       "max_count": 2,  
                       "show_global": false,  
                       "show_link_local": true,  
                       "ipv6_support": true  
               },  
               {  
                       "type": "WAN_IP",  
                       "one_line": true,  
                       "ipv4": {  
                               "dns_query": "myip.opendns.com",  
                               "dns_resolver": "resolver1.opendns.com",  
                               "dns_timeout": 1,  
                               "http_url": "https://v4.ident.me/",  
                               "http_timeout": 1  
                       },  
                       "ipv6": {  
                               "dns_query": "myip.opendns.com",  
                               "dns_resolver": "resolver1.opendns.com",  
                               "dns_timeout": 1,  
                               "http_url": "https://v6.ident.me/",  
                               "http_timeout": 1  
                       }  
               }  
  
       ],  
       "default_strings": {  
               "latest": "latest",  
               "available": "available",  
               "no_address": "No Address",  
               "not_detected": "Not detected",  
               "virtual_environment": "Virtual Environment"  
       }  
}
```

Also look for neofetch it seems more used