# Text Pollinations SSE Client

本项目是一个简单的Python脚本，使用SSE（Server-Sent Events）从[Text Pollinations API](https://text.pollinations.ai/feed)请求流数据。

## 功能

- 通过SSE从API获取实时文本数据。
- 将返回的数据以JSON格式在控制台上打印，便于阅读和调试。

## 依赖

在运行本项目之前，请确保已安装以下Python包：

- `sseclient`
- `requests`

可以通过以下命令安装所需的包：

```
pip install sseclient requests
```

## 使用方法

1. 克隆或下载本项目。
2. 在终端中运行以下命令以启动SSE客户端：

```
python script.py
```

3. 观察控制台输出以查看从API获取的实时数据。