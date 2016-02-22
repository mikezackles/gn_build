This project is meant to facilitate building C++ using
[generate ninja](https://chromium.googlesource.com/chromium/src/tools/gn/)

To use it, just include it as a git submodule:
```shell
cd project_root
git submodule add https://github.com/mikezackles/gn_build build
echo "buildconfig = \"//build/config/BUILDCONFIG.gn\"" >> .gn
```

If you make any changes you feel might be useful to others, please feel free to
submit a pull request!
