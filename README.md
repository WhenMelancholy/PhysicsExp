# PhysicsExp
### USTC Physics Experiments Data Processing Tools

### 中科大大物实验数据处理工具

#### Comes with NO WARRENTY

*The package is also released on [pypi](https://pypi.org/project/physicsexp/).*

*For readers from pypi, [here](https://github.com/ustcpetergu/PhysicsExp) please.*

### Notice：项目分割！！

分割之后本项目只包含数据处理工具程序，具体的实验数据和用到的数据处理脚本（原Experiment目录）移动至[USTCPhysExpData](https://github.com/ustcpetergu/USTCPhysExpData)项目中.

## About

~~最终目的是建造一套用于自动化处理大物实验数据、绘制图像、生成可打印文档、将文档提交到在线打印系统的工具；针对常用数据处理需求实现简化和自动化，只要简单的几行代码，就能完成通用的绘图、拟合、不确定度计算等大物实验常用任务。~~
理想与现实差距还很大，目前仅仅包装了matplotlib绘图库、简单拟合、文件输入、docx生成，简化重复劳动。

### A Simple Guide

#### The easy way 

**You may want to use a virtualenv to run this program. **

**Install the package**

 Use USTC mirror to accelerate. Depencencies like numpy and matplotlib will be installed automatically. 

```
pip install -i https://mirrors.ustc.edu.cn/pypi/web/simple physicsexp
```

**Test the installation(Optional)**

```
>>> from physicsexp.mainfunc import *
>>> from physicsexp.gendocx import *
>>>
```

**Run the scripts**

```
python path/to/plot.py
```

For example if you run my scripts in USTCPhysExpData, you'll see graphs poped out and saved to .png, a generated gen.docx ready to print, and calculations(if any) printed to output. Then you can modify the code or write your own code to process your data!

#### For advanced users 

Assuming you are using Windows.

**Change the command to make then work on your device! Don't just copy & paste!**

 **Prepare to build**

Set up environment to build and release python packages, detailed guide can be found on pypi website. 

**Build**

```
python setup.py sdist bdist_wheel
```

Then the packaged wheel file can be found at `./dist/physicsexp-0.0.1-py3-none-any.whl`(Name may be different)

**Install**

**This package haven't been tested as it should be and I don't know what will happen after installation.**

**So using a virtualenv is recommended. **

Create a virtualenv(here named test-env)

```
python -m venv test-env
```

Activate it

```
./test-env/Scripts/activate.bat
```

Install the wheel (Use USTC mirror to accelerate, and it will download and install other required packages)

```
pip install -i https://mirrors.ustc.edu.cn/pypi/web/simple path\to\physicsexp-0.0.1-py3-none-any.whl
```

Wait a moment for the installation to finish.

### Usage

Wanna know how to use? Read the source code yourself, see templates at `physicsexp/Template/` and my programs in USTCPhysExpData (Most of them are already outdated and cannot be run, if you really need to run them, maybe a `git reset` is the last way) , or contact developer.

But most of the time neither of these works. 

**And can using these tools boost your efficiency? I don't know, but probably can't.**

**Finally, think twice before wasting time on this project, instead, enjoy your life, learn some real physics, and find a (boy|girl)friend.**

