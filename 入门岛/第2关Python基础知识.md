大模型笔记-书生训练营第三期闯关指南
## 1 闯关任务	

Python实现wordcount	

```python
import re
from collections import defaultdict

def wordcount(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()

    word_freq = defaultdict(int)

    for word in words:
        word_freq[word] += 1 

    return dict(word_freq)  


text = """
Got this panda plush toy for my daughter's birthday,
who loves it and takes it everywhere. It's soft and
super cute, and its face has a friendly look. It's
a bit small for what I paid though. I think there
might be other options that are bigger for the
same price. It arrived a day earlier than expected,
so I got to play with it myself before I gave it
to her.
"""

print(wordcount(text))

```

![image-20240719172629466](https://github.com/jiangxiaobaiii/InternLM-openNotebook/blob/main/%E5%85%A5%E9%97%A8%E5%B2%9B/%E7%AC%AC2%E5%85%B3Python%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/python%E5%AE%9E%E7%8E%B0wordcount.png?raw=true)

## 2 闯关任务	

Vscode连接InternStudio debug笔记


![image-20240719172843402](https://github.com/jiangxiaobaiii/InternLM-openNotebook/blob/main/%E5%85%A5%E9%97%A8%E5%B2%9B/%E7%AC%AC2%E5%85%B3Python%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/python%E8%BF%9B%E8%A1%8Cdebug.png?raw=true)

[提交作业](https://aicarrier.feishu.cn/share/base/form/shrcnZ4bQ4YmhEtMtnKxZUcf1vd)