from flask import request, jsonify
from bs4 import BeautifulSoup as bs
from sqlalchemy.inspection import inspect
from tqdm.notebook import trange

from src.database.cnae import Cnae
from src.database.empresa import Empresa
from src.database.estabele import Estabele
from src.database.motivosit import MotivoSit
from src.database.municipio import Municipio
from src.database.natju import NatJu
from src.database.pais import Pais
from src.database.quals import Quals
from src.database.simples import Simples
from src.database.socio import Socio
from src import app, db

import requests, os, re, json, zipfile
import dask.dataframe as dd


urlbase = "https://dadosabertos.rfb.gov.br/CNPJ/dados_abertos_cnpj/2024-08/"
dirpath = "downloads/" #a path precisa existir

'''
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm.notebook import tqdm, trange
import sqlalchemy as sa


def mapp(fn,data, workers=8):
  tasks=[]
  out = []
  with ThreadPoolExecutor(max_workers=workers) as tex:
    tasks=[tex.submit(fn,i) for i in data]
  for task in as_completed(tasks):
    out.append(task.result())
  return out


    
def upload(local, table, dcol):
    colunas=list(dcol.keys())
    with engine.connect() as c:
        c.execute(sa.text("DROP TABLE IF EXISTS \"" + table + "\""))
        block='default' if local.find('.zip') < 0 else None
        df = dd.read_csv(local, header=None, encoding='latin1', sep=";", decimal=",", names=colunas, dtype=dcol, blocksize=block)
    for n in trange(df.npartitions, desc=table):
        df.get_partition(n).compute().to_sql( name=table, con=engine, if_exists= 'append', chunksize=1000, index=False)
    with engine.connect() as c:
         c.execute(sa.text("CREATE INDEX IF NOT EXISTS idx_" + table + " ON \"" + table + "\" (\"" + df.columns[0] + "\")"))

def extract(flist,filtro):
    filenames=[]
    files=list(filter(lambda x: not x.find(filtro), dirlist))
    for filename in files:
            zip=zipfile.ZipFile(dirpath+filename)
            filenames.append(dirpath+zip.filelist[0].filename)
            zip.extractall(path=dirpath)
    return filenames

def remove(flist):
    for f in flist:
            os.remove(f)

def importdata():
    filelist = list( filter( lambda s: s.find(".")>0, [tag.attrs['href'] for tag in bs(requests.get(urlbase).content).find_all('a')]))
    urllist = [urlbase+f for f in filelist]
    res = mapp(downloader,urllist) if input("Tem certeza? S/N").upper() == "S" else "Cancelado"
    dirlist= os.listdir(dirpath)
    engine = sa.create_engine(uri_sqlite)
    engine.connect().close() #test

    local=dirpath+'Municipios.zip'
    dcol = {"CD_MUNICIPIO": "int","MUNICIPIO":"str"}
    table='MUNICIPIO'
    upload(local, table, dcol)

    local=dirpath+'Cnaes.zip'
    dcol = {"CNAE": "int","NM_CNAE":"str"}
    table='CNAE'
    upload(local, table, dcol)

    local=dirpath+'Paises.zip'
    dcol = {"CD_PAIS": "int","PAIS":"str"}
    table='PAIS'
    upload(local, table, dcol)

    local=dirpath+'Naturezas.zip'
    dcol={"CD_NAT_JURIDICA": "int","NAT_JURIDICA":"str"}
    table='NATJU'
    upload(local, table, dcol)

    local=dirpath+'Motivos.zip'
    dcols={"CD_MOTIVO_SIT_CADASTRO":"int","MOTIVO_SIT_CADASTRO":"str"}
    table='MOTIVOSIT'
    upload(local, table, dcol)


    local=dirpath+'Qualificacoes.zip'
    dcol={"CD_QUALS":"int","NM_QUALS":"str"}
    table='QUALS'
    upload(local, table, dcol)

    lista= extract(dirlist,"Simples")
    #simples (cerca de 9min)
    local=dirpath+'*.SIMPLES.*'
    dcol={"CNPJ_BASICO":"int","OP_SIMPLES":"str","DT_OP_SIMPLES":"int","DT_EXC_SIMPLES":"int","OP_MEI":"str","DT_OP_MEI":"int","DT_EXC_MEI":"int"}
    table='SIMPLES'
    upload(local, table, dcol)
    remove(lista)


    #%%time
    lista= extract(dirlist,"Empre")
    #empresa
    dcol = {"CNPJ_BASICO":"int", "RAZAO_SOCIAL":"str", "NAT_JURIDICA":"int", "QUAL_RESP":"int", "CAPITAL_SOCIAL":"float",
            "PORTE_EMPRESA":"Int64", "ENTE_FED_RESP":"str"}
    local=dirpath+'*.EMPRECSV'
    table='EMPRESA'
    upload(local, table, dcol)
    remove(lista)

    lista= extract(dirlist,"Socios")
    #socios
    dcol={"CNPJ_BASICO":"int","ID_TIPO_SOCIO":"int","NOME_OU_RAZAO_SOCIAL":"str","CNPJ_CPF":"str","QUALIF_SOCIO":"int",
            "DT_ENTRADA":"int","CD_PAIS":"Int64","REPR_LEGAL":"str","NM_REPR":"str","CD_QUALIF_REPR":"int","FAIXA_ETARIA":"int"}
    local=dirpath+'*.SOCIOCSV'
    table='SOCIO'
    upload(local, table, dcol)
    remove(lista)


    lista= extract(dirlist,"Estabelecimentos")
    #estabelecimentos
    dcol={"CNPJ_BASICO":"int", "CNPJ_ORDEM":"int", "CNPJ_DV":"int", "CD_MATRIZ_FILIAL":"int", "NM_FANTASIA":"str",
            "CD_SIT_CADASTRO":"int", "DT_SIT_CADASTRO":"int","MOTIVO_SIT_CADASTRO":"int","NM_CIDADE_EXT":"str",
            "CD_PAIS":"Int64","DT_INI":"int", "CNAE_PRINCIPAL":"str","CNAE_SECUNDARIO":"str",
            "TIP_LOGRADOURO":"str","LOGRADOURO":"str","NUMERO":"str","COMPLEMENTO":"str","BAIRRO":"str","CEP":"str","UF":"str",
            "MUNICIPIO":"int", "DDD_1":"str","TEL_1":"str","DDD_2":"str","TEL_2":"str","DDD_FAX":"str","FAX":"str",
            "EMAIL":"str","SIT_ESP":"str", "DT_SIT_ESP":"Int64"}
    local=dirpath+'*.ESTABELE'
    table='ESTABELE'
    upload(local, table, dcol)
    remove(lista)

    remove([dirpath+f for f in filter(lambda x: x.find(".zip") > 0,dirlist)]) if input("Tem certeza? S/N").upper() == "S" else "Cancelado"

    dirlist= os.listdir(dirpath)
    dirlist
'''
def get_table_structure( cls ):
    mapper = inspect( cls )
    structure = {
        'table_name': cls.__tablename__,
        'columns': {}
    }
    for column in mapper.columns:
        if(column.name not in ['id','created','updated']):
            match str(column.type)[:7]:
                case 'INTEGER':
                    structure['columns'][column.name] = 'int'
                case 'VARCHAR':
                    structure['columns'][column.name] = 'str'
                case _:
                    structure['columns'][column.name] = str(column.type)    
    return structure    

