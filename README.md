# Analysis of the immo_eliza project

Simple dashboard used to get an idea of the content of our scraped dataset.

## How to use 

Begin by cloning and entering this repo
```sh
git clone https://github.com/Jojopanis/immo_eliza_analysis.git
cd immo_eliza_analysis/
```
You can then create a venv using python, and activate it
```sh
python -m venv /path/to/your/venv/folder/venvname
source /path/to/your/venv/folder/venvname/bin/activate
```
In some environments you need to use `python3` instead of `python`

Once in the venv you can insall all the required libraries 
```sh
pip install -r requirements.txt
```
In some environments you need to use `pip3` instead of `pip`

Lastly, you can run the file with
```sh
python dash_test.py
```
You should see an address on your local computer, most likely
> http://127.0.0.1:8050/

open it in your favorite browser and enjoy the dashboard!