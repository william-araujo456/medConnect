from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('hospital', '0002_alter_medication_type_application'),
    ]

    operations = [
        migrations.RunSQL("CREATE EXTENSION IF NOT EXISTS unaccent;")
    ]