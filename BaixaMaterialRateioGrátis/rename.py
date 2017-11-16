# encoding: utf-8
import os

path = "/home/vitor/Material Concursos - Rateio Grátis/PRF 2016/Física Aplicada à Perícia de Acidentes Rodoviários/"

#Lista os arquivos do diretório e ordena em ordem alfabética
files = os.listdir(path)
files.sort()

file_names = []
with open("file_name.txt", "r") as file:
	for line in file:
		file_names.append(line)

bkp_names = files

#Mostra o nome atual do arquivo e o nome que receberá
i = 0
for file in files:
	print file + " -> " + file_names[i] 	
	i = i + 1
print("\n")

asw = raw_input("Continuar? Y - Sim ou N - Não: ")
#Renomeia os arquivos de acordo com os novos nomes mostrados
if asw == "Y" or asw == "y" or asw == "S" or asw == "s":
	i = 0
	for file in files:
		os.rename(os.path.join(path, file), os.path.join(path, str(file_names[i])))

		i = i + 1

#Adquire os nomes dos arquivos do diretório novamente e organiza em ordem alfabética
files = os.listdir(path)
files.sort()

#Oferece a opção de desfazer a renomeação de arquivos
confirm = raw_input("Digite Y para concluir ou N para desfazer: ")

if confirm == "N" or confirm == "n":
	j = 0
	for file in files:
		os.rename(os.path.join(path, file), os.path.join(path, bkp_names[j]))
		j = j + 1