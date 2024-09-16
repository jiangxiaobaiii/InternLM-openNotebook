参考链接
官网：https://git-scm.com/

官方文档：[Git - Book](https://git-scm.com/book/en/v2)

Git 基础：[Git 基础知识](https://aicarrier.feishu.cn/wiki/YAXRwLZxPi8Hy6k3tOQcuwAHn5g)
[书生浦语git文档](https://github.com/InternLM/Tutorial/blob/camp3/docs/L0/Git/readme.md)

# 1 破冰活动
提交一份自我介绍。
- 1 将该项目复制到你自己的GitHub账户下，fork 项目https://github.com/InternLM/Tutorial
- 2 克隆Fork的项目到本地
bash
git clone https://github.com/your_username/project_name.git

- 3 添加上游仓库
- 4 拉取最新更改
- 5 创建新分支
- 6 进行修改
- 7 提交更改
- 8 推送至远程仓库
- 9 创建Pull Request:
  - 回到你的GitHub仓库页面，你会看到一个提示说可以从你的分支向原项目发送一个Pull Request。
  - 点击“Compare & pull request”按钮，填写PR描述，然后提交。
- 10 等待审查

# 1 实践项目
创建并提交一个项目。这里以GitHub为例
- 1 GitHub 新建一个repo
- 2 本地创建一个路径如gpt-document，cd gpt-document
- 3 创建README.md文件
- 4 初始化仓库
- 5 配置remote
- 6 git add README.md文件
- 7 git commit -m"init"
- 8 git push -u master:master


git add files 把当前文件放入暂存区域

git commit 给暂存区域生成快照并提交

git reset -- files 用来撤销最后一次的git add files ,也可以用 git reset 撤销所有暂存区域文件

git checkout --files 把文件从暂存区域复制到工作目录，用来丢弃本地修改



git config   配置用户信息和偏好设置
git init  初始化一个新的 Git 仓库
git clone  克隆一个远程仓库到本地
git status  查看仓库当前的状态，显示有变更的文件
git add  将文件更改添加到暂存区
git commit  提交暂存区到仓库区
git branch  列出、创建或删除分支
git checkout  切换分支或恢复工作树文件
git merge  合并两个或更多的开发历史
git pull  从另一仓库获取并合并本地的版本
git push  更新远程引用和相关的对象
git remote  管理跟踪远程仓库的命令
git fetch  从远程仓库获取数据到本地仓库，但不自动合


分支上传成功
![image](https://github.com/jiangxiaobaiii/InternLM-openNotebook/blob/main/%E5%85%A5%E9%97%A8%E5%B2%9B/%E7%AC%AC3%E5%85%B3Git%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/%E4%B8%8A%E4%BC%A0%E6%88%90%E5%8A%9F.png?raw=true)

终端上传成功
![image](https://github.com/jiangxiaobaiii/InternLM-openNotebook/blob/main/%E5%85%A5%E9%97%A8%E5%B2%9B/%E7%AC%AC3%E5%85%B3Git%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/%E7%BB%88%E7%AB%AF%E6%8F%90%E4%BA%A4%E6%88%90%E5%8A%9F.png?raw=true)



