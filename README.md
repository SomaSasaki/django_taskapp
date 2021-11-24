# スケジュール管理アプリ
現在開発中です(2021年11月現在)
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
$ python3 manage.py makemigtations accounts --settings config.setting.local
$ python3 manage.py makemigtations django_taskapp --settings config.setting.local
$ python3 manage.py migrate --settings config.setting.local
$ python3 manage.py runserver --settings config.setting.local
```
