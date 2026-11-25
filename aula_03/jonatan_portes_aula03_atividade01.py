fita_dna = str(input('Digite uma fita de DNA com 21 nucleotídeos: '))

fita_dna_padronizada = fita_dna.upper()
hemoglobina_a_padrao = "ATGGTGCACCTGACTCCTGAG"

comparacao_DNA = hemoglobina_a_padrao != fita_dna_padronizada

status = ["✅ Código PADRÃO / VÁLIDO", "⚠️ Código MODIFICADO / ALTERADO"]

#print(status[comparacao_DNA])

proteina = fita_dna_padronizada.replace('ATG', 'Met-').replace('GTG', 'Val-').replace('CAC', 'His-').replace('CTG', 'Leu-').replace('ACT', 'Thr-').replace('CCT', 'Pro-').replace('GAG', 'Glu')

#print(proteina)

aminoacido = str(input('Digite um aminoácido para busca (ex: Val ou His): '))
posicao_aminoacido = proteina.find(aminoacido)

print('--------------------------------------------------------------------------')
print(f'DNA de referência: {hemoglobina_a_padrao}')
print(f'DNA digitado: {fita_dna_padronizada}')
print(f'Tamanho da fita: {(len(fita_dna_padronizada))}')
print(f'Proteína traduzida: {proteina}')
print(f'Resultado do diagnóstico: {status[comparacao_DNA]}')
print(f'Posição do aminoácido pesquisado: {posicao_aminoacido}')
