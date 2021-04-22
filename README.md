# 

```
pipenv install fastapi
pipenv install uvicorn
```

```
uvicorn src.startup:app
```

https://fastapi.tiangolo.com/ja/

Fastapi x openapi

https://qiita.com/yoshi0518/items/52914cd1211eff4b93d0

template

https://fastapi.tiangolo.com/advanced/templates/

```
pipenv install jinja2
pipenv install aiofiles
```


https://rightcode.co.jp/blog/information-technology/fastapi-tutorial-todo-apps-environment


SQL Database

https://github.com/tys-hiroshi/docker-compose-mysql-phpmyadmin

https://fastapi.tiangolo.com/ja/advanced/async-sql-databases/

```
pipenv install databases
pipenv install sqlalchemy
#pipenv install pymysql  # https://qiita.com/xfan/items/f2c88aeb0d3945ed4775
pipenv install mysql-python

pipenv install databases[mysql]
```

pipenv install mysqlclient でエラーになるとき。

## ubuntu

```
sudo apt install -y mysql-server
sudo apt install -y libmysqlclient-dev
```

## mac

以下を行う。

```
brew install mysql-connector-c


Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
`python3`, `python3-config`, `pip3` etc., respectively, have been installed into
  /usr/local/opt/python@3.9/libexec/bin

You can install Python packages with
  pip3 install <package>
They will install into the site-package directory
  /usr/local/lib/python3.9/site-packages

tkinter is no longer included with this formula, but it is available separately:
  brew install python-tk@3.9

See: https://docs.brew.sh/Homebrew-and-Python
==> icu4c
icu4c is keg-only, which means it was not symlinked into /usr/local,
because macOS provides libicucore.dylib (but nothing else).

If you need to have icu4c first in your PATH, run:
  echo 'export PATH="/usr/local/opt/icu4c/bin:$PATH"' >> ~/.zshrc
  echo 'export PATH="/usr/local/opt/icu4c/sbin:$PATH"' >> ~/.zshrc

For compilers to find icu4c you may need to set:
  export LDFLAGS="-L/usr/local/opt/icu4c/lib"
  export CPPFLAGS="-I/usr/local/opt/icu4c/include"

For pkg-config to find icu4c you may need to set:
  export PKG_CONFIG_PATH="/usr/local/opt/icu4c/lib/pkgconfig"
```


```
brew install mysql
```

```
mysql -u docker -h 127.0.0.1 -D test_database -p
```

https://zenn.dev/yusugomori/articles/a3d5dc8baf9e386a58e5

https://qiita.com/satto_sann/items/4fbc1a4e2b33fa2237d2


### firestore

https://firebase.google.com/docs/firestore/quickstart#python_1
https://console.firebase.google.com/u/0/project/bnode-2cd0d/authentication/providers
https://googleapis.dev/python/firestore/latest/index.html
https://qiita.com/yusukeito58/items/c77feaa25fbbe37e9953

add data

https://firebase.google.com/docs/firestore/manage-data/add-data

pipenv install firebase-admin
pipenv install google-cloud-firestore
