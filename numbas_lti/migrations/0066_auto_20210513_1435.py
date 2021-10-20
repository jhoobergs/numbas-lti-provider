# Generated by Django 2.2.13 on 2021-05-13 13:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('numbas_lti', '0065_attempt_diffed'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='', help_text='Who is this for and what does it change?')),
                ('available_from', models.DateTimeField(blank=True, null=True, verbose_name='Available from')),
                ('available_until', models.DateTimeField(blank=True, null=True, verbose_name='Available until')),
                ('extend_deadline', models.DurationField(blank=True, null=True, verbose_name='Extend deadline by')),
                ('max_attempts', models.PositiveIntegerField(blank=True, help_text='Zero means unlimited attempts.', null=True, verbose_name='Maximum attempts per user')),
                ('extend_duration', models.FloatField(blank=True, null=True, verbose_name='Extend exam duration by')),
                ('extend_duration_units', models.CharField(choices=[('percent', 'percent'), ('minutes', 'minutes')], default='percent', max_length=10)),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='access_changes', to='numbas_lti.Resource')),
                ('users', models.ManyToManyField(blank=True, related_name='access_changes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'access change',
                'verbose_name_plural': 'access changes',
            },
        ),
        migrations.AlterModelOptions(
            name='scormelement',
            options={'ordering': ['-time', '-counter', '-pk'], 'verbose_name': 'SCORM element', 'verbose_name_plural': 'SCORM elements'},
        ),
        migrations.CreateModel(
            name='UsernameAccessChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('access_change', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usernames', to='numbas_lti.AccessChange')),
            ],
        ),
        migrations.CreateModel(
            name='EmailAccessChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('access_change', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='numbas_lti.AccessChange')),
            ],
        ),
    ]
