# スケジュール管理アプリ
現在開発中です(2021/11/6時点)
<br>
<br>

### プロジェクトに参加するには


#### 1. Python3とGitを事前にインストールしておく
#### 2. リポジトリをローカルにコピーする

```
$ cd 任意のフォルダ
$ git clone https://github.com/SomaSasaki/django_taskapp.git
```

#### 3. ブランチを作成する。<br>
誤って他人のブランチを破壊しないよう、必ず新規作成してください。<br>
ブランチ名は他人と被らないようにお願いします。

```
$ git checkout -b develop main  //mainブランチからdevelopブランチを作成
$ git branch -vv //ブランチを確認
$ git push -u origin develop //githubにdevelopブランチを登録
```

<br>
<br>

### アプリを実行してみる

```
$ pip3 install -r requirements.txt
$ python3 manage.py makemigtations --settings config.setting.local
$ python3 manage.py migrate --settings config.setting.local
$ python3 manage.py runserver --settings config.setting.local
```
