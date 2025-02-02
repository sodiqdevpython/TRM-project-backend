# Generated by Django 4.2.15 on 2024-09-07 04:01

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=32, unique=True, validators=[django.core.validators.MinLengthValidator(limit_value=5, message="Shaxar nomi juda qisqa, noto'g'ri kiritgansiz")])),
            ],
            options={
                'verbose_name': 'Shaxar',
                'verbose_name_plural': 'Shaxarlar',
            },
        ),
        migrations.CreateModel(
            name='Districts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=32, unique=True, validators=[django.core.validators.MinLengthValidator(limit_value=5, message="Tuman nomi juda qisqa, noto'g'ri kiritgansiz")])),
            ],
            options={
                'verbose_name': 'Tuman',
                'verbose_name_plural': 'Tumanlar',
            },
        ),
        migrations.CreateModel(
            name='Organizations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('organization_number', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=64, validators=[django.core.validators.MinLengthValidator(limit_value=5, message="Muassasa nomi juda qisqa, noto'g'ri kiritgansiz")])),
                ('education_type', models.CharField(choices=[("Maktabgacha ta'lim", "Maktabgacha ta'lim"), ("Umumiy o'rta ta'lim maktablari", "Umumiy o'rta ta'lim maktablari"), ('Musiqa maktablari', 'Musiqa maktablari'), ('Sport maktablari', 'Sport maktablari')], max_length=32)),
                ('power', models.PositiveBigIntegerField(default=0)),
                ('vr_mode_url', models.URLField(blank=True, null=True)),
                ('is_inclusive', models.BooleanField(default=False)),
                ('rating', models.CharField(choices=[('Qoniqarsiz', 'Qoniqarsiz'), ("O'rtacha", "O'rtacha"), ('Yaxshi', 'Yaxshi')], max_length=16)),
                ('is_city', models.BooleanField(default=False)),
                ('ball', models.PositiveBigIntegerField(default=0)),
                ('admin', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.cities')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.districts')),
            ],
            options={
                'verbose_name': 'Muassasa',
                'verbose_name_plural': 'Muassasa',
                'ordering': ['-ball'],
            },
        ),
        migrations.CreateModel(
            name='OrganizationStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(choices=[("Maktabgacha ta'lim", "Maktabgacha ta'lim"), ("Umumiy o'rta ta'lim maktablari", "Umumiy o'rta ta'lim maktablari"), ('Musiqa maktablari', 'Musiqa maktablari'), ('Sport maktablari', 'Sport maktablari')], max_length=32, unique=True)),
                ('number', models.PositiveIntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Tashkilot turi',
                'verbose_name_plural': 'Tashkilot turlari',
            },
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=32, unique=True, validators=[django.core.validators.MinLengthValidator(limit_value=6, message="Viloyat nomi juda qisqa, noto'g'ri kiritgansiz")])),
            ],
            options={
                'verbose_name': 'Viloyat',
                'verbose_name_plural': 'Viloyatlar',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='RoomsEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=256, validators=[django.core.validators.MinLengthValidator(3, "Jihoz nomi juda qisqa, xato kiritgan bo'lishingiz mumkin !")])),
                ('measure_type', models.CharField(choices=[('dona', 'dona'), ('juftlik', 'juftlik'), ("to'plam", "to'plam")], max_length=8)),
                ('amount', models.PositiveBigIntegerField(default=1)),
                ('avilable_type', models.CharField(choices=[('Soz', 'Soz'), ('Nosoz', 'Nosoz'), ('Yaroqsiz', 'Yaroqsiz')], max_length=32)),
                ('accepted_date', models.DateField()),
                ('entered_date', models.DateField()),
                ('when_first_time_used', models.DateField()),
                ('when_made', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MaxValueValidator(2024)])),
                ('image1', models.ImageField(blank=True, null=True, upload_to='school/rooms/equipement/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='school/rooms/equipement/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='school/rooms/equipement/')),
                ('penny_by_year', models.FloatField()),
                ('xarakteri', models.TextField(blank=True, null=True)),
                ('equipment_type', models.CharField(choices=[('Asbob uskunalar', 'Asbob uskunalar'), ('Jihozlar', 'Jihozlar')], max_length=16)),
            ],
            options={
                'verbose_name': 'Xona jihozi',
                'verbose_name_plural': 'Xonalar jihozlari',
            },
        ),
        migrations.CreateModel(
            name='RoomsType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Xona turi',
                'verbose_name_plural': 'Xonalar turlari',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(default='No Name', max_length=32)),
                ('last_name', models.CharField(default='No Last Name', max_length=32)),
                ('father_name', models.CharField(max_length=32)),
                ('passport_id', models.CharField(max_length=9, unique=True)),
                ('manzil', models.CharField(max_length=256)),
                ('pinfl', models.CharField(max_length=14, unique=True)),
                ('position', models.CharField(max_length=512)),
                ('tel_number', models.CharField(max_length=9)),
                ('command_pdf', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx'])])),
                ('is_active', models.BooleanField(default=True)),
                ('is_selected', models.BooleanField(default=False)),
                ('is_super_admin', models.BooleanField(default=False)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Foydalanuvchi profili',
                'verbose_name_plural': 'Foydalanuvchilar profillari',
            },
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('students_amount', models.PositiveSmallIntegerField(default=1)),
                ('room_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.roomstype')),
                ('room_uquipment', models.ManyToManyField(to='school.roomsequipment')),
            ],
            options={
                'verbose_name': 'Xona',
                'verbose_name_plural': 'Xonalar',
            },
        ),
        migrations.CreateModel(
            name='OverallClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('rooms_amount', models.PositiveSmallIntegerField(default=1, help_text='Xonalar soni')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.organizations')),
            ],
            options={
                'verbose_name': 'Umumiy sinf',
                'verbose_name_plural': 'Umumiy sinflar',
            },
        ),
        migrations.AddField(
            model_name='organizations',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.regions'),
        ),
        migrations.CreateModel(
            name='HistoricalUserProfile',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('updated', models.DateTimeField(blank=True, editable=False)),
                ('first_name', models.CharField(default='No Name', max_length=32)),
                ('last_name', models.CharField(default='No Last Name', max_length=32)),
                ('father_name', models.CharField(max_length=32)),
                ('passport_id', models.CharField(db_index=True, max_length=9)),
                ('manzil', models.CharField(max_length=256)),
                ('pinfl', models.CharField(db_index=True, max_length=14)),
                ('position', models.CharField(max_length=512)),
                ('tel_number', models.CharField(max_length=9)),
                ('command_pdf', models.TextField(max_length=100, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx'])])),
                ('is_active', models.BooleanField(default=True)),
                ('is_selected', models.BooleanField(default=False)),
                ('is_super_admin', models.BooleanField(default=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Foydalanuvchi profili',
                'verbose_name_plural': 'historical Foydalanuvchilar profillari',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalRoomsType',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('updated', models.DateTimeField(blank=True, editable=False)),
                ('name', models.CharField(max_length=128)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Xona turi',
                'verbose_name_plural': 'historical Xonalar turlari',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalRoomsEquipment',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('updated', models.DateTimeField(blank=True, editable=False)),
                ('name', models.CharField(max_length=256, validators=[django.core.validators.MinLengthValidator(3, "Jihoz nomi juda qisqa, xato kiritgan bo'lishingiz mumkin !")])),
                ('measure_type', models.CharField(choices=[('dona', 'dona'), ('juftlik', 'juftlik'), ("to'plam", "to'plam")], max_length=8)),
                ('amount', models.PositiveBigIntegerField(default=1)),
                ('avilable_type', models.CharField(choices=[('Soz', 'Soz'), ('Nosoz', 'Nosoz'), ('Yaroqsiz', 'Yaroqsiz')], max_length=32)),
                ('accepted_date', models.DateField()),
                ('entered_date', models.DateField()),
                ('when_first_time_used', models.DateField()),
                ('when_made', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MaxValueValidator(2024)])),
                ('image1', models.TextField(blank=True, max_length=100, null=True)),
                ('image2', models.TextField(blank=True, max_length=100, null=True)),
                ('image3', models.TextField(blank=True, max_length=100, null=True)),
                ('penny_by_year', models.FloatField()),
                ('xarakteri', models.TextField(blank=True, null=True)),
                ('equipment_type', models.CharField(choices=[('Asbob uskunalar', 'Asbob uskunalar'), ('Jihozlar', 'Jihozlar')], max_length=16)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Xona jihozi',
                'verbose_name_plural': 'historical Xonalar jihozlari',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalRooms',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('updated', models.DateTimeField(blank=True, editable=False)),
                ('students_amount', models.PositiveSmallIntegerField(default=1)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('room_category', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='school.roomstype')),
            ],
            options={
                'verbose_name': 'historical Xona',
                'verbose_name_plural': 'historical Xonalar',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalRegions',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('updated', models.DateTimeField(blank=True, editable=False)),
                ('name', models.CharField(db_index=True, max_length=32, validators=[django.core.validators.MinLengthValidator(limit_value=6, message="Viloyat nomi juda qisqa, noto'g'ri kiritgansiz")])),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Viloyat',
                'verbose_name_plural': 'historical Viloyatlar',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalOverallClasses',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('updated', models.DateTimeField(blank=True, editable=False)),
                ('name', models.CharField(db_index=True, max_length=64)),
                ('rooms_amount', models.PositiveSmallIntegerField(default=1, help_text='Xonalar soni')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='school.organizations')),
            ],
            options={
                'verbose_name': 'historical Umumiy sinf',
                'verbose_name_plural': 'historical Umumiy sinflar',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalOrganizationStatistics',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('updated', models.DateTimeField(blank=True, editable=False)),
                ('type', models.CharField(choices=[("Maktabgacha ta'lim", "Maktabgacha ta'lim"), ("Umumiy o'rta ta'lim maktablari", "Umumiy o'rta ta'lim maktablari"), ('Musiqa maktablari', 'Musiqa maktablari'), ('Sport maktablari', 'Sport maktablari')], db_index=True, max_length=32)),
                ('number', models.PositiveIntegerField(default=1)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Tashkilot turi',
                'verbose_name_plural': 'historical Tashkilot turlari',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalOrganizations',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('updated', models.DateTimeField(blank=True, editable=False)),
                ('organization_number', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=64, validators=[django.core.validators.MinLengthValidator(limit_value=5, message="Muassasa nomi juda qisqa, noto'g'ri kiritgansiz")])),
                ('education_type', models.CharField(choices=[("Maktabgacha ta'lim", "Maktabgacha ta'lim"), ("Umumiy o'rta ta'lim maktablari", "Umumiy o'rta ta'lim maktablari"), ('Musiqa maktablari', 'Musiqa maktablari'), ('Sport maktablari', 'Sport maktablari')], max_length=32)),
                ('power', models.PositiveBigIntegerField(default=0)),
                ('vr_mode_url', models.URLField(blank=True, null=True)),
                ('is_inclusive', models.BooleanField(default=False)),
                ('rating', models.CharField(choices=[('Qoniqarsiz', 'Qoniqarsiz'), ("O'rtacha", "O'rtacha"), ('Yaxshi', 'Yaxshi')], max_length=16)),
                ('is_city', models.BooleanField(default=False)),
                ('ball', models.PositiveBigIntegerField(default=0)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('admin', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('city', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='school.cities')),
                ('district', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='school.districts')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('region', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='school.regions')),
            ],
            options={
                'verbose_name': 'historical Muassasa',
                'verbose_name_plural': 'historical Muassasa',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalDistricts',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('updated', models.DateTimeField(blank=True, editable=False)),
                ('name', models.CharField(db_index=True, max_length=32, validators=[django.core.validators.MinLengthValidator(limit_value=5, message="Tuman nomi juda qisqa, noto'g'ri kiritgansiz")])),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('region', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='school.regions')),
            ],
            options={
                'verbose_name': 'historical Tuman',
                'verbose_name_plural': 'historical Tumanlar',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCities',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('updated', models.DateTimeField(blank=True, editable=False)),
                ('name', models.CharField(db_index=True, max_length=32, validators=[django.core.validators.MinLengthValidator(limit_value=5, message="Shaxar nomi juda qisqa, noto'g'ri kiritgansiz")])),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('region', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='school.regions')),
            ],
            options={
                'verbose_name': 'historical Shaxar',
                'verbose_name_plural': 'historical Shaxarlar',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddField(
            model_name='districts',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.regions'),
        ),
        migrations.AddField(
            model_name='cities',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.regions'),
        ),
    ]
