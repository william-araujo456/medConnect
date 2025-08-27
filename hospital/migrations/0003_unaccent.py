from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('hospital', '0002_moreinfo'),
    ]

    operations = [
        migrations.RunSQL('CREATE EXTENSION IF NOT EXISTS unnacent')
    ]