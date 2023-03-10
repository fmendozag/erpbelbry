# Generated by Django 2.1.15 on 2021-04-14 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SisDivisas',
            fields=[
                ('id', models.CharField(db_column='ID', editable=False, max_length=10, primary_key=True, serialize=False)),
                ('codigo', models.CharField(db_column='Código', max_length=15)),
                ('nombre', models.CharField(db_column='Nombre', max_length=50)),
                ('simbolo', models.CharField(blank=True, db_column='Símbolo', max_length=5, null=True)),
                ('base', models.BooleanField(db_column='Base', default=False)),
                ('cambio', models.DecimalField(blank=True, db_column='Cambio', decimal_places=6, max_digits=12, null=True)),
                ('nota', models.CharField(blank=True, db_column='Nota', max_length=1024, null=True)),
                ('anulado', models.BooleanField(db_column='Anulado', default=False)),
                ('creadopor', models.CharField(blank=True, db_column='CreadoPor', default='', editable=False, max_length=15, null=True)),
                ('creadodate', models.DateTimeField(blank=True, db_column='CreadoDate', editable=False, null=True)),
                ('editadopor', models.CharField(blank=True, db_column='EditadoPor', default='', editable=False, max_length=15, null=True)),
                ('editadodate', models.DateTimeField(blank=True, db_column='EditadoDate', editable=False, null=True)),
                ('sucursalid', models.CharField(blank=True, db_column='SucursalID', editable=False, max_length=2, null=True)),
                ('pcid', models.CharField(blank=True, db_column='PCID', default='', editable=False, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Divisa',
                'verbose_name_plural': 'Divisas',
                'db_table': 'SIS_DIVISAS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SisDivisiones',
            fields=[
                ('id', models.CharField(db_column='ID', editable=False, max_length=10, primary_key=True, serialize=False)),
                ('codigo', models.CharField(blank=True, db_column='Código', max_length=15, null=True)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=50, null=True)),
                ('gerente', models.CharField(blank=True, db_column='Gerente', max_length=50, null=True)),
                ('nota', models.CharField(blank=True, db_column='Nota', max_length=1024, null=True)),
                ('anulado', models.BooleanField(db_column='Anulado', default=False)),
                ('creadopor', models.CharField(blank=True, db_column='CreadoPor', editable=False, max_length=15, null=True)),
                ('creadodate', models.DateTimeField(auto_now_add=True, db_column='CreadoDate', null=True)),
                ('editadopor', models.CharField(blank=True, db_column='EditadoPor', editable=False, max_length=15, null=True)),
                ('editadodate', models.DateTimeField(auto_now=True, db_column='EditadoDate', null=True)),
                ('sucursal', models.CharField(blank=True, db_column='SucursalID', editable=False, max_length=2, null=True)),
                ('pcid', models.CharField(blank=True, db_column='PCID', editable=False, max_length=50, null=True)),
                ('ruta', models.CharField(blank=True, db_column='Ruta', editable=False, max_length=1024, null=True)),
                ('orden', models.CharField(blank=True, db_column='Orden', editable=False, max_length=1024, null=True)),
                ('tipo', models.CharField(blank=True, db_column='Tipo', max_length=10, null=True)),
                ('informal', models.BooleanField(db_column='Informal', default=False)),
                ('activatefe', models.BooleanField(db_column='ActivateFE', default=False)),
                ('activatend', models.BooleanField(db_column='ActivateND', default=False)),
                ('activategu', models.BooleanField(db_column='ActivateGU', default=False)),
                ('activatere', models.BooleanField(db_column='ActivateRE', default=False)),
                ('ambiente_sri', models.BooleanField(db_column='AmbienteSRI', default=False)),
                ('facturacion_automatica_sri', models.BooleanField(db_column='FacturaciónAutomaticaSRI', default=False)),
                ('nombre_comercial_sri', models.CharField(blank=True, db_column='NombreComercialSRI', max_length=200, null=True)),
                ('razon_social_sri', models.CharField(blank=True, db_column='RazonSocialSRI', max_length=200, null=True)),
                ('ruc_sri', models.CharField(blank=True, db_column='RucSRI', max_length=13, null=True)),
                ('direccion_matriz_sri', models.CharField(blank=True, db_column='DirecciónMatrizSRI', max_length=1024, null=True)),
                ('direccion_establecimiento_sri', models.CharField(blank=True, db_column='DirecciónEstablecimientoSRI', max_length=1024, null=True)),
                ('contribuyente_especial_sri', models.CharField(blank=True, db_column='ContribuyenteEspecialSRI', max_length=50, null=True)),
                ('path_logo', models.CharField(blank=True, db_column='PathLogo', max_length=1024, null=True)),
                ('path_certificado', models.CharField(blank=True, db_column='PathCertificado', max_length=1024, null=True)),
                ('password_certificado_sri', models.CharField(blank=True, db_column='PasswordCertificadoSRI', max_length=30, null=True)),
                ('path_xml_generados', models.CharField(blank=True, db_column='PathXMLGenerados', max_length=1024, null=True)),
                ('path_xml_autorizados', models.CharField(blank=True, db_column='PathXMLAutorizados', max_length=1024, null=True)),
                ('servidor_correo', models.CharField(blank=True, db_column='ServidorCorreo', max_length=30, null=True)),
                ('cuenta_correo', models.CharField(blank=True, db_column='CuentaCorreo', max_length=200, null=True)),
                ('password_correo', models.CharField(blank=True, db_column='PasswordCorreo', max_length=30, null=True)),
                ('puerto_correo', models.CharField(blank=True, db_column='PuertoCorreo', max_length=10, null=True)),
                ('activate_outlook', models.BooleanField(db_column='ActivateOutlook', default=False)),
                ('obligado_contabilidad', models.BooleanField(db_column='ObligadoContabilidad', default=False)),
                ('server_url', models.CharField(blank=True, db_column='ServerURL', max_length=200, null=True)),
                ('usuario_sri', models.CharField(blank=True, db_column='UsuarioSRI', max_length=50, null=True)),
                ('api_sri', models.CharField(blank=True, db_column='ApiSRI', max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Division',
                'verbose_name_plural': 'Divisiones',
                'db_table': 'SIS_DIVISIONES',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SisParametros',
            fields=[
                ('id', models.CharField(db_column='ID', editable=False, max_length=10, primary_key=True, serialize=False)),
                ('codigo', models.CharField(db_column='Código', max_length=50)),
                ('nombre', models.CharField(db_column='Nombre', max_length=50)),
                ('tipo', models.CharField(blank=True, db_column='Tipo', max_length=10, null=True)),
                ('valor', models.CharField(blank=True, db_column='Valor', max_length=100, null=True)),
                ('extradata', models.CharField(blank=True, db_column='ExtraData', max_length=1024, null=True)),
                ('anulado', models.BooleanField(db_column='Anulado', default=False)),
                ('ruta', models.CharField(blank=True, db_column='Ruta', max_length=1024, null=True)),
                ('orden', models.CharField(blank=True, db_column='Orden', max_length=1024, null=True)),
                ('creadopor', models.CharField(blank=True, db_column='CreadoPor', max_length=15, null=True)),
                ('creadodate', models.DateTimeField(blank=True, db_column='CreadoDate', null=True)),
                ('editadopor', models.CharField(blank=True, db_column='EditadoPor', max_length=15, null=True)),
                ('editadodate', models.DateTimeField(blank=True, db_column='EditadoDate', null=True)),
                ('sucursal', models.CharField(blank=True, db_column='SucursalID', max_length=2, null=True)),
                ('pcid', models.CharField(blank=True, db_column='PCID', max_length=50, null=True)),
                ('extra_sri', models.CharField(blank=True, db_column='ExtraSRI', max_length=50, null=True)),
                ('cod_extra_sri', models.CharField(blank=True, db_column='CodExtraSRI', max_length=15, null=True)),
            ],
            options={
                'verbose_name': 'Parametro',
                'verbose_name_plural': 'Parametros',
                'db_table': 'SIS_PARAMETROS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SisSucursales',
            fields=[
                ('id', models.CharField(db_column='ID', editable=False, max_length=10, primary_key=True, serialize=False)),
                ('codigo', models.CharField(db_column='Código', max_length=2)),
                ('nombre', models.CharField(db_column='Nombre', max_length=50)),
                ('nota', models.CharField(blank=True, db_column='Nota', max_length=1024, null=True)),
                ('anulado', models.BooleanField(db_column='Anulado', default=False)),
                ('creadopor', models.CharField(blank=True, db_column='CreadoPor', max_length=15, null=True)),
                ('editadopor', models.CharField(blank=True, db_column='EditadoPor', max_length=15, null=True)),
                ('creadodate', models.DateTimeField(blank=True, db_column='CreadoDate', null=True)),
                ('editadodate', models.DateTimeField(blank=True, db_column='EditadoDate', null=True)),
                ('sucursal', models.CharField(blank=True, db_column='SucursalID', max_length=2, null=True)),
                ('pcid', models.CharField(blank=True, db_column='PCID', max_length=50, null=True)),
                ('disponible', models.BooleanField(blank=True, db_column='Disponible', null=True)),
                ('serversql', models.CharField(blank=True, db_column='ServerSQL', max_length=50, null=True)),
                ('databasesql', models.CharField(blank=True, db_column='DataBaseSQL', max_length=50, null=True)),
                ('passwordsql', models.CharField(blank=True, db_column='PasswordSQL', max_length=50, null=True)),
                ('matriz', models.BooleanField(blank=True, db_column='Matriz', null=True)),
            ],
            options={
                'verbose_name': 'Sucursal',
                'verbose_name_plural': 'Sucursales',
                'db_table': 'SIS_SUCURSALES',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SisZonas',
            fields=[
                ('id', models.CharField(db_column='ID', editable=False, max_length=10, primary_key=True, serialize=False)),
                ('codigo', models.CharField(db_column='Código', max_length=15, unique=True)),
                ('nombre', models.CharField(db_column='Nombre', max_length=50)),
                ('tipo', models.CharField(blank=True, choices=[('PAIS      ', 'PAIS'), ('PROVINCIA ', 'PROVINCIA'), ('CIUDAD    ', 'CIUDAD'), ('CANTON    ', 'CANTON'), ('PARROQUIA ', 'PARROQUIA'), ('ZONAS     ', 'ZONA'), ('OTRO      ', 'OTRO')], db_column='Tipo', default='PAIS      ', max_length=10, null=True)),
                ('anulado', models.BooleanField(db_column='Anulado', default=False)),
                ('ruta', models.CharField(blank=True, db_column='Ruta', editable=False, max_length=1024, null=True)),
                ('orden', models.CharField(blank=True, db_column='Orden', editable=False, max_length=1024, null=True)),
                ('creadopor', models.CharField(blank=True, db_column='CreadoPor', editable=False, max_length=15, null=True)),
                ('creadodate', models.DateTimeField(auto_now_add=True, db_column='CreadoDate', null=True)),
                ('editadopor', models.CharField(blank=True, db_column='EditadoPor', editable=False, max_length=15, null=True)),
                ('editadodate', models.DateTimeField(auto_now=True, db_column='EditadoDate', null=True)),
                ('sucursal', models.CharField(blank=True, db_column='SucursalID', editable=False, max_length=2, null=True)),
                ('pcid', models.CharField(blank=True, db_column='PCID', editable=False, max_length=50, null=True)),
                ('sigla', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'verbose_name': 'Zona',
                'verbose_name_plural': 'Zonas',
                'db_table': 'SIS_ZONAS',
                'ordering': ['codigo'],
                'managed': False,
            },
        ),
    ]
