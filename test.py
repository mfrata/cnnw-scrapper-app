# coding=utf-8
import time
from predictor.risk import predictRisk
from predictor.category import predictCategory
from predictor.entity import predictPeople, predictCompanies
from textmining import clearString

def test_performance(string_param):
    """
    Test the performance of the predict functions counting the time to performance
    the prediction
    ---
    args : String
    """
    for func in [predictRisk, predictCategory]:
        start = time.time()
        answer = func(string_param)
        print "predicted: "+answer
        end = time.time()
        print "time for first:{}".format(end - start)

        start = time.time()
        answer = func(string_param)
        print "predicted: "+answer
        end = time.time()
        print "time for second:{}".format(end - start)

        start = time.time()
        for x in range(1,10000):
            answer = func(string_param)
        end = time.time()
        print "time for 10000:{}".format(end - start)
    print "Number of characters : {}".format(len(string_param))


#Full json of a scrapped news
Modelo_STF = \
{"title": "STF irá discutir direito a diferenças de remuneração após a transposição de servidor celetista para RJU", "date": "Terça-feira, 04 de julho de 2017", "headline": "Ao decidir pela existência de repercussão geral, STF analisará recurso que discute se os servidores federais têm direito às diferenças relacionadas ao reajuste de 47,11% sobre a parcela denominada adiantamento do PCCS, após mudança de regime.", "link": "http://www.stf.jus.br/portal/cms/verNoticiaDetalhe.asp?idConteudo=348734", "body": ["\r\n\t\t", "O Supremo Tribunal Federal (STF) irá decidir se os servidores federais têm direito às diferenças relacionadas ao reajuste de 47,11% sobre a parcela denominada adiantamento do PCCS após a mudança do regime celetista para o estatutário. Em votação no Plenário Virtual, foi reconhecida a repercussão geral do Recurso Extraordinário (RE) 1023750, interposto pela União contra acórdão do Tribunal Regional Federal da 4ª Região (TRF-4), que julgou procedente o pagamento das diferenças após a transposição de servidores para o Regime Jurídico Único (RJU).", "No caso dos autos, a Justiça do Trabalho garantiu direito ao reajuste de 47,11% sobre parcela denominada adiantamento do PCCS, prevista no artigo 1º da Lei 7.686/1988, limitando sua execução à data em que o regime jurídico dos beneficiários passou de trabalhista para estatutário. Ao examinar a questão, o TRF-4 entendeu que, em razão da Lei 8.460/1992 (artigo 4º, inciso II), o direito às diferenças relativas ao adiantamento do PCCS cessa com a incorporação do abono aos vencimentos dos servidores. Entretanto, para evitar redução salarial, admitiu o pagamento aos servidores de eventual parcela que exceda o valor previsto nas novas tabelas, a título de vantagem pessoal, até que seja absorvida por reajustes posteriores (exceto reajustes gerais para reposição inflacionária).", "A União interpôs recurso extraordinário, argumentado quanto à necessidade de reformar o acórdão para que a Justiça Federal passe ao exame do mérito da questão, de forma independente, sem se submeter aos limites da decisão proferida pela Justiça do Trabalho, baseada nas normas da CLT.", "O relator original do processo, ministro Luís Roberto Barroso, propôs o não conhecimento do recurso, por entender que a questão não possui natureza constitucional e não tem repercussão geral. Em seu entendimento, ao contrário do sustentado pela União, o acórdão do TRF-4 não apresenta a decisão trabalhista como único fundamento, nem se ampara em normas da CLT para reconhecer o direito pleiteado. Dessa forma, para ele, eventual revisão do acórdão atacado demandaria a análise da legislação infraconstitucional que disciplinou a política remuneratória, o que é inviável em recurso extraordinário.", "Como o relator foi vencido na deliberação do Plenário Virtual, o processo será redistribuído, por sorteio, entre os ministros que divergiram ou não se manifestaram nessa votação, nos termos do artigo 324, parágrafo 3º, do Regimento Interno do STF."]}

#cleaning news body
other_text = clearString(" ".join(Modelo_STF['body']))

#news text from the data used to train the module
text_predict = 'A mesma indistin\xc3\xa7\xc3\xa3o por vezes ocorre entre a propriedade da empresa e a propriedade de seus acionistas controladores.\nTodavia, o emprego das aeronaves n\xc3\xa3o consta como benef\xc3\xadcio indireto -ou seja, Joesley faz uso da propriedade da empresa para fins absolutamente particulares e alheios aos interesses dos demais acionistas.\nNoticiou-se que Joesley, ap\xc3\xb3s a divulga\xc3\xa7\xc3\xa3o do escandaloso acordo de dela\xc3\xa7\xc3\xa3o premiada, mudou-se com sua fam\xc3\xadlia para os Estados Unidos em "seu jato", fato que, ali\xc3\xa1s, causou enor'


test_performance(other_text)
