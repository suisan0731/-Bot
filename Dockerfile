#指定したイメージの内容を持ってくる(1)
FROM python:3.11

#Dockerコンテナのカレントディレクトリ設定
WORKDIR /usr/src/app

#requirements.txtをコンテナ側にコピー
COPY requirements.txt /usr/src/app/

#Dockerイメージ作成時に実行(2)
RUN python3 -m pip install -r requirements.txt

#(3)
COPY . /usr/src/app/

#コンテナを起動のタイミングで実行
CMD ["python3", "main.py"]


#python:3.11のイメージを元に(1)
#ライブラリをインストールし(2)
#最後に必要なソースコードをコンテナイメージにコピーしディスクイメージを作成(3)