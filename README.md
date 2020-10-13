# conan-helloword-template
conan的初始工程模板。创建一个名字为ProjectName的命令如下：
``` bash
python ./CreateProjectTemplate.py -d ProjectName
```

## 在VSCode中使用Conan
1. 首先需要在vscode里面安装cmake插件。
2. 执行creat-dev.bat创建调试工程的依赖环境。
3. 使用vscode的cmake插件创建调试工程。选中c_cpp_properties.json文件，vscode的右下角选择Windows.

## 在xCode里使用Conan
由于我现在大量使用了GoogleTest,它有一个设置需要compiler.libcxx=libc++。否则过不了编译。
``` ini
[settings]
os=Macos
os_build=Macos
arch=x86_64
arch_build=x86_64
compiler=apple-clang
compiler.version=12.0
compiler.libcxx=libc++
build_type=Release
[options]
[build_requires]
[env]
```
vscode的cmake插件目前的设置如下
``` json
{
    "workbench.iconTheme": "material-icon-theme",
    "terminal.integrated.fontFamily": "Hack Nerd Font Mono",
    "editor.renderWhitespace": "all",
    "breadcrumbs.enabled": true,
    "terminal.integrated.scrollback": 50000,
    "cmake.generator": "Xcode",
    "cmake.preferredGenerators": [
        "Xcode",
        "Ninja",
        "Unix Makefiles"
    ],
    "git.autofetch": true,
    "explorer.confirmDelete": false,
    "workbench.colorTheme": "Visual Studio 2019 Dark",
}
```