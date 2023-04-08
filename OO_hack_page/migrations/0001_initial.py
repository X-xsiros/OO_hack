

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='REstate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_state', models.CharField(verbose_name='State')),
                ('object_dist', models.CharField(verbose_name='District')),
                ('object_adress', models.CharField(verbose_name='Adress')),
                ('object_type', models.CharField(choices=[('LV', 'Жилое помещение'), ('NL', 'Нежилое помещение'), ('AP', 'Квартира'), ('EH', 'Доходный дом'), ('MH', 'Общежитие'), ('HO', 'Отель'), ('GH', 'Дом престарелых'), ('ST', 'Склад'), ('SR', 'Стрит-ретейл'), ('OF', 'Офис'), ('SM', 'Супермаркет'), ('TC', 'Торговый центр'), ('OR', 'Другое')], default='OR', verbose_name='Type')),
                ('object_status', models.CharField(choices=[('EX', 'Введено в экспаутацию'), ('NC', 'Незавершенное строительство'), ('NR', 'Требует реконструкции'), ('NE', 'Не в ведено в эксплаутацию'), ('DE', 'Назначено под снос'), ('NA', 'Статус не определен')], default='NA', verbose_name='Status')),
                ('object_square', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Square')),
                ('object_client', models.CharField(verbose_name='Client')),
                ('object_photo', models.CharField(verbose_name='Photo')),
                ('object_video', models.CharField(verbose_name='Video')),
                ('object_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OO_hack_page.owner')),
            ],
        ),
    ]
