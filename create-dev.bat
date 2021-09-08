chcp 65001
REM 生成一个开发用的VS工程目录
python -V
mkdir build
cd build

REM 现在这个命令只是为了装依赖库,而依赖库最全的是test_package工程
conan install ../test_package -s compiler.runtime=MD -s arch=x86_64 -s build_type=Release --build missing

REM 之后使用vscode的cmake插件构建工程
