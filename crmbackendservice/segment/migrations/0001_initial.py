# Generated by Django 4.2.5 on 2024-02-04 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityFilter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('users_did_events_operation', models.CharField(choices=[('and', 'And'), ('or', 'Or')], max_length=20)),
                ('users_not_did_events_operation', models.CharField(choices=[('and', 'And'), ('or', 'Or')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='DataType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserAttribute',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('attribute_id', models.CharField(max_length=50, unique=True)),
                ('data_type', models.CharField(choices=[('number', 'Number'), ('string', 'String'), ('date', 'Date'), ('boolean', 'Boolean')], max_length=20)),
                ('type', models.CharField(choices=[('system', 'System'), ('custom', 'Custom')], max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('active', 'Active'), ('de-active', 'De-Active'), ('deleted', 'Deleted')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserAttributeFilter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('condition', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=100)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='segment.userattribute')),
            ],
        ),
        migrations.CreateModel(
            name='UserFilterCondition',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('condition_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('active', 'Active'), ('de-active', 'De-Active'), ('deleted', 'Deleted')], max_length=20)),
                ('applicable_data_types', models.ManyToManyField(blank=True, to='segment.datatype')),
            ],
        ),
        migrations.CreateModel(
            name='UserSegment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('segment_type', models.CharField(choices=[('static', 'Static'), ('dynamic', 'Dynamic')], max_length=20)),
                ('customer_type', models.CharField(choices=[('new', 'New'), ('regular', 'Regular'), ('frequent_visitor', 'Frequent Visitor'), ('lapsed', 'Lapsed')], max_length=50)),
                ('country_filter_operation', models.CharField(choices=[('any', 'Any'), ('none', 'None'), ('not_applicable', 'Not Applicable')], max_length=20)),
                ('user_attribute_filter_operation', models.CharField(choices=[('and', 'And'), ('or', 'Or')], max_length=20)),
                ('activity_filters', models.ManyToManyField(blank=True, to='segment.activityfilter')),
                ('filtered_countries', models.ManyToManyField(blank=True, to='segment.country')),
                ('user_attribute_filters', models.ManyToManyField(blank=True, to='segment.userattributefilter')),
                ('user_ids_filter_condition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='segment.userfiltercondition')),
            ],
        ),
        migrations.AddField(
            model_name='activityfilter',
            name='users_did_events',
            field=models.ManyToManyField(blank=True, to='segment.event'),
        ),
        migrations.AddField(
            model_name='activityfilter',
            name='users_not_did_events',
            field=models.ManyToManyField(blank=True, related_name='users_not_did_events', to='segment.event'),
        ),
    ]
