# 1 闯关任务  

完成SSH连接与端口映射并运行hello_world.py 

## 1.1 [ssh连接]

1. 申请开发机并启动
   ![image-1515](https://github.com/jiangxiaobaiii/InternLM-openNotebook/blob/main/%E5%85%A5%E9%97%A8%E5%B2%9B/%E7%AC%AC1%E5%85%B3Linux%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/%E5%BC%80%E5%8F%91%E6%9C%BA%E5%88%9B%E5%BB%BA.png?raw=true)

2. 创建ssh连接
    ssh-keygen支持RSA和DSA两种认证密钥。

    常用参数包括：

    -t：指定密钥类型，如dsa、ecdsa、ed25519、rsa。
    -b：指定密钥长度。
    -C：添加注释。
    -f：指定保存密钥的文件名。
    -i：读取未加密的ssh-v2兼容的私钥/公钥文件

   - win下已有key在C:\Users\用户名\.ssh\
   - [新生成](https://github.com/InternLM/Tutorial/blob/camp3/docs/L0/Linux/readme.md#222-%E9%85%8D%E7%BD%AEssh%E5%AF%86%E9%92%A5%E8%BF%9B%E8%A1%8Cssh%E8%BF%9C%E7%A8%8B%E8%BF%9E%E6%8E%A5%E5%8F%AF%E9%80%89)

   配置免密连接

3. win下cmd进行远程连接
 ![image-20240719163850639](https://github.com/jiangxiaobaiii/InternLM-openNotebook/blob/main/%E5%85%A5%E9%97%A8%E5%B2%9B/%E7%AC%AC1%E5%85%B3Linux%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/nvidia-smi.png?raw=true)


4. [vscode远程连接]()（**后续debug使用**）

![image-20240719164647128](https://github.com/jiangxiaobaiii/InternLM-openNotebook/blob/main/%E5%85%A5%E9%97%A8%E5%B2%9B/%E7%AC%AC1%E5%85%B3Linux%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/ssh%E8%BF%9E%E6%8E%A5.png?raw=true)

## 1.2 端口映射

- 创建示例web服务hello_world.py 

```python
# ssh连接开发机
# vim hello_world.py
import socket
import re
import gradio as gr
 
# 获取主机名
def get_hostname():
    hostname = socket.gethostname()
    match = re.search(r'-(\d+)$', hostname)
    name = match.group(1)
    
    return name
 
# 创建 Gradio 界面
with gr.Blocks(gr.themes.Soft()) as demo:
    html_code = f"""
            <p align="center">
            <a href="https://intern-ai.org.cn/home">
                <img src="https://intern-ai.org.cn/assets/headerLogo-4ea34f23.svg" alt="Logo" width="20%" style="border-radius: 5px;">
            </a>
            </p>
            <h1 style="text-align: center;">☁️ Welcome {get_hostname()} user, welcome to the ShuSheng LLM Practical Camp Course!</h1>
            <h2 style="text-align: center;">😀 Let’s go on a journey through ShuSheng Island together.</h2>
            <p align="center">
                <a href="https://github.com/InternLM/Tutorial/blob/camp3">
                    <img src="https://oss.lingkongstudy.com.cn/blog/202406301604074.jpg" alt="Logo" width="20%" style="border-radius: 5px;">
                </a>
            </p>

            """
    gr.Markdown(html_code)

demo.launch()
```

- 安装必要依赖pip install gradio==4.29.0
- 运行服务python hello_world.py
- 另起一个cmd，执行映射命令

```bash
ssh -p 36407 root@ssh.intern-ai.org.cn -CNg -L 7860:127.0.0.1:7860 -o StrictHostKeyChecking=no

#ssh -p 37367 root@ssh.intern-ai.org.cn -CNg -L {本地机器_PORT}:127.0.0.1:{开发机_PORT} -o StrictHostKeyChecking=no
```

命令各部分的含义：

- `-p 37367`：是指定 SSH 连接的端口为 37367，**注意修改为自己开发机的**。

- `root@ssh.intern-ai.org.cn`：表示要以 `root` 用户身份连接到 `ssh.intern-ai.org.cn` 这个主机。

- ```
  -CNg
  ```

  ：

  - `-C` 通常用于启用压缩。
  - `-N` 表示不执行远程命令，仅建立连接用于端口转发等。
  - `-g` 允许远程主机连接到本地转发的端口。

- `-L {本地机器_PORT}:127.0.0.1:{开发机_PORT}`：这是设置本地端口转发，将本地机器的指定端口（由 `{本地机器_PORT}` 表示）转发到远程主机（这里即 `ssh.intern-ai.org.cn`）的 `127.0.0.1` （即本地回环地址）和指定的开发机端口（由 `{开发机_PORT}` 表示）。

- `-o StrictHostKeyChecking=no`：关闭严格的主机密钥检查，这样可以避免第一次连接时因为未知主机密钥而产生的提示或错误。

![image-20240719171629972](https://github.com/jiangxiaobaiii/InternLM-openNotebook/blob/main/%E5%85%A5%E9%97%A8%E5%B2%9B/%E7%AC%AC1%E5%85%B3Linux%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/%E8%BF%90%E8%A1%8C%E7%BB%93%E6%9E%9C.png?raw=true)
**PS：不知道是不是bug。我这里并没有端口映射操作。仅就配置了免密登录和vscode连接**
# 2 可选任务

## 2.1 可选任务 1  

将Linux基础命令在开发机上完成一遍 

## 2.2 可选任务 2 

 使用 VSCODE 远程连接开发机并创建一个conda环境 
![image-20451356](https://github.com/jiangxiaobaiii/InternLM-openNotebook/blob/main/%E5%85%A5%E9%97%A8%E5%B2%9B/%E7%AC%AC1%E5%85%B3Linux%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83%E5%88%9B%E5%BB%BA.png?raw=true)

## 2.3 可选任务 3  

创建并运行test.sh文件

[提交作业](https://aicarrier.feishu.cn/share/base/form/shrcnZ4bQ4YmhEtMtnKxZUcf1vd)
