# Generated by Django 5.1.4 on 2024-12-06 17:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("BookShelf", "0002_book_cover_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="status",
            field=models.CharField(
                choices=[("В наличии", "В наличии"), ("Выдана", "Выдана")],
                default="В наличии",
                max_length=20,
            ),
        ),
    ]
