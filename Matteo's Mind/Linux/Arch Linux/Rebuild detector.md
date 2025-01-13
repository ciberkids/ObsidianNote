
# Site
https://github.com/maximbaz/rebuild-detector

# Description
it detect in arch when a packaged has been build to a older version of the executable, E.g. Python


# Useful command

```bash
$ checkrebuild | awk '{print $2}' | xargs -r paru -S --rebuild
```