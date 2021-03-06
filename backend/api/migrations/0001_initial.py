# Generated by Django 3.0.3 on 2020-06-13 20:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeVirtualModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date creation')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Date de mise ajour')),
                ('deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Date de suppression')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('timevirtualmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.TimeVirtualModel')),
                ('nom', models.CharField(blank=True, max_length=50, null=True)),
                ('prenom', models.CharField(blank=True, max_length=80, null=True)),
                ('dateAdhesion', models.DateField(auto_now=True, null=True)),
                ('dateNaissance', models.DateField(blank=True, null=True)),
                ('lieuNaissance', models.CharField(blank=True, max_length=150, null=True)),
                ('sexe', models.CharField(blank=True, max_length=10, null=True)),
                ('contact', models.CharField(blank=True, max_length=20, null=True)),
                ('adresse', models.CharField(blank=True, max_length=150, null=True)),
                ('profession', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.CharField(blank=True, max_length=150, null=True)),
            ],
            bases=('api.timevirtualmodel',),
        ),
        migrations.CreateModel(
            name='CreditEpargne',
            fields=[
                ('timevirtualmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.TimeVirtualModel')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('numero', models.CharField(blank=True, max_length=50, null=True)),
                ('nature_taux', models.CharField(blank=True, max_length=50, null=True)),
                ('taux_interet', models.FloatField(blank=True, null=True)),
                ('frais_dossier', models.FloatField(blank=True, null=True)),
                ('frais_gestion', models.FloatField(blank=True, null=True)),
                ('frais_assurance', models.FloatField(blank=True, null=True)),
                ('nbe_echeances', models.IntegerField(blank=True, null=True, verbose_name="nombre d'escheances")),
                ('duree_echeance', models.CharField(blank=True, max_length=150, null=True, verbose_name='Année/Mois/Jours')),
                ('nantissement', models.FloatField(blank=True, null=True)),
                ('montant', models.FloatField(blank=True, null=True)),
                ('date_limite', models.DateField(blank=True, null=True)),
                ('montant_rembourse', models.FloatField(blank=True, null=True, verbose_name='somme deja remboursé')),
                ('reste_a_rembourser', models.FloatField(blank=True, null=True, verbose_name='reste à rembourser')),
                ('rembourse', models.NullBooleanField(default=False)),
                ('prochaine_echeance', models.IntegerField(blank=True, null=True)),
                ('montant_prevue', models.FloatField(blank=True, null=True)),
                ('date_prevue', models.DateField(blank=True, null=True)),
                ('agent_de_credit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('api.timevirtualmodel',),
        ),
        migrations.CreateModel(
            name='CreditTontine',
            fields=[
                ('timevirtualmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.TimeVirtualModel')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('numero', models.CharField(blank=True, max_length=50, null=True)),
                ('nature_taux', models.CharField(blank=True, max_length=50, null=True)),
                ('taux_interet', models.FloatField(blank=True, null=True)),
                ('frais_dossier', models.FloatField(blank=True, null=True)),
                ('frais_gestion', models.FloatField(blank=True, null=True)),
                ('frais_assurance', models.FloatField(blank=True, null=True)),
                ('nbe_echeances', models.IntegerField(blank=True, null=True, verbose_name="nombre d'escheances")),
                ('duree_echeance', models.CharField(blank=True, max_length=150, null=True, verbose_name='Année/Mois/Jours')),
                ('nantissement', models.FloatField(blank=True, null=True)),
                ('montant', models.FloatField(blank=True, null=True)),
                ('date_limite', models.DateField(blank=True, null=True)),
                ('montant_rembourse', models.FloatField(blank=True, null=True, verbose_name='somme deja remboursé')),
                ('reste_a_rembourser', models.FloatField(blank=True, null=True, verbose_name='reste à rembourser')),
                ('rembourse', models.NullBooleanField(default=False)),
                ('prochaine_echeance', models.IntegerField(blank=True, null=True)),
                ('montant_prevue', models.FloatField(blank=True, null=True)),
                ('date_prevue', models.DateField(blank=True, null=True)),
                ('agent_de_credit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('api.timevirtualmodel',),
        ),
        migrations.CreateModel(
            name='DepotEpargne',
            fields=[
                ('timevirtualmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.TimeVirtualModel')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('deposeur', models.CharField(blank=True, max_length=50, null=True)),
                ('montant', models.FloatField(blank=True, null=True)),
                ('nouveau_solde', models.FloatField(blank=True, null=True)),
            ],
            bases=('api.timevirtualmodel',),
        ),
        migrations.CreateModel(
            name='RetraitEpargne',
            fields=[
                ('timevirtualmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.TimeVirtualModel')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('receveur', models.CharField(blank=True, max_length=50, null=True)),
                ('montant', models.FloatField(blank=True, null=True)),
                ('nouveau_solde', models.FloatField(blank=True, null=True)),
            ],
            bases=('api.timevirtualmodel',),
        ),
        migrations.CreateModel(
            name='TypeCreditEpargne',
            fields=[
                ('timevirtualmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.TimeVirtualModel')),
                ('libelle', models.CharField(blank=True, max_length=50, null=True)),
            ],
            bases=('api.timevirtualmodel',),
        ),
        migrations.CreateModel(
            name='TypeCreditTontine',
            fields=[
                ('timevirtualmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.TimeVirtualModel')),
                ('libelle', models.CharField(blank=True, max_length=50, null=True)),
            ],
            bases=('api.timevirtualmodel',),
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('timevirtualmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.TimeVirtualModel')),
                ('code', models.CharField(blank=True, max_length=50, null=True)),
                ('libelle', models.CharField(blank=True, max_length=50, null=True)),
            ],
            bases=('api.timevirtualmodel',),
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('timevirtualmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.TimeVirtualModel')),
                ('nom', models.CharField(blank=True, max_length=50, null=True)),
                ('prenom', models.CharField(blank=True, max_length=50, null=True)),
                ('addresse', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('contact', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('genre', models.CharField(blank=True, choices=[('M', 'Masculin'), ('F', 'Feminin')], max_length=1, null=True)),
                ('profil', models.CharField(blank=True, choices=[('AGT', 'Agent de Terrain'), ('SEC', 'Secretaire'), ('CAS', 'Caissier'), ('CPT', 'Comptable'), ('CTL', 'Controleur')], max_length=5, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='User/Profile', verbose_name='Image de profile')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('api.timevirtualmodel',),
        ),
        migrations.CreateModel(
            name='Tontine',
            fields=[
                ('timevirtualmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.TimeVirtualModel')),
                ('numero', models.CharField(blank=True, max_length=50, null=True)),
                ('dateCreation', models.DateField(auto_now_add=True, null=True)),
                ('miseActuelle', models.FloatField(blank=True, null=True)),
                ('miseProchaine', models.FloatField(blank=True, null=True)),
                ('solde', models.FloatField(blank=True, default=0, null=True)),
                ('clientTont', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Client')),
            ],
            bases=('api.timevirtualmodel',),
        ),
        migrations.CreateModel(
            name='RetraitTontine',
            fields=[
                ('timevirtualmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.TimeVirtualModel')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('montant', models.FloatField(blank=True, null=True)),
                ('nouveauSolde', models.FloatField(blank=True, null=True)),
                ('compteTontine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Tontine')),
            ],
            bases=('api.timevirtualmodel',),
        ),
        migrations.CreateModel(
            name='RembourssementTontine',
            fields=[
                ('timevirtualmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.TimeVirtualModel')),
                ('montant', models.FloatField(blank=True, null=True)),
                ('interet', models.FloatField(blank=True, null=True)),
                ('penalites', models.FloatField(blank=True, default=0.0, null=True)),
                ('remboursseur', models.CharField(blank=True, max_length=50, null=True)),
                ('credit_tontine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.CreditTontine')),
            ],
            bases=('api.timevirtualmodel',),
        ),
        migrations.CreateModel(
            name='RembourssementEpargne',
            fields=[
                ('timevirtualmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.TimeVirtualModel')),
                ('montant', models.FloatField(blank=True, null=True)),
                ('interet', models.FloatField(blank=True, null=True)),
                ('penalites', models.FloatField(blank=True, default=0.0, null=True)),
                ('remboursseur', models.CharField(blank=True, max_length=50, null=True)),
                ('credit_epargne', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.CreditEpargne')),
            ],
            bases=('api.timevirtualmodel',),
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('timevirtualmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.TimeVirtualModel')),
                ('date', models.DateField(blank=True, null=True, verbose_name="Date de l'operation")),
                ('typeOperationp', models.CharField(blank=True, choices=[('DEP', 'Depot'), ('RET', 'Retrait')], max_length=5, null=True)),
                ('libelle', models.CharField(max_length=50)),
                ('montant', models.FloatField(blank=True, null=True)),
                ('operateur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Operateur', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('api.timevirtualmodel',),
        ),
        migrations.CreateModel(
            name='Mouvement',
            fields=[
                ('timevirtualmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.TimeVirtualModel')),
                ('date', models.DateField(blank=True, null=True)),
                ('libelle', models.CharField(blank=True, max_length=50, null=True)),
                ('depot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.DepotEpargne')),
                ('retrait', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.RetraitEpargne')),
            ],
            bases=('api.timevirtualmodel',),
        ),
        migrations.CreateModel(
            name='MoisCotisation',
            fields=[
                ('timevirtualmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.TimeVirtualModel')),
                ('mise', models.FloatField(blank=True, null=True)),
                ('dateDebut', models.DateField(blank=True, null=True)),
                ('dateFin', models.DateField(blank=True, null=True)),
                ('montantMax', models.FloatField(blank=True, null=True)),
                ('montantActuel', models.FloatField(blank=True, null=True)),
                ('compteTontine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Tontine')),
            ],
            bases=('api.timevirtualmodel',),
        ),
        migrations.CreateModel(
            name='Epargne',
            fields=[
                ('timevirtualmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.TimeVirtualModel')),
                ('numero', models.CharField(blank=True, max_length=50, null=True)),
                ('typeCompte', models.CharField(blank=True, choices=[('PHY', 'Physique'), ('MOR', 'Morale')], default='PHY', max_length=5, null=True)),
                ('dateCreation', models.DateField(auto_now_add=True, null=True)),
                ('bloque', models.BooleanField(blank=True, default=None, null=True)),
                ('dateLimiteBlocage', models.DateField(blank=True, null=True)),
                ('droitAdhsion', models.FloatField(blank=True, null=True)),
                ('partSocial', models.FloatField(blank=True, null=True)),
                ('soldeInitial', models.FloatField(blank=True, null=True)),
                ('soldeBloqué', models.FloatField(blank=True, null=True)),
                ('solde', models.FloatField(blank=True, default=0, null=True)),
                ('clientEp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Client')),
            ],
            bases=('api.timevirtualmodel',),
        ),
        migrations.AddField(
            model_name='credittontine',
            name='compte_tontine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Tontine', verbose_name='Compte Tontine'),
        ),
        migrations.AddField(
            model_name='credittontine',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.TypeCreditEpargne', verbose_name='Type credit Epargne'),
        ),
        migrations.AddField(
            model_name='creditepargne',
            name='compte_epargne',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Epargne', verbose_name='Compte Epargne'),
        ),
        migrations.AddField(
            model_name='creditepargne',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.TypeCreditEpargne', verbose_name='Type credit Epargne'),
        ),
        migrations.CreateModel(
            name='Cotisation',
            fields=[
                ('timevirtualmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.TimeVirtualModel')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('montant', models.FloatField(blank=True, null=True)),
                ('mois', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.MoisCotisation')),
            ],
            bases=('api.timevirtualmodel',),
        ),
        migrations.CreateModel(
            name='CompteComptable',
            fields=[
                ('timevirtualmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.TimeVirtualModel')),
                ('code', models.CharField(blank=True, max_length=50, null=True)),
                ('numero', models.CharField(blank=True, max_length=50, null=True)),
                ('groupe', models.CharField(blank=True, max_length=50, null=True)),
                ('classe', models.IntegerField(blank=True, null=True)),
                ('statut', models.CharField(blank=True, max_length=50, null=True)),
                ('montantStatut', models.FloatField(blank=True, null=True)),
                ('createur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('api.timevirtualmodel',),
        ),
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('timevirtualmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.TimeVirtualModel')),
                ('date', models.DateField(blank=True, null=True)),
                ('montant', models.FloatField(blank=True, null=True)),
                ('CpTontine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Tontine')),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('api.timevirtualmodel',),
        ),
        migrations.AddField(
            model_name='client',
            name='zoneClt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Zone', verbose_name='zone'),
        ),
        migrations.CreateModel(
            name='Amortissement',
            fields=[
                ('timevirtualmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.TimeVirtualModel')),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('mensualite_due', models.FloatField(blank=True, null=True)),
                ('interet_mensuel_du', models.FloatField(blank=True, null=True)),
                ('capital_mensuel_du', models.FloatField(blank=True, null=True)),
                ('solde_capital_due', models.FloatField(blank=True, null=True)),
                ('solde_mensualite_due', models.FloatField(blank=True, null=True)),
                ('rembourse', models.BooleanField(blank=True, default=False, null=True)),
                ('date_remboursement', models.DateField(blank=True, null=True)),
                ('credit_epargne', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.CreditEpargne')),
                ('credit_tontine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.CreditTontine')),
            ],
            bases=('api.timevirtualmodel',),
        ),
        migrations.CreateModel(
            name='Alimentation',
            fields=[
                ('timevirtualmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.TimeVirtualModel')),
                ('date', models.DateField(auto_now=True)),
                ('montant', models.FloatField(blank=True, null=True)),
                ('nbrb10000', models.IntegerField(blank=True, null=True, verbose_name='Nombre de billets de 10.000F')),
                ('nbrb5000', models.IntegerField(blank=True, null=True, verbose_name='Nombre de billets de 5.000F')),
                ('nbrb2000', models.IntegerField(blank=True, null=True, verbose_name='Nombre de billets de 2.000F')),
                ('nbrb1000', models.IntegerField(blank=True, null=True, verbose_name='Nombre de billets de 1.000F')),
                ('nbrb500', models.IntegerField(blank=True, null=True, verbose_name='Nombre de billets de 500F')),
                ('nbrp500', models.IntegerField(blank=True, null=True, verbose_name='Nombre de pieces de 500F')),
                ('nbrp250', models.IntegerField(blank=True, null=True, verbose_name='Nombre de pieces de 250F')),
                ('nbrp200', models.IntegerField(blank=True, null=True, verbose_name='Nombre de pieces de 200F')),
                ('nbrp100', models.IntegerField(blank=True, null=True, verbose_name='Nombre de pieces de 100F')),
                ('nbrp50', models.IntegerField(blank=True, null=True, verbose_name='Nombre de pieces de 50F')),
                ('nbrp25', models.IntegerField(blank=True, null=True, verbose_name='Nombre de pieces de 25F')),
                ('nbrp10', models.IntegerField(blank=True, null=True, verbose_name='Nombre de pieces de 10F')),
                ('nbrp5', models.IntegerField(blank=True, null=True, verbose_name='Nombre de pieces de 5F')),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Agent', to=settings.AUTH_USER_MODEL)),
                ('caissier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Caissier', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('api.timevirtualmodel',),
        ),
    ]
