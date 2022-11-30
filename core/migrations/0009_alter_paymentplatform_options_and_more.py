# Generated by Django 4.1.3 on 2022-11-29 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_alter_order_reference_alter_paymentplatform_active_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="paymentplatform",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AlterModelOptions(
            name="transaction",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AlterModelOptions(
            name="wallet",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AlterField(
            model_name="order",
            name="reference",
            field=models.CharField(default="802B74C8F28A8E46", max_length=50),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="reference",
            field=models.CharField(default="342AD48169E1192F", max_length=50),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="status",
            field=models.CharField(
                choices=[
                    ("SUCCESSFUL", "Successful"),
                    ("PENDING", "Pending"),
                    ("FAILED", "Failed"),
                ],
                max_length=50,
            ),
        ),
    ]
