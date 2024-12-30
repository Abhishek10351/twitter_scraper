# twitter_scraper

A scraper that scrapes the top trending topics on the twitter homepage

## Installation

### With poetry

```bash
pip install poetry
poetry install
poetry shell
```

### Without poetry

```bash
pip install -r requirements.txt
```

## Usage

```bash
# for windows systems use the following command
py manage.py runserver
# for unix systems use the following command
python3 manage.py runserver
```

After this command, a chrome window will open which prompt you to login to your twitter account.
**Note: This is completely safe as the data isn't stored anywhere and deleted after closing the server.**
After logging in, open the following links and view the scraped results.
Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and follow the instructions
