### Module not found after Python version update

A Python-based application might output `No module named _module_name_` for an installed dependency named `_module_name_` after having upgraded the [python](https://archlinux.org/packages/?name=python) package to a new minor version (e.g. from version 3.10 to 3.11).

The above scenario happens when a dependency is not available for that Python version or not installed at all. Python packages are installed in a versioned site-packages directory (`/usr/lib/python_X.Y_/site-packages` if system-wide, or `~/.local/lib/python_X.Y_/site-packages/` if per-user, where `_X.Y_` is a version like "3.11"). So whenever there is a new minor version upgrade, the Python-based package built with previous Python version must be rebuilt against the new one in order to be properly used.

Please notice it is the user's responsibility to rebuild non-official packages, including Python-based packages installed from AUR. See [AUR#Updating packages](https://wiki.archlinux.org/title/AUR#Updating_packages "AUR") and [FAQ#What if I run a full system upgrade and there will be an update for a shared library, but not for the applications that depend on it?](https://wiki.archlinux.org/title/FAQ#What_if_I_run_a_full_system_upgrade_and_there_will_be_an_update_for_a_shared_library,_but_not_for_the_applications_that_depend_on_it? "FAQ")


