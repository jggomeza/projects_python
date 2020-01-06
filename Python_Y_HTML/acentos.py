acentos = {'á':'&aacute;', 'é':'&eacute;', 'í':'&iacute;', 'ó':'&oacute;', 'ú':'&uacute;', 'ñ':'&ntilde;', 'Ñ':'&Ntilde;', 'ä':'&auml;', 'ë':'&euml;', 'ï':'&iuml;', 'ö':'&ouml;', 'ü':'&uuml;', 'Á':'&Aacute;', 'É':'&Aacute;', 'Í':'&Iacute;', 'Ó':'&Oacute;', 'Ú':'&Uacute;', 'Ä':'&Auml;', 'Ë':'&Euml;', 'Ï':'&Iuml;', 'Ö':'&Ouml;', 'Ü':'&Uuml;'}

frase = "á é í ó ú Á É Í Ó Ú ñ Ñ ä ë ï ö ü Ä Ë Ï Ö Ü"

for i in acentos:
	frase = frase.replace(str(i), str(acentos[i]))

print(frase)