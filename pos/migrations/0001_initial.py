# Generated by Django 2.1.15 on 2021-04-14 09:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PosAperturaCaja',
            fields=[
                ('id', models.CharField(db_column='ID', editable=False, max_length=10, primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(blank=True, db_column='Fecha', default=django.utils.timezone.now, null=True)),
                ('numero', models.CharField(blank=True, db_column='Número', default='', max_length=10, null=True, unique=True)),
                ('detalle', models.CharField(blank=True, db_column='Detalle', default='', max_length=100, null=True)),
                ('total', models.DecimalField(db_column='Total', decimal_places=4, default=0, max_digits=19)),
                ('creadopor', models.CharField(blank=True, db_column='CreadoPor', default='', max_length=15, null=True)),
                ('creadodate', models.DateTimeField(auto_now_add=True, db_column='CreadoDate', null=True)),
                ('cerrada', models.BooleanField(db_column='Cerrada', default=False)),
                ('cerradapor', models.CharField(blank=True, db_column='CerradaPor', default='', max_length=15, null=True)),
                ('cerradadate', models.DateTimeField(auto_now=True, db_column='CerradaDate', null=True)),
                ('ingresoid', models.CharField(blank=True, db_column='IngresoID', default='', max_length=10, null=True)),
                ('fecha_cierre', models.DateTimeField(blank=True, db_column='FechaCierre', null=True)),
                ('pcid', models.CharField(blank=True, db_column='PcID', default='', editable=False, max_length=50, null=True)),
                ('sobrante', models.DecimalField(blank=True, db_column='Sobrante', decimal_places=4, default=0, max_digits=19, null=True)),
                ('faltante', models.DecimalField(blank=True, db_column='Faltante', decimal_places=4, default=0, max_digits=19, null=True)),
            ],
            options={
                'verbose_name': 'Apertura de caja',
                'verbose_name_plural': 'Aperturas caja',
                'db_table': 'POS_APERTURA_CAJA',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PosCierre',
            fields=[
                ('id', models.CharField(db_column='ID', editable=False, max_length=10, primary_key=True, serialize=False)),
                ('numero', models.CharField(blank=True, db_column='Número', default='', max_length=10, null=True)),
                ('usuarioid', models.CharField(blank=True, db_column='UsuarioID', default='', max_length=10, null=True)),
                ('fecha', models.DateTimeField(blank=True, db_column='Fecha', null=True)),
                ('fecha_cierre', models.DateTimeField(blank=True, db_column='FechaCierre', null=True)),
                ('detalle', models.CharField(db_column='Detalle', default='', max_length=100)),
                ('nota', models.CharField(blank=True, db_column='Nota', default='', max_length=100, null=True)),
                ('tipo', models.CharField(blank=True, db_column='Tipo', default='', max_length=10, null=True)),
                ('apertura', models.DecimalField(db_column='Apertura', decimal_places=4, default=0, max_digits=19)),
                ('facturas', models.DecimalField(db_column='Facturas', decimal_places=4, default=0, max_digits=19)),
                ('ordenes', models.DecimalField(db_column='Ordenes', decimal_places=4, default=0, max_digits=19)),
                ('cobranzas', models.DecimalField(db_column='Cobranzas', decimal_places=4, default=0, max_digits=19)),
                ('devolucion_contado', models.DecimalField(db_column='DevolucionContado', decimal_places=4, default=0, max_digits=19)),
                ('devolucion_credito', models.DecimalField(db_column='DevolucionCredito', decimal_places=4, default=0, max_digits=19)),
                ('egresos', models.DecimalField(db_column='Egresos', decimal_places=4, default=0, max_digits=19)),
                ('creditos', models.DecimalField(db_column='Creditos', decimal_places=4, default=0, max_digits=19)),
                ('tarjetas', models.DecimalField(db_column='Tarjetas', decimal_places=4, default=0, max_digits=19)),
                ('transferencias', models.DecimalField(db_column='Transferencias', decimal_places=4, default=0, max_digits=19)),
                ('efectivo', models.DecimalField(db_column='Efectivo', decimal_places=4, default=0, max_digits=19)),
                ('total_ventas', models.DecimalField(db_column='TotalVentas', decimal_places=4, default=0, max_digits=19)),
                ('total_contado', models.DecimalField(db_column='TotalContado', decimal_places=4, default=0, max_digits=19)),
                ('total_credito', models.DecimalField(db_column='TotalCredito', decimal_places=4, default=0, max_digits=19)),
                ('estado', models.CharField(blank=True, db_column='Estado', default='', max_length=10, null=True)),
                ('total', models.DecimalField(db_column='Total', decimal_places=4, default=0, max_digits=19)),
                ('anulado', models.BooleanField(db_column='Anulado', default=False)),
                ('creadopor', models.CharField(blank=True, db_column='CreadoPor', default='', max_length=15, null=True)),
                ('creadodate', models.DateTimeField(auto_now_add=True, db_column='CreadoDate', null=True)),
                ('anuladopor', models.CharField(blank=True, db_column='AnuladoPor', default='', max_length=15, null=True)),
                ('anuladodate', models.DateTimeField(blank=True, db_column='AnuladoDate', null=True)),
                ('anuladonota', models.CharField(blank=True, db_column='AnuladoNota', default='', editable=False, max_length=1024, null=True)),
                ('sucursalid', models.CharField(blank=True, db_column='SucursalID', default='', editable=False, max_length=2, null=True)),
                ('pcid', models.CharField(blank=True, db_column='PcID', default='', editable=False, max_length=50, null=True)),
                ('ingresoid', models.CharField(blank=True, db_column='IngresoID', default='', max_length=10, null=True)),
                ('asientoid', models.CharField(blank=True, db_column='AsientoID', default='', max_length=10, null=True)),
            ],
            options={
                'verbose_name': 'Cierre de caja',
                'verbose_name_plural': 'Cierres de cajas',
                'db_table': 'POS_CIERRE',
                'managed': False,
            },
        ),
    ]