class Aquisition():

    def __init__(self) -> None:
        self.setEndPoints()

    def setEndPoints(self) -> None:
        app.add_url_rule('/api/getdata', view_func=self.getData, methods=['GET'])
        app.add_url_rule('/api/loaddata', view_func=self.loadData, methods=['GET'])

    def downloader(self, url):
        try:
            r = requests.get(url, stream=True)
            total = int(r.headers.get('content-length', 0))
            
            if "Content-Disposition" in r.headers.keys():
                fname = re.findall("filename=(.+)", r.headers["Content-Disposition"])[0]
            else:
                fname = os.path.basename(url)
            
            with open(os.path.join(dirpath, fname), 'wb') as file:
                bytes_downloaded = 0
                
                for data in r.iter_content(chunk_size=1024):
                    size = file.write(data)
                    bytes_downloaded += size          
        except Exception as inst:
            print(inst)  # Exibe a exceção
        finally:
            return [str(r.status_code), url]

    def getData(self):
        # Faz uma requisição para a URL e obtém o conteúdo
        response = requests.get(urlbase)
        content = response.content

        # Analisa o conteúdo HTML
        soup = bs(content, 'html.parser')

        # Extrai todos os links (<a>) e filtra aqueles que contêm um ponto (.)
        hrefs = [tag.attrs['href'] for tag in soup.find_all('a')]
        filelist = [href for href in hrefs if '.' in href and href.find('.') > 0]

        urllist = [urlbase+f for f in filelist]
        for arquivo in urllist:
            #arquivo = urllist[0]
            self.downloader(arquivo)
        return json.dumps(urllist), 200

    def loadData(self):
        local=dirpath+'Cnaes.zip'
        dcol = {"CD_MUNICIPIO": "int","MUNICIPIO":"str"}
        table='CNAE'
        jsonret = self.upload(local, table, dcol)
        return jsonret
    
    def upload(self, local, table, dcol):
        match table.upper():
            case 'CNAE': 
                tbl = Cnae
            case 'MUNICIPIO':
                tbl = Municipio
            case _:
                return jsonify({'message': 'Tabela nao esta especificada '+table }), 400
        colunas = get_table_structure( tbl )

        # Excluindo a tabela se já existir
        with db.engine.connect() as connection:
            connection.execute(f"DROP TABLE IF EXISTS \"{table}\"")

        # Lendo o arquivo CSV
        block = 'default' if local.find('.zip') < 0 else None
        df = dd.read_csv(local, header=None, encoding='latin1', sep=";", decimal=",", names=colunas, dtype=dcol, blocksize=block)

        # Inserindo dados na tabela
        for n in trange(df.npartitions, desc=table):
            # Computando a partição e inserindo os dados
            partition_df = df.get_partition(n).compute()
            partition_df.to_sql(name=table, con=db.engine, if_exists='append', chunksize=1000, index=False)

        # Criando um índice na tabela
        with db.engine.connect() as connection:
            connection.execute(f"CREATE INDEX IF NOT EXISTS idx_{table} ON \"{table}\" (\"{df.columns[0]}\"))")

        return jsonify({'message': 'Tabela importada com sucesso'+table }), 200