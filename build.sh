#!/bin/bash

# نصب تمام پکیج‌ها طبق pyproject.toml
poetry install --no-interaction --no-ansi

# اجرای مهاجرت‌ها داخل محیط Poetry
poetry run python manage.py migrate

# جمع‌آوری فایل‌های استاتیک (اگه Django هست)
poetry run python manage.py collectstatic --noinput
