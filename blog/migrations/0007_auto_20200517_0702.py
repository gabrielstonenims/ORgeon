# Generated by Django 3.0.6 on 2020-05-17 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200516_0720'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientinfoprogress',
            old_name='accessment_officer',
            new_name='assessment_officer',
        ),
        migrations.AddField(
            model_name='clientinfoprogress',
            name='assessment_phase_details',
            field=models.TextField(blank=True, help_text='Enter detailed info gathered for assessment here'),
        ),
        migrations.AddField(
            model_name='clientinfoprogress',
            name='care_plan',
            field=models.CharField(choices=[('Eagle', 'Eagle'), ('Kangaroo', 'Kangaroo'), ('Nested', 'Nested')], default='Eagle', help_text='Choose a plan for client', max_length=20),
        ),
        migrations.AddField(
            model_name='clientinfoprogress',
            name='development_phase_details',
            field=models.TextField(blank=True, help_text='Enter detailed info gathered for development here'),
        ),
        migrations.AddField(
            model_name='clientinfoprogress',
            name='evaluation_phase_details',
            field=models.TextField(blank=True, help_text='Enter detailed info gathered for evaluation here'),
        ),
        migrations.AddField(
            model_name='clientinfoprogress',
            name='implementation_phase_details',
            field=models.TextField(blank=True, help_text='Enter detailed info gathered for implementation here'),
        ),
        migrations.AddField(
            model_name='clientinfoprogress',
            name='planning_phase_details',
            field=models.TextField(blank=True, help_text='Enter detailed info gathered for planning here'),
        ),
        migrations.AddField(
            model_name='clientinfoprogress',
            name='star_phase_details',
            field=models.TextField(blank=True, help_text='Enter detailed info gathered for star here.'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='additional_message',
            field=models.CharField(default='To make a difference', help_text='Please press once on the button below', max_length=200),
        ),
    ]
