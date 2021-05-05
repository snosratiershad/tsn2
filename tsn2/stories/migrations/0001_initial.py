# Generated by Django 3.2 on 2021-05-05 05:44

from django.db import migrations, models
import django.db.models.deletion
import location_field.models.plain
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='stories.post')),
                ('text', models.TextField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('stories.post',),
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='stories.post')),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('title', models.CharField(blank=True, max_length=60, null=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('stories.post',),
        ),
    ]
