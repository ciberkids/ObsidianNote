# Podman 

When you use intellij with flatpak you need to add some command to the flatpak intallation like:

```bash
sudo flatpak override --filesystem=/run/user/$UID/podman/podman.sock com.jetbrains.IntelliJ-IDEA-Ultimate
```

this command will let the flatpak to see the `podman.sock`

then we need to tell gradle to craete an env variables called `DOCKER_HOST` that points to that path

```gradle
test {  
    OperatingSystem os = DefaultNativePlatform.currentOperatingSystem;  
    if (os.isLinux()) {  
       def uid = ["id", "-u"].execute().text.trim()  
       environment "DOCKER_HOST", "unix:///run/user/$uid/podman/podman.sock"  
    } else if (os.isMacOsX()) {  
       environment "DOCKER_HOST", "unix:///tmp/podman.sock"  
    }  
    environment "TESTCONTAINERS_RYUK_DISABLED", "true"  
}
```

add this to the `build.gradle` file
if it doesn't work you can test with this
```bash
DOCKER_HOST="unix:///run/user/$UID/podman/podman.sock" TESTCONTAINERS_RYUK_DISABLED="true" ./gradlew clean build -i
```

# Flatpak

when there are problem with flatpak and java then install the sdk in flatpak

```bash
flatpak install org.freedesktop.Sdk.Extension.openjdk21
```

you will asked with version:
```
Similar refs found for ‘org.freedesktop.Sdk.Extension.openjdk21’ in remote ‘flathub’ (system):  
  
  1) runtime/org.freedesktop.Sdk.Extension.openjdk21/x86_64/22.08  
  2) runtime/org.freedesktop.Sdk.Extension.openjdk21/x86_64/23.08  
  3) runtime/org.freedesktop.Sdk.Extension.openjdk21/x86_64/24.08  
  
Which do you want to use (0 to abort)? [0-3]:
```

i didn't understand how to match the right version with the version in intellij:
```
i found a way to understand which version intellij is using, install some of the version then start intellij then try to unistall the different version, flatpak will warn you that the version is in use in somehow
```

since intellij in flatpak has a version like:
```bash
flatpak info com.jetbrains.IntelliJ-IDEA-Ultimate    
  
IntelliJ IDEA Ultimate - Capable and Ergonomic Java IDE for Enterprise, Web and  
Mobile Development  
  
         ID: com.jetbrains.IntelliJ-IDEA-Ultimate  
        Ref: app/com.jetbrains.IntelliJ-IDEA-Ultimate/x86_64/stable  
       Arch: x86_64  
     Branch: stable  
    Version: 2024.2.4  
    License: LicenseRef-proprietary  
     Origin: flathub  
 Collection: org.flathub.Stable  
Installation: system  
  Installed: 14.2 MB  
    Runtime: org.freedesktop.Sdk/x86_64/24.08  
        Sdk: org.freedesktop.Sdk/x86_64/24.08  
  
     Commit: f5afb718fe0333ee5709e816158ee43278ac018a3439ae18e469aff60ae6cf8b  
     Parent: 076b151b4f9ec3d3c224c296f9663518fb4c1d76c2ed49aa700112be8b78c33b  
    Subject: Update IntelliJ IDEA to version 2024.2.4 (edd6e3c5)  
       Date: 2024-10-23 15:10:21 +0000
       ```
so i installed the  `24.08` and it didn't work, i installed the `22.08` and it worked.

In Intellij i added a sdk using a disk installation and the installation path (inside flatpak) is

```bash
/usr/lib/sdk/openjdk21/jvm/openjdk-21
```

### Gradle 

for getting gradle to work we need to set up 2 things
1) gradle from the command line
2) gradle in intellij

#### Gradle command line (inside intellij)

first and foremost export the right `JAVA_HOME` so in the intellij terminal run this
```bash
export JAVA_HOME=/usr/lib/sdk/openjdk21
```


#### Gradle inside intellij

we need to configure gradle inside intellij. in order to do so we need to do the following setting inside the `file->settings->Build Execution and tool-> Build tools->gradle`
![[Pasted image 20241107141140.png]]

in addition we need to add the right sdk to the project
so right click on the project `open module settings`

![[Pasted image 20241107141323.png]]

Attention the JDK home is slightly different
```bash
/usr/lib/sdk/openjdk21/jvm/openjdk-21
```

if you have problem with gradle
remember the matrix

https://docs.gradle.org/8.8-rc-1/userguide/compatibility.html
![[Pasted image 20241107133414.png]]



