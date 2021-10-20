# Generated by Django 3.2.7 on 2021-10-14 12:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('numbas_lti', '0068_alter_remarkpart_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('outfile', models.FileField(upload_to='reports/', verbose_name='Output file')),
                ('status', models.CharField(choices=[('inprogress', 'In progress'), ('complete', 'Complete')], default='inprogress', max_length=10)),
                ('creation_time', models.DateTimeField(auto_now_add=True, verbose_name='Time this report was created')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='file_reports', to=settings.AUTH_USER_MODEL)),
                ('resource', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_reports', to='numbas_lti.resource')),
            ],
        ),
    ]
