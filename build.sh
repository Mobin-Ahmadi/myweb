#!/bin/bash

# نصب پکیج‌ها
poetry install

# اجرای مهاجرت‌ها
python manage.py migrate

# جمع‌آوری فایل‌های استاتیک (اگه Django هست)
python manage.py collectstatic --noinput
