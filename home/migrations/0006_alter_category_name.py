# Generated by Django 5.0.4 on 2024-04-26 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_category_course_coursematerial_review_teacher_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('ssc', 'SSC'), ('hsc', 'HSC'), ('admission', 'Admission')], max_length=100),
        ),
    ]
