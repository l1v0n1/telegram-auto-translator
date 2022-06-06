# telegram auto translator
  Automatic translator of your telegram messages
 <p align="center">For the bot to work correctly, install the latest version of python.

## Example
  


https://user-images.githubusercontent.com/70073044/172148688-a63716c2-3ba4-48c5-acd8-4e0bbf3ff4f3.MP4






  
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
Follow the link https://my.telegram.org/apps - log in, create an application, take api id and api hash and replace this in translator.py file
```python
API_ID = 123
API_HASH = "123"
```

### Launch
```sh
python translator.py
```
