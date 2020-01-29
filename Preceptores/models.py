from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class Preceptores(models.Model):


# SESAP – HOSPITAL REGIONAL DE CAICÓ
# SESAP – HOSPITAL REGIONAL MARIANO COELHO
# SESAP – HOSPITAL GISELDA TRIGUEIRO
# SESAP – HOSPITAL MONSENHOR WALFREDO GURGEL
# SESAP – OUTRO: __________________________
# SMS - CAICÓ
# SMS - CURRAIS NOVOS
# SMS - SANTA CRUZ
# OUTRO: ___________________________


    
    ESTADOS = (
        ('Acre', 'AC'),
        ('Alagoas', 'AL'),
        ('Amapá', 'AP'),
        ('Amazonas', 'AM'),
        ('Bahia', 'BA'),
        ('Ceará', 'CE'),
        ('Distrito Federal', 'DF'),
        ('Espírito Santo', 'ES'),
        ('Goiás', 'GO'),
        ('Maranhão', 'MA'),
        ('Mato Grosso', 'MT'),
        ('Mato Grosso do Sul', 'MS'),
        ('Minas Gerais', 'MG'),
        ('Pará', 'PA'),
        ('Paraíba', 'PB'),
        ('Paraná', 'PR'),
        ('Pernambuco', 'PE'),
        ('Piauí', 'PI'),
        ('Rio de Janeiro', 'RJ'),
        ('Rio Grande do Norte', 'RN'),
        ('Rio Grande do Sul', 'RS'),
        ('Rondônia', 'RO'),
        ('Roraima', 'RR'),
        ('Santa Catarina', 'SC'),
        ('São Paulo', 'SP'),
        ('Sergipe', 'SE'),
        ('Tocantins', 'TO'),
    )
    DADOS_PROFISSIONAIS = (
        ('Graduação', 'GRADUACAO'),
        ('Residência', 'RESIDENCIA'),
        ('Mestrado', 'MESTRADO'),
        ('Doutorado', 'DOUTORADO')

    )

    #-->>> INFORMAÇÕES PESSOAIS
    nome = models.CharField(
        max_length=100, 
        blank=False
    )
    CPF = models.CharField(
        max_length=15,
        blank=False,
        null=False,
        unique=True
    )
    CRM_RN = models.PositiveIntegerField(
        default=0, 
        blank=False,
        null=False,
        unique=True
    )
    data_nascimento = models.DateField(
        blank=False
    )
    RG = models.CharField(
        max_length=10,
        blank=False,
        null=False,
        unique=True
    )
    emissor_RG = models.CharField(
        max_length=50,
        blank=False
    )
    UF_RG = models.CharField(
        max_length=30,
        choices=ESTADOS,
        default=''
    )
    # > ENDEREÇO
    endereço = models.CharField(
        max_length=100,
        blank=False
    )
    complemento = models.CharField(
        max_length=100,
        blank=False
    )
    bairro = models.CharField(
        max_length=100, blank=False
    )
    CEP = models.CharField(
        max_length=10,
        blank=False
    )
    cidade = models.CharField(
        max_length=100,
        blank=False
    )
    UF_CEP = models.CharField(
        max_length=30,
        choices=ESTADOS,
        default=''
    )
    # > CONTATO
    telefone = models.CharField(
        max_length=20,
        blank=False
    )
    celular_1 = models.CharField(
        max_length=20,
        blank=True
    )
    celular_2 = models.CharField(
        max_length=20,
        blank=True
    )
    email = models.CharField(
        max_length=100,
        blank=False
    )

    #-->>> DADOS BANCÁRIOS
    banco = models.CharField(
        max_length=50,
        blank=False
    )
    angencia = models.CharField(
        max_length=10,
        blank=False
    )
    conta = models.CharField(
        max_length=30,
        blank=False
    )
    
    #-->>> DADOS PROFISSIONAIS
    escolaridade = MultiSelectField(
        blank=False,
        choices=DADOS_PROFISSIONAIS,
        default=''
    )
   
    def __str__(self):
        return self.nome

    #####
    num_edital = models.CharField(
        max_length=10,
        blank=False
    )

class Graduacao(models.Model):
    preceptores = models.ForeignKey(
        Preceptores,
        on_delete=models.CASCADE
    )
    curso = models.CharField(
        max_length=50, 
        blank=False
    )
    data_termino = models.DateField(
        blank=False
    )
    instituicao = models.CharField(
        max_length=50,
        blank=False
    )
    
    def __str__(self):
        return self.curso

class Residencia(models.Model):
    preceptores = models.ForeignKey(
        Preceptores,
        on_delete=models.CASCADE
    )
    area = models.CharField(
        max_length=50, 
        blank=False
    )
    data_termino = models.DateField(
        blank=False
    )
    instituicao = models.CharField(
        max_length=50,
        blank=False
    )
    def __str__(self):
        return self.area

class Mestrado(models.Model):
    preceptores = models.ForeignKey(
        Preceptores,
        on_delete=models.CASCADE
    )
    area = models.CharField(
        max_length=50, 
        blank=False
    )
    data_termino = models.DateField(
        blank=False
    )
    instituicao = models.CharField(
        max_length=50,
        blank=False
    )
    def __str__(self):
        return self.area

class Doutorado(models.Model):
    preceptores = models.ForeignKey(
        Preceptores,
        on_delete=models.CASCADE
    )
    area = models.CharField(
        max_length=50, 
        blank=False
    )
    data_termino = models.DateField(
        blank=False
    )
    instituicao = models.CharField(
        max_length=50,
        blank=False
    )
    def __str__(self):
        return self.area
    

    
    
