# Generated by Django 2.0 on 2019-12-26 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rapidsms_httprouter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryerror',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, help_text='When this delivery error occurred'),
        ),
        migrations.AlterField(
            model_name='deliveryerror',
            name='log',
            field=models.TextField(help_text='A short log on the error that was received when this message was delivered'),
        ),
        migrations.AlterField(
            model_name='deliveryerror',
            name='message',
            field=models.ForeignKey(help_text='The message that had an error', on_delete=django.db.models.deletion.CASCADE, related_name='errors', to='rapidsms_httprouter.Message'),
        ),
        migrations.AlterField(
            model_name='message',
            name='direction',
            field=models.CharField(choices=[('I', 'Incoming'), ('O', 'Outgoing')], max_length=1),
        ),
        migrations.AlterField(
            model_name='message',
            name='external_id',
            field=models.CharField(blank=True, help_text='An arbitrary id which you can use to map ids assigned by an external backend to your local messages', max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='status',
            field=models.CharField(choices=[('R', 'Received'), ('H', 'Handled'), ('P', 'Processing'), ('L', 'Locked'), ('Q', 'Queued'), ('S', 'Sent'), ('D', 'Delivered'), ('C', 'Cancelled'), ('E', 'Errored'), ('F', 'Failed')], max_length=1),
        ),
    ]
