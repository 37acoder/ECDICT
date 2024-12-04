# 使用官方的 Python 3 基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录的内容到工作目录
COPY ./server.py /app
COPY ./requirements.txt /app
COPY ./stardict.py /app
COPY ./init.py /app

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露应用程序运行的端口
EXPOSE 10099

# 使用 Gunicorn 启动 Flask 应用
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:10099", "server:app"]