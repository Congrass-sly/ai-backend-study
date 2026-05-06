# Python PIP 常用命令大全
## 1. 版本查看
pip --version
pip3 --version

## 2. 安装第三方库
pip install 库名

## 3. 卸载库
pip uninstall 库名

## 4. 查看已安装库
pip list

## 5. 查看库详情
pip show 库名

## 6. 升级 pip
python -m pip install --upgrade pip

## 7. 安装指定版本
pip install 库名==版本号

## 8. 清华镜像加速
pip install 库名 -i https://pypi.tuna.tsinghua.edu.cn/simple

## 9. 导出依赖
pip freeze > requirements.txt

## 10. 批量安装依赖
pip install -r requirements.txt

二、国内清华镜像源（解决下载慢 / 超时）
临时使用清华源安装
bash
运行
pip install 库名 -i https://pypi.tuna.tsinghua.edu.cn/simple
三、项目依赖管理（工作 / 面试必会）
1. 导出当前项目所有依赖到 requirements.txt
bash
运行
pip freeze > requirements.txt
2. 从 requirements.txt 批量安装所有依赖
bash
运行
pip install -r requirements.txt
四、PIP 常见报错 & 现成解决方案
1. 下载超时、网速慢、连接失败
原因：官方源国外网络差解决：改用清华镜像
bash
运行
pip install 库名 -i https://pypi.tuna.tsinghua.edu.cn/simple
2. 'pip' 不是内部或外部命令
原因：Python 没加入系统环境变量解决：绕开直接用 python 调用
bash
运行
python -m pip install 库名
3. 权限不足、拒绝访问
解决：终端右键 以管理员身份运行 再执行命令
4. 多 Python 版本分不清 pip /pip3
统一最稳写法，不会装错环境：
bash
运行
python -m pip install 库名
python3 -m pip install 库名
5. 安装成功，但 import 找不到库
排查：
bash
运行
pip show 库名
看 Location 路径，和 VSCode 选中的 Python 解释器路径是否一致。



虚拟环境：Python 版本管理和依赖隔离的利器
# PIP + 虚拟环境 速查笔记
## 一、规范写法（必记）
统一用：python -m pip xxx
作用：防止多Python版本装错环境

## 二、常用PIP命令
# 安装库
python -m pip install 库名

# 清华镜像加速
python -m pip install 库名 -i https://pypi.tuna.tsinghua.edu.cn/simple

# 安装指定版本
python -m pip install 库名==版本号

# 升级库
python -m pip install --upgrade 库名

# 卸载库
python -m pip uninstall 库名

# 查看已安装库
python -m pip list

# 查看库详情（路径、版本）
python -m pip show 库名

# 升级pip自身
python -m pip install --upgrade pip

## 三、项目依赖管理（工作必考）
# 导出所有依赖到文件
pip freeze > requirements.txt

# 新环境批量安装依赖
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

## 四、虚拟环境全套（面试必背）
### 1. 作用
1. 项目依赖隔离，互不干扰
2. 不污染全局Python环境
3. 不同项目可使用不同库版本

### 2. 全套命令
# 创建虚拟环境
python -m venv venv

# Windows激活
venv\Scripts\activate

# 退出虚拟环境
deactivate

## 五、常见报错快速解决
1. pip不是内部命令
   改用：python -m pip xxx

2. 下载超时/网速慢
   加清华镜像源 -i 地址

3. 安装成功但导包找不到
   pip show 库名 核对安装路径与解释器路径

cd 只能切换到文件夹，不能切换到文件