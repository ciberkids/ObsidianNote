
**Pre-requisites:**
1) Both users must have at least 1 user group in common


## Main user execute
```bash
$  tmux -S <path_to_a_location_socket> new -s <session_name>
```

#### In my case:

```bash
 tmux -S /tmp/stefano new -s stefano_session
```

### In addition once it is started:

```bash

$ chgrp <common_usergroup> <path_to_a_location_socket> 
$ chmod g+rwx <path_to_a_location_socket> 
$ tmux server-access -a  <user to give access to>
```

#### In my case

```bash
chgrp wheel /tmp/stefano ;
```

```bash
chmod g+rwx /tmp/stefano ;
```

```bash
tmux server-access -a stefano ;
```
## Secondary user run:

```bash
$ tmux -S  <path_to_a_location_socket> -t <session_name>
```

#### In my case

```bash
tmux -S /tmp/stefano -t stefano_session
```

