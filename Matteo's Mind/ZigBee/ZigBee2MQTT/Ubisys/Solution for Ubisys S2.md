
To unbind the releay from the input the cluster are the 3 and 4, but it possible to do it via interfance in zigbee2mqtt

![[Pasted image 20240710003128.png]]
```
zigbee2mqtt/bridge/request/device/unbind

{"from": "Kitchen Table Remote/1", "to": "Kitchen Table Remote"}
```

```
zigbee2mqtt/bridge/request/device/bind

{
  "from": "Kitchen Table Remote/1", 
  "to": "Kitchen Table"
}

```

set toggle switch
```
zigbee2mqtt/Kitchen Table Remote/set

{
    "configure_device_setup": {
        "input_action_templates": [
            {
                "//_comment": "will automatically use inputs 0 and 1 and endpoint 2 (first outbound endpoint on a D1)",
                "type": "dimmer_single"
            },
             {
                "//_comment": "will automatically use inputs 0 and 1 and endpoint 2 (first outbound endpoint on a D1)",
                "type": "dimmer_single"
            }
        ]
    }
}


```


to set up the power on behaviour

```
zigbee2mqtt/Kitchen Table Remote/set
{"power_on_behavior_l1": "on"}

```



