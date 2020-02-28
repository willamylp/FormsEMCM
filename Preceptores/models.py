from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class Preceptores(models.Model):
    TURNO = (
        ('Matutino', 'MATUTINO'),
        ('Vespertino', 'VESPERTINO'),
        ('Noturno', 'NOTURNO')
    )
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

    BANCOS = (
        ('325', 'Órama DTVM S.A.'),
        ('356', 'ABN AMRO S.A'),
        ('332', 'Acesso Soluções de Pagamento S.A.'),
        ('654', 'BANCO A. J. RENNER S.A'),
        ('246', 'BANCO ABC ROMA S.A'),
        ('222', 'BANCO AGF BRASIL S. A.'),
        ('483', 'BANCO AGRIMISA S.A.'),
        ('217', 'BANCO AGROINVEST S.A'),
        ('025', 'BANCO ALFA S/A'),
        ('215', 'BANCO AMERICA DO SUL S.A'),
        ('621', 'BANCO APLICAP S.A.'),
        ('625', 'BANCO ARAUCARIA S.A'),
        ('213', 'BANCO ARBI S.A'),
        ('648', 'BANCO ATLANTIS S.A'),
        ('201', 'BANCO AUGUSTA INDUSTRIA E COMERCIAL S.A'),
        ('394', 'BANCO B.M.C. S.A'),
        ('318', 'BANCO B.M.G. S.A'),
        ('116', 'BANCO B.N.L DO BRASIL S.A'),
        ('239', 'BANCO BANCRED S.A'),
        ('230', 'BANCO BANDEIRANTES S.A'),
        ('752', 'BANCO BANQUE NATIONALE DE PARIS BRASIL S'),
        ('107', 'BANCO BBM S.A'),
        ('267', 'BANCO BBM-COM.C.IMOB.CFI S.A.'),
        ('231', 'BANCO BOAVISTA S.A'),
        ('262', 'BANCO BOREAL S.A'),
        ('351', 'BANCO BOZANO SIMONSEN S.A'),
        ('225', 'BANCO BRASCAN S.A'),
        ('282', 'BANCO BRASILEIRO COMERCIAL'),
        ('501', 'BANCO BRASILEIRO IRAQUIANO S.A.'),
        ('168', 'BANCO C.C.F. BRASIL S.A'),
        ('336', 'BANCO C6 S.A.'),
        ('263', 'BANCO CACIQUE'),
        ('236', 'BANCO CAMBIAL S.A'),
        ('266', 'BANCO CEDULA S.A'),
        ('002', 'BANCO CENTRAL DO BRASIL'),
        ('244', 'BANCO CIDADE S.A'),
        ('713', 'BANCO CINDAM S.A'),
        ('241', 'BANCO CLASSICO S.A'),
        ('308', 'BANCO COMERCIAL BANCESA S.A.'),
        ('730', 'BANCO COMERCIAL PARAGUAYO S.A'),
        ('753', 'BANCO COMERCIAL URUGUAI S.A.'),
        ('109', 'BANCO CREDIBANCO S.A'),
        ('721', 'BANCO CREDIBEL S.A'),
        ('295', 'BANCO CREDIPLAN S.A'),
        ('220', 'BANCO CREFISUL'),
        ('628', 'BANCO CRITERIUM S.A'),
        ('229', 'BANCO CRUZEIRO S.A'),
        ('003', 'BANCO DA AMAZONIA S.A'),
        ('707', 'BANCO DAYCOVAL S.A'),
        ('479', 'BANCO DE BOSTON S.A'),
        ('219', 'BANCO DE CREDITO DE SAO PAULO S.A'),
        ('640', 'BANCO DE CREDITO METROPOLITANO S.A'),
        ('291', 'BANCO DE CREDITO NACIONAL S.A'),
        ('240', 'BANCO DE CREDITO REAL DE MINAS GERAIS S.'),
        ('022', 'BANCO DE CREDITO REAL DE MINAS GERAIS SA'),
        ('300', 'BANCO DE LA NACION ARGENTINA S.A'),
        ('627', 'BANCO DESTAK S.A'),
        ('214', 'BANCO DIBENS S.A'),
        ('649', 'BANCO DIMENSAO S.A'),
        ('001', 'BANCO DO BRASIL'),
        ('034', 'BANCO DO ESADO DO AMAZONAS S.A'),
        ('028', 'BANCO DO ESTADO DA BAHIA S.A'),
        ('030', 'BANCO DO ESTADO DA PARAIBA S.A'),
        ('020', 'BANCO DO ESTADO DE ALAGOAS S.A'),
        ('031', 'BANCO DO ESTADO DE GOIAS S.A'),
        ('048', 'BANCO DO ESTADO DE MINAS GERAIS S.A'),
        ('024', 'BANCO DO ESTADO DE PERNAMBUCO'),
        ('059', 'BANCO DO ESTADO DE RONDONIA S.A'),
        ('645', 'BANCO DO ESTADO DE RORAIMA S.A'),
        ('027', 'BANCO DO ESTADO DE SANTA CATARINA S.A'),
        ('047', 'BANCO DO ESTADO DE SERGIPE S.A'),
        ('026', 'BANCO DO ESTADO DO ACRE S.A'),
        ('635', 'BANCO DO ESTADO DO AMAPA S.A'),
        ('035', 'BANCO DO ESTADO DO CEARA S.A'),
        ('021', 'BANCO DO ESTADO DO ESPIRITO SANTO S.A'),
        ('036', 'BANCO DO ESTADO DO MARANHAO S.A'),
        ('032', 'BANCO DO ESTADO DO MATO GROSSO S.A.'),
        ('037', 'BANCO DO ESTADO DO PARA S.A'),
        ('038', 'BANCO DO ESTADO DO PARANA S.A'),
        ('039', 'BANCO DO ESTADO DO PIAUI S.A'),
        ('029', 'BANCO DO ESTADO DO RIO DE JANEIRO S.A'),
        ('041', 'BANCO DO ESTADO DO RIO GRANDE DO SUL S.A'),
        ('004', 'BANCO DO NORDESTE DO BRASIL S.A'),
        ('302', 'BANCO DO PROGRESSO S.A'),
        ('622', 'BANCO DRACMA S.A'),
        ('743', 'BANCO EMBLEMA S.A'),
        ('245', 'BANCO EMPRESARIAL S.A'),
        ('242', 'BANCO EUROINVEST S.A'),
        ('641', 'BANCO EXCEL ECONOMICO S/A'),
        ('496', 'BANCO EXTERIOR DE ESPANA S.A'),
        ('265', 'BANCO FATOR S.A'),
        ('375', 'BANCO FENICIA S.A'),
        ('224', 'BANCO FIBRA S.A'),
        ('626', 'BANCO FICSA S.A'),
        ('725', 'BANCO FINABANCO S.A'),
        ('199', 'BANCO FINANCIAL PORTUGUES'),
        ('473', 'BANCO FINANCIAL PORTUGUES S.A'),
        ('252', 'BANCO FININVEST S.A'),
        ('728', 'BANCO FITAL S.A'),
        ('729', 'BANCO FONTE S.A'),
        ('434', 'BANCO FORTALEZA S.A'),
        ('346', 'BANCO FRANCES E BRASILEIRO S.A'),
        ('652', 'BANCO FRANCES E BRASILEIRO SA'),
        ('200', 'BANCO FRICRISA AXELRUD S.A'),
        ('505', 'BANCO GARANTIA S.A'),
        ('624', 'BANCO GENERAL MOTORS S.A'),
        ('353', 'BANCO GERAL DO COMERCIO S.A'),
        ('734', 'BANCO GERDAU S.A'),
        ('731', 'BANCO GNPP S.A.'),
        ('221', 'BANCO GRAPHUS S.A'),
        ('612', 'BANCO GUANABARA S.A'),
        ('256', 'BANCO GULVINVEST S.A'),
        ('303', 'BANCO HNF S.A.'),
        ('399', 'BANCO HSBC'),
        ('228', 'BANCO ICATU S.A'),
        ('258', 'BANCO INDUSCRED S.A'),
        ('604', 'BANCO INDUSTRIAL DO BRASIL S.A'),
        ('320', 'BANCO INDUSTRIAL E COMERCIAL'),
        ('653', 'BANCO INDUSVAL S.A'),
        ('166', 'BANCO INTER-ATLANTICO S.A'),
        ('630', 'BANCO INTERCAP S.A'),
        ('722', 'BANCO INTERIOR DE SAO PAULO S.A'),
        ('077', 'BANCO INTERMEDIUM'),
        ('616', 'BANCO INTERPACIFICO S.A'),
        ('232', 'BANCO INTERPART S.A'),
        ('223', 'BANCO INTERUNION S.A'),
        ('705', 'BANCO INVESTCORP S.A.'),
        ('249', 'BANCO INVESTCRED S.A'),
        ('617', 'BANCO INVESTOR S.A.'),
        ('499', 'BANCO IOCHPE S.A'),
        ('106', 'BANCO ITABANCO S.A.'),
        ('372', 'BANCO ITAMARATI S.A'),
        ('488', 'BANCO J. P. MORGAN S.A'),
        ('757', 'BANCO KEB DO BRASIL S.A.'),
        ('495', 'BANCO LA PROVINCIA DE BUENOS AIRES'),
        ('494', 'BANCO LA REP. ORIENTAL DEL URUGUAY'),
        ('234', 'BANCO LAVRA S.A.'),
        ('235', 'BANCO LIBERAL S.A'),
        ('600', 'BANCO LUSO BRASILEIRO S.A'),
        ('233', 'BANCO MAPPIN S.A'),
        ('647', 'BANCO MARKA S.A'),
        ('206', 'BANCO MARTINELLI S.A'),
        ('656', 'BANCO MATRIX S.A'),
        ('720', 'BANCO MAXINVEST S.A'),
        ('388', 'BANCO MERCANTIL DE DESCONTOS S/A'),
        ('392', 'BANCO MERCANTIL DE SAO PAULO S.A'),
        ('389', 'BANCO MERCANTIL DO BRASIL S.A'),
        ('008', 'BANCO MERIDIONAL DO BRASIL'),
        ('755', 'BANCO MERRILL LYNCH S.A'),
        ('466', 'BANCO MITSUBISHI BRASILEIRO S.A'),
        ('504', 'BANCO MULTIPLIC S.A'),
        ('007', 'BANCO NAC DESENV. ECO. SOCIAL S.A'),
        ('412', 'BANCO NACIONAL DA BAHIA S.A'),
        ('420', 'BANCO NACIONAL DO NORTE S.A'),
        ('415', 'BANCO NACIONAL S.A'),
        ('733', 'BANCO NACOES S.A.'),
        ('735', 'BANCO NEON'),
        ('165', 'BANCO NORCHEM S.A'),
        ('424', 'BANCO NOROESTE S.A'),
        ('247', 'BANCO OMEGA S.A'),
        ('608', 'BANCO OPEN S.A'),
        ('718', 'BANCO OPERADOR S.A'),
        ('212', 'BANCO ORIGINAL'),
        ('208', 'BANCO PACTUAL S.A'),
        ('623', 'BANCO PANAMERICANO S.A'),
        ('254', 'BANCO PARANA BANCO S.A'),
        ('602', 'BANCO PATENTE S.A'),
        ('611', 'BANCO PAULISTA S.A'),
        ('650', 'BANCO PEBB S.A'),
        ('613', 'BANCO PECUNIA S.A'),
        ('264', 'BANCO PERFORMANCE S.A'),
        ('277', 'BANCO PLANIBANC S.A'),
        ('304', 'BANCO PONTUAL S.A'),
        ('658', 'BANCO PORTO REAL S.A'),
        ('724', 'BANCO PORTO SEGURO S.A'),
        ('480', 'BANCO PORTUGUES DO ATLANTICO-BRASIL S.A'),
        ('732', 'BANCO PREMIER S.A.'),
        ('719', 'BANCO PRIMUS S.A'),
        ('638', 'BANCO PROSPER S.A'),
        ('275', 'BANCO REAL S.A'),
        ('633', 'BANCO REDIMENTO S.A'),
        ('216', 'BANCO REGIONAL MALCON S.A'),
        ('750', 'BANCO REPUBLIC NATIONAL OF NEW YORK (BRA'),
        ('453', 'BANCO RURAL S.A'),
        ('204', 'BANCO S.R.L S.A'),
        ('422', 'BANCO SAFRA'),
        ('502', 'BANCO SANTANDER S.A'),
        ('607', 'BANCO SANTOS NEVES S.A'),
        ('702', 'BANCO SANTOS S.A'),
        ('251', 'BANCO SAO JORGE S.A.'),
        ('250', 'BANCO SCHAHIN CURY S.A'),
        ('643', 'BANCO SEGMENTO S.A'),
        ('211', 'BANCO SISTEMA S.A'),
        ('637', 'BANCO SOFISA S.A'),
        ('366', 'BANCO SOGERAL S.A'),
        ('243', 'BANCO STOCK S.A'),
        ('347', 'BANCO SUDAMERIS BRASIL S.A'),
        ('205', 'BANCO SUL AMERICA S.A'),
        ('464', 'BANCO SUMITOMO BRASILEIRO S.A'),
        ('657', 'BANCO TECNICORP S.A'),
        ('618', 'BANCO TENDENCIA S.A'),
        ('456', 'BANCO TOKIO S.A'),
        ('634', 'BANCO TRIANGULO S.A'),
        ('493', 'BANCO UNION S.A.C.A'),
        ('736', 'BANCO UNITED S.A'),
        ('726', 'BANCO UNIVERSAL S.A'),
        ('610', 'BANCO V.R. S.A'),
        ('261', 'BANCO VARIG S.A'),
        ('715', 'BANCO VEGA S.A'),
        ('711', 'BANCO VETOR S.A.'),
        ('655', 'BANCO VOTORANTIM S.A.'),
        ('756', 'BANCOOB'),
        ('629', 'BANCORP BANCO COML. E. DE INVESTMENTO'),
        ('489', 'BANESTO BANCO URUGAUAY S.A'),
        ('184', 'BBA - CREDITANSTALT S.A'),
        ('740', 'BCN BARCLAYS'),
        ('294', 'BCR - BANCO DE CREDITO REAL S.A'),
        ('370', 'BEAL - BANCO EUROPEU PARA AMERICA LATINA'),
        ('601', 'BFC BANCO S.A.'),
        ('739', 'BGN'),
        ('639', 'BIG S.A. - BANCO IRMAOS GUIMARAES'),
        ('237', 'BRADESCO'),
        ('070', 'BRB - BANCO DE BRASÍLIA'),
        ('749', 'BRMSANTIL SA'),
        ('741', 'BRP'),
        ('218', 'BS2'),
        ('104', 'CAIXA ECONÔMICA FEDERAL'),
        ('151', 'CAIXA ECONOMICA DO ESTADO DE SAO PAULO'),
        ('153', 'CAIXA ECONOMICA DO ESTADO DO R.G.SUL'),
        ('498', 'CENTRO HISPANO BANCO'),
        ('376', 'CHASE MANHATTAN BANK S.A'),
        ('745', 'CITIBANK'),
        ('477', 'CITIBANK N.A'),
        ('175', 'CONTINENTAL BANCO S.A'),
        ('210', 'DEUTSCH SUDAMERIKANICHE BANK AG'),
        ('487', 'DEUTSCHE BANK S.A - BANCO ALEMAO'),
        ('751', 'DRESDNER BANK LATEINAMERIKA-BRASIL S/A'),
        ('742', 'EQUATORIAL'),
        ('492', 'INTERNATIONALE NEDERLANDEN BANK N.V.'),
        ('341', 'ITAÚ'),
        ('472', 'LLOYDS BANK PLC'),
        ('738', 'MARADA'),
        ('323', 'MercadoPago.com Representações Ltda.'),
        ('255', 'MILBANCO S.A.'),
        ('746', 'MODAL S.A'),
        ('148', 'MULTI BANCO S.A'),
        ('260', 'NUBANK'),
        ('290', 'PagSeguro Internet S.A.'),
        ('369', 'PONTUAL'),
        ('747', 'RAIBOBANK DO BRASIL'),
        ('033', 'SANTANDER'),
        ('748', 'SICREDI'),
        ('744', 'THE FIRST NATIONAL BANK OF BOSTON'),
        ('737', 'THECA'),
        ('409', 'UNIBANCO - UNIAO DOS BANCOS BRASILEIROS'),
        ('102', 'XP INVESTIMENTOS'),
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
        max_length=200,
        blank=False,
        choices=BANCOS,
        default=''
    )
    angencia = models.CharField(
        max_length=10,
        blank=False
    )
    conta = models.CharField(
        max_length=30,
        blank=False
    )
    
    # #-->>> DADOS PROFISSIONAIS
    # escolaridade = MultiSelectField(
    #     blank=False,
    #     choices=DADOS_PROFISSIONAIS,
    #     default=''
    # )

    #####
    num_edital = models.CharField(
        max_length=10,
        blank=False
    )
   
    def __str__(self):
        return self.nome

class Graduacao(models.Model):
    preceptores = models.ForeignKey(
        Preceptores,
        on_delete=models.CASCADE
    )
    curso = models.CharField(
        max_length=50, 
        blank=False
    )
    ano_termino = models.PositiveIntegerField(
        default=0, 
        blank=False,
        null=False,
        unique=True
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
    ano_termino = models.PositiveIntegerField(
        default=0, 
        blank=False,
        null=False,
        unique=True
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
    ano_termino = models.PositiveIntegerField(
        default=0, 
        blank=False,
        null=False,
        unique=True
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
    ano_termino = models.PositiveIntegerField(
        default=0, 
        blank=False,
        null=False,
        unique=True
    )
    instituicao = models.CharField(
        max_length=50,
        blank=False
    )
    def __str__(self):
        return self.area
    

class Vinculo_Profissional(models.Model):
    preceptores = models.ForeignKey(
        Preceptores,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
    

    

    
