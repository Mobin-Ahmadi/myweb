#!/bin/bash

# نصب پکیج‌ها از requirements.txt
pip install --upgrade pip
pip install -r requirements.txt

# اجرای مهاجرت‌ها
python manage.py migrate

# جمع‌آوری فایل‌های استاتیک
python manage.py collectstatic --noinput
