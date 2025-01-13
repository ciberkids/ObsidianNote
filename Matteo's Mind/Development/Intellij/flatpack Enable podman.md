# how to
## inside a gradle project write this

```groovy

test {  
  
    OperatingSystem os = DefaultNativePlatform.currentOperatingSystem;  
    if (os.isLinux()) {  
       println "We are under linux"  
       def uid = ["id", "-u"].execute().text.trim()  
       environment "DOCKER_HOST", "unix:///run/user/$uid/podman/podman.sock"  
    } else if (os.isMacOsX()) {  
       println "We are under MacOS"  
       environment "DOCKER_HOST", "unix:///tmp/podman.sock"  
    } else {  
       println "NO OS FOUND"  
    }  
  
    environment "TESTCONTAINERS_RYUK_DISABLED", "true"
```

## on the bash

```bash
sudo flatpak override --filesystem=/run/user/$UID/podman/podman.sock com.jetbrains.IntelliJ-IDEA-Ultimate
```