# SpiderMan

一个爬取相关视频的开源爬虫系统。

# 运行

1. Python安装

2. 安装依赖

```
yum install python-devel mysql-devel gcc
```

3. 安装和运行redis

```
$ wget http://download.redis.io/releases/redis-2.8.3.tar.gz
$ tar xzvf redis-2.8.3.tar.gz
$ cd redis-2.8.3
$ make
$ make install
$ redis-server
```

4. 更新配置

配置爬虫的源地址等，如pornhub.com等。

5. 创建和初始化数据库

```
mysql> CREATE DATABASE `pornhub` CHARACTER SET utf8;
```

6. 启动SpiderMan

```
python bootstrap.py
```

# TODO

# License
Licensed under the MIT License.

