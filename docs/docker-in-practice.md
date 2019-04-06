Docker 实践

- by 代码会说话

## 第一期 初探 Docker

### 基本概念

- 镜像 光盘
- 容器 电影内容
- 镜像仓库

### 常用命令

1. `FROM` 命令语法说明 `[<用户名>/]<仓库名>:<标签>`
   对于 Docker 官方维护镜像来说，用户名省略。

## 第二期 初探 Docker 数据存储

> by 代码会说话

why?
how?

1. 路径绑定
   注意：

- 使用绝对路径。

2. 数据存储卷

不推荐使用 `-v` 的绑定方式。`--mount`

3. 使用已有数据填充空的 数据存储卷

## 第三期 CMD 指令与 ENTRYPOINT 指令 实例详解

1. alpine 极简镜像
2. ENTRYPOINT
3. CMD

## Docker 实践 (4) 容器进程启动的两种模式: `exec` 形式和 `shell` 形式

> by 代码会说话

1. `exec` 模式，不会通过 shell 调用。注意：因此不会替换命令中的 _\$HOME_ 之类的 SHELL 变量。 `~`

2. `shell` 模式，相比 `exec` 模式增加了 `sh -c` 作来启动。这带来的影响的是 容器的信号首先`sh`程序接收了。
   导致进程无法优雅退出。

## Docker 实践 (5) 容器网络配置之单机网络 （1）自定义 bridge

> redis 主从架构单机容器网络配置
> by 代码会说话

### 网络驱动概览

- `bridge` (网桥,默认驱动)，自定义 `bridge` 网络是单机网络多容器通信的最佳选择。
- `host` 消除容器与宿主机的网络空间隔离。
- `overlay` 分布式多容器宿主。
- `macvlan` 可用于给容器设置 MAC 地址。模拟网络中真实的物理设备。
- `none` 不配置。
- 其他自定义网络插件。

### 自定义网桥和默认网桥的区别

1. 自定义 `bridge` 提供了更好的网络隔离性及互操作性。
   同一自定义的`bridge` 下的容器可以互相访问所有端口，不需要暴露端口到外部。
2. 自定义 `bridge` 提供了容器间的自动 DNS 解析能力。
   不再需要手动的 `--link`
3. 自定义 `bridge` 可以热插拔.
4. 每一个自定义 `bridge` 都有自己单独的配置。
5. 通过链接默认`bridge` 的容器存在共享环境变量的问题。
   自定义链接 可以通过挂载同一个文件共享，或者使用 `docker-compose` 的话，可以定义共享变量。

### 操作

1. `docker network create <mynetworkname>
2. `docker create --net` or `docker run --net`
3. redis 主从架构单机容器网络配置

## Docker 实践 (6) docker-machine 及简单应用

> by 代码会说话

### 需求

为多机 Docker 宿主机相关实验做准备。

### 解决方案

使用 Docker Machine.

1. Docker Machine 封装了配置外部宿主机的指令。
2. Docker Machine 不是集群解决方案

默认支持驱动主要有：
Amazon Web Services
Microsoft Azure
Digital Ocean
Exoscale
Google Compute Engine
Microsoft Hyper-V
OpenStack
Rackspace
IBM Softlayer
Oracle VirtualBox
VMware vCloud Air
VMware Fusion
VMware vSphere
第三方插件：
https://github.com/docker/docker.github.io/blob/master/machine/AVAILABLE_DRIVER_PLUGINS.md

### 创建 VirtualBox 虚拟机

1. 确认已经安装 VirtualBox

2. 创建 `docker-machine create --driver virtualbox <NAME>`
   > Tip: boot2docker.iso 可以自己先行下载放到缓存目录，以免执行命令时下载失败。

我的命名，以港口命名。

```
➜  ~ docker-machine create --driver virtualbox beihai
Running pre-create checks...
(beihai) Default Boot2Docker ISO is out-of-date, downloading the latest release...
(beihai) Latest release for github.com/boot2docker/boot2docker is v18.09.4
(beihai) Downloading /Users/banxi/.docker/machine/cache/boot2docker.iso from https://github.com/boot2docker/boot2docker/releases/download/v18.09.4/boot2docker.iso...
(beihai) 0%....10%....20%....30%....40%....50%....60%....70%....80%....90%....100%
Creating machine...
(beihai) Copying /Users/banxi/.docker/machine/cache/boot2docker.iso to /Users/banxi/.docker/machine/machines/beihai/boot2docker.iso...
(beihai) Creating VirtualBox VM...
(beihai) Creating SSH key...
(beihai) Starting the VM...
(beihai) Check network to re-create if needed...
(beihai) Waiting for an IP...
Waiting for machine to be running, this may take a few minutes...
Detecting operating system of created instance...
Waiting for SSH to be available...
Detecting the provisioner...
Provisioning with boot2docker...
Copying certs to the local machine directory...
Copying certs to the remote machine...
Setting Docker configuration on the remote daemon...
Checking connection to Docker...
Docker is up and running!
To see how to connect your Docker Client to the Docker Engine running on this virtual machine, run: docker-machine env beihai
```

C/S
