# telegram auto translator
  Automatic translator of your telegram messages
 <p align="center">For the bot to work correctly, install the latest version of python.

### Installation:
```sh
mkdir telegramtranslator && cd telegramtranslator
```
```sh
virtualenv venv
```
```sh
venv\Scripts\activate
```
```sh
git clone https://github.com/l1v0n1/telegram-auto-translator.git
```
```sh
cd telegram-auto-translator
```
```sh
pip install -r requirements.txt
```
### Setup:
```
go to https://my.telegram.org/apps log in, create an application, take api id and api hash and replace this in translator.py file
```python
API_ID = 123
API_HASH = "123"
```

### Launch
```sh
python translator.py
```