## Description

A simple Django application for browsing and saving AI-generated images
from [thispersondoesnotexist.com](https://thispersondoesnotexist.com).

## Features:

1. `gallery/preview/` – displays a random image and allows you to save it under a chosen index.
2. `gallery/preview/<int:index>/` – displays the saved image for a given index.

## Install required packages using poetry:

```bash
poetry install
```

## Apply migrations and run the server:

```bash
python manage.py migrate
python manage.py runserver
```

## Usage

- Open in browser: `http://127.0.0.1:8000/gallery/preview/` to view a random image and save it under an index.
- Open in browser: `http://127.0.0.1:8000/gallery/preview/<index>/` to view the saved image for a specific index.

## Notes

- Saved images are stored in the `media/` folder.
