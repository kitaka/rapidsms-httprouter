# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-12-23 13:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rapidsms', '0004_auto_20150801_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryError',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.TextField(help_text=b'A short log on the error that was received when this message was delivered')),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text=b'When this delivery error occurred')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('direction', models.CharField(choices=[(b'I', b'Incoming'), (b'O', b'Outgoing')], max_length=1)),
                ('status', models.CharField(choices=[(b'R', b'Received'), (b'H', b'Handled'), (b'P', b'Processing'), (b'L', b'Locked'), (b'Q', b'Queued'), (b'S', b'Sent'), (b'D', b'Delivered'), (b'C', b'Cancelled'), (b'E', b'Errored'), (b'F', b'Failed')], max_length=1)),
                ('date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('sent', models.DateTimeField(blank=True, null=True)),
                ('delivered', models.DateTimeField(blank=True, null=True)),
                ('external_id', models.CharField(blank=True, help_text=b'An arbitrary id which you can use to map ids assigned by an external backend to your local messages', max_length=64, null=True)),
                ('connection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='rapidsms.Connection')),
                ('in_response_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='rapidsms_httprouter.Message')),
            ],
        ),
        migrations.AddField(
            model_name='deliveryerror',
            name='message',
            field=models.ForeignKey(help_text=b'The message that had an error', on_delete=django.db.models.deletion.CASCADE, related_name='errors', to='rapidsms_httprouter.Message'),
        ),
        migrations.AlterIndexTogether(
            name='message',
            index_together=set([('direction', 'date')]),
        ),
    ]
