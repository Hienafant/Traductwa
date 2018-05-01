# coding=UTF-8
import re

with open('entrada.txt', 'r') as f:
    txt = f.read()

#Everybode is in replace
cita_libro_s = re.findall('''{{cite book''', txt, re.I)
for cita_libro in cita_libro_s:
    txt = txt.replace(cita_libro, "{{ref-llibre")
cita_web_s = re.findall('''{{cite web''', txt, re.I)
for cita_web in cita_web_s:
    txt = txt.replace(cita_web, "{{ref-web")
cita_noticia_s = re.findall('''{{cite news''', txt, re.I)
for cita_noticia in cita_noticia_s:
    txt = txt.replace(cita_noticia, "{{ref-notícia")
cita_publicacion_s = re.findall('''{{cite journal''', txt, re.I)
for cita_publicacion in cita_publicacion_s:
    txt = txt.replace(cita_publicacion, "{{ref-publicació")
titulo_s = re.findall('''\|\s*title''', txt)
for titulo in titulo_s:
    txt = txt.replace(titulo, "|títol")
capitulo_s = re.findall('''\|\s*chapter''', txt)
for capitulo in capitulo_s:
    txt = txt.replace(capitulo, "|capítol")
publicacion_s = re.findall('''\|\s*journal''', txt) #de Cite journal
for publicacion in publicacion_s:
    txt = txt.replace(publicacion, "|publicació")
revista_s = re.findall('''\|\s*work''', txt) #de Cite news
for revista in revista_s:
    txt = txt.replace(revista, "|obra")
apellido_s = re.findall('''\|\s*last''', txt)
for apellido in apellido_s:
    txt = txt.replace(apellido, "|cognom")
nombre_s = re.findall('''\|\sname''', txt)
for nombre in nombre_s:
    txt = txt.replace(nombre, "|nom")
ubicacion_s = re.findall('''\|\s*location''', txt)
for ubicacion in ubicacion_s:
    txt = txt.replace(ubicacion, "|lloc")
fechaacceso_s = re.findall('''\|\s*access-date''', txt)
for fechaacceso in fechaacceso_s:
    txt = txt.replace(fechaacceso, "|consulta")
fecha_s = re.findall('''\|\s*date''', txt)
for fecha in fecha_s:
    txt = txt.replace(fecha, "|data")
sitioweb_s = re.findall('''\|\s*website''', txt)
for sitioweb in sitioweb_s:
    txt = txt.replace(sitioweb, "|obra")
anno_s = re.findall('''\|\s*year''', txt)
for anno in anno_s:
    txt = txt.replace(anno, "|any")
edicion_s = re.findall('''\|\s*edition''', txt)
for edicion in edicion_s:
    txt = txt.replace(edicion, "|edició")
paginas_s = re.findall('''\|\s*pages''', txt)
for paginas in paginas_s:
    txt = txt.replace(paginas, "|pàgines")
pagina_s = re.findall('''\|\s*page\s*=''', txt)
for pagina in pagina_s:
    txt = txt.replace(pagina, "|pàgina=")
agencia_s = re.findall('''\|\s*agency''', txt)
for agencia in agencia_s:
    txt = txt.replace(agencia, "|agència")
volumen_s = re.findall('''\|\s*volume''', txt)
for volumen in volumen_s:
    txt = txt.replace(volumen, "|volum")
numero_s = re.findall('''\|\s*issue''', txt)
for numero in numero_s:
    txt = txt.replace(numero, "|exemplar")
editorial_s = re.findall('''\|\s*publisher''', txt)
for editorial in editorial_s:
    txt = txt.replace(editorial, "|editorial")
    
with open('eixida.txt', 'w') as f:
    f.write(str(txt))
