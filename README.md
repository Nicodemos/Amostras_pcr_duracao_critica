
# Este Script Identifica amostras PCR perdidas

    Amostras processadas na unidade de apoio ao diagnóstico da COVID19 tem tempo máximo
    de liberarção de 24 horas. A unidade tem capacidade para processar 5 mil exames dia.
    Muitos processos nos laboratórios ocorrem de forma manual, e há ocorrências de amostras 
    que demoram mais que 24 horas. O processo para identificar essas amostras leva muito tempo
    se feito de forma manual pelos Analistas de laboratório.


    Esse script gera uma planilha no diretório: "\\ceara-fs\Ceara\Central Analítica\Biologia Molecular\Room3-record\S3. Supervisão\TESTE_TI\amostras_duracao_critica.xlsx

    Os dados contidos na planilha são de amostras que já ultrapassaram 24 horas e não foram liberadas.
    O script é execultado diáriamente às 09 horas. 
    O script precisa de um arquivo csv exportado do bioluados e deve ser renomeado para: biolaudo_amostras.csv
    O Script precisa de outro arquivo da biologia molecular de amostras em reteste.
    O arquivo exportado do Biolaudos deve ser gerado pela opção de exportação: "Gerar CSV".
    O arquivo exportado deve estar no mesmo diretório do script python.
    O arquivo deve ser gerado com data de início 3 dias aterior a data atual de geração.

#### Dependências: pandas, openpyxl e datetime