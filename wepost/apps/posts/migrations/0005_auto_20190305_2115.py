# Generated by Django 2.2b1 on 2019-03-05 21:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wepost_posts', '0004_dev_user_star_some_nodes'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='users',
            field=models.ManyToManyField(related_name='star_or_followed_nodes', through='wepost_posts.UserNodeStar', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='NodeModeratorRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='最后更新')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('memo', models.CharField(blank=True, default='', max_length=128, verbose_name='备注')),
                ('moderator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='管理员')),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wepost_posts.Node', verbose_name='节点')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='node',
            name='moderators',
            field=models.ManyToManyField(related_name='moderated_nodes', through='wepost_posts.NodeModeratorRelation', to=settings.AUTH_USER_MODEL),
        ),
    ]
