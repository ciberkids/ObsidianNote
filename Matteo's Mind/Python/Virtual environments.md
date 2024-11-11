to create a virtual environment first you need a folder where to create the virtual environment:

```
/somewhere
```

the you run the command:

```
python -m venv venv
```

this will create a folder `venv` (second parameter is the folder name)

then you can enter the virtual environment with
```
source venv/bin/activate
```

the prompt will change to something like:

```
(venv) root@bumblebee:~/python_virtual_envs/nvidia-checks
```

that tells you you are in the virtual env

then you can run the normal pip install commands for the library you need

to exit the virtual env you type
```
deactivate
```

important to remember the "shebang" for the script has to change as well

```
#!/usr/bin/env python
```