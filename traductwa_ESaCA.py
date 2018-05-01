# coding=UTF-8
import re

with open('entrada.txt', 'r') as f:
    txt = f.read()

#Everybode is in replace
cita_libro_s = re.findall('''{{cita libro''', txt, re.I)
for cita_libro in cita_libro_s:
    txt = txt.replace(cita_libro, "{{ref-llibre")
cita_web_s = re.findall('''{{cita web''', txt, re.I)
for cita_web in cita_web_s:
    txt = txt.replace(cita_web, "{{ref-web")
cita_noticia_s = re.findall('''{{cita noticia''', txt, re.I)
for cita_noticia in cita_noticia_s:
    txt = txt.replace(cita_noticia, "{{ref-notícia")
cita_publicacion_s = re.findall('''{{cita publicación''', txt, re.I)
for cita_publicacion in cita_publicacion_s:
    txt = txt.replace(cita_publicacion, "{{ref-publicació")
titulo_s = re.findall('''\|\s*título''', txt)
for titulo in titulo_s:
    txt = txt.replace(titulo, "|títol")
capitulo_s = re.findall('''\|\s*capítulo''', txt)
for capitulo in capitulo_s:
    txt = txt.replace(capitulo, "|capítol")
publicacion_s = re.findall('''\|\s*publicación''', txt)
for publicacion in publicacion_s:
    txt = txt.replace(publicacion, "|publicació")
revista_s = re.findall('''\|\s*revista''', txt)
for revista in revista_s:
    txt = txt.replace(revista, "|publicació")
apellido_s = re.findall('''\|\s*apellido''', txt)
for apellido in apellido_s:
    txt = txt.replace(apellido, "|cognom")
nombre_s = re.findall('''\|\s*nombre''', txt)
for nombre in nombre_s:
    txt = txt.replace(nombre, "|nom")
ubicacion_s = re.findall('''\|\s*ubicación''', txt)
for ubicacion in ubicacion_s:
    txt = txt.replace(ubicacion, "|lloc")
fechaacceso_s = re.findall('''\|\s*fechaacceso''', txt)
for fechaacceso in fechaacceso_s:
    txt = txt.replace(fechaacceso, "|consulta")
fecha_s = re.findall('''\|\s*fecha''', txt)
for fecha in fecha_s:
    txt = txt.replace(, "|data")
sitioweb_s = re.findall('''\|\s*sitioweb''', txt)
for sitioweb in sitioweb_s:
    txt = txt.replace(sitioweb, "|obra")
anno_s = re.findall('''\|\s*año''', txt)
for anno in anno_s:
    txt = txt.replace(anno, "|any")
edicion_s = re.findall('''\|\s*edición''', txt)
for edicion in edicion_s:
    txt = txt.replace(edicion, "|edició")
paginas_s = re.findall('''\|\s*páginas''', txt)
for paginas in paginas_s:
    txt = txt.replace(paginas, "|pàgines")
periodico_s = re.findall('''\|\s*periódico''', txt)
for periodico in periodico_s:
    txt = txt.replace(periodico, "|obra")
agencia_s = re.findall('''\|\s*agencia''', txt)
for agencia in agencia_s:
    txt = txt.replace(agencia, "|agència")
volumen_s = re.findall('''\|\s*volumen''', txt)
for volumen in volumen_s:
    txt = txt.replace(volumen, "|volum")
numero_s = re.findall('''\|\s*número''', txt)
for numero in numero_s:
    txt = txt.replace(numero, "|exemplar")
    
with open('eixida.txt', 'w') as f:
    f.write(str(txt))
