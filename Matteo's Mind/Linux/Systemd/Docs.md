https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html

`Type=`[](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html#Type= "Permalink to this term")

Configures the mechanism via which the service notifies the manager that the service start-up has finished. One of `simple`, `exec`, `forking`, `oneshot`, `dbus`, `notify`, `notify-reload`, or `idle`



`RemainAfterExit=`[](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html#RemainAfterExit= "Permalink to this term")

Takes a boolean value that specifies whether the service shall be considered active even when all its processes exited. Defaults to `no`.


`ExecStartPre=`, `ExecStartPost=`[](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html#ExecStartPre= "Permalink to this term")

Additional commands that are executed before or after the command in `ExecStart=`, respectively. Syntax is the same as for `ExecStart=`. Multiple command lines are allowed, regardless of the service type (i.e. `Type=`), and the commands are executed one after the other, serially.

If any of those commands (not prefixed with "`-`") fail, the rest are not executed and the unit is considered failed.

`ExecStart=` commands are only run after all `ExecStartPre=` commands that were not prefixed with a "`-`" exit successfully.

`ExecStartPost=` commands are only run after the commands specified in `ExecStart=` have been invoked successfully, as determined by `Type=` (i.e. the process has been started for `Type=simple` or `Type=idle`, the last `ExecStart=` process exited successfully for `Type=oneshot`, the initial process exited successfully for `Type=forking`, "`READY=1`" is sent for `Type=notify`/`Type=notify-reload`, or the `BusName=` has been taken for `Type=dbus`).

Note that `ExecStartPre=` may not be used to start long-running processes. All processes forked off by processes invoked via `ExecStartPre=` will be killed before the next service process is run.

Note that if any of the commands specified in `ExecStartPre=`, `ExecStart=`, or `ExecStartPost=` fail (and are not prefixed with "`-`", see above) or time out before the service is fully up, execution continues with commands specified in `ExecStopPost=`, the commands in `ExecStop=` are skipped.

Note that the execution of `ExecStartPost=` is taken into account for the purpose of `Before=`/`After=` ordering constraints.