
this set up the C4 input 1 and 2 to use push button and in dimmer single configuration
1) every press is a toggle
2) long press change in brighness

```
zigbee2mqtt/Living Room Remote/set

{
    "configure_device_setup": {
        "input_action_templates": [
            {
                "//_comment": "will automatically use input 0 and endpoint 1",
                "type": "dimmer_single",
                "no_onoff_down":1
                
            },
            {
                "//_comment": "will automatically use input 1 and endpoint 2",
                "type": "dimmer_single",
                "no_onoff_down":1

            }
    ]
  }
}```