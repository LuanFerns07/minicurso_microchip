#!/usr/bin/env python3
"""Desenha os polos e compõe as listas da seção Brasil a partir dos CSVs."""
import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# Coordenadas de referência apenas para situar polos; interiores são áreas agregadas.
POLOS = [
('Manaus', -60.02, -3.10, 'Norte', 'Manaus', 1.5, 5.9),
('Brasília', -47.88, -15.79, 'Centro-Oeste', 'Brasília', 2.8, 3.8),
('Campina Grande', -35.88, -7.23, 'Nordeste', 'Campina Grande', 7.5, 5.1),
('Salvador', -38.50, -12.97, 'Nordeste', 'Salvador', 7.5, 3.8),
('Interior de Minas Gerais', -45.9, -21.5, 'Sudeste', 'Interior de MG', 7.5, 2.9),
('Belo Horizonte e proximidades', -43.94, -19.92, 'Sudeste', 'Belo Horizonte', 7.5, 3.35),
('Campinas e proximidades', -47.06, -22.90, 'Sudeste', 'Campinas', 7.5, 2.1),
('Florianópolis', -48.55, -27.59, 'Sul', 'Florianópolis', 7.5, .9),
('Porto Alegre e proximidades', -51.23, -30.03, 'Sul', 'Porto Alegre', 5.0, -.25),
('Interior de São Paulo', -49.4, -21.5, 'Sudeste', 'Interior de SP', 1.4, 2.5),
('Curitiba e proximidades', -49.27, -25.43, 'Sul', 'Curitiba', 7.5, 1.45),
('Interior do Rio Grande do Sul', -54.5, -29.8, 'Sul', 'Interior do RS', 1.5, .25),
('São José dos Campos e proximidades', -45.88, -23.18, 'Sudeste', 'S. José dos Campos', 7.5, 2.55),
]
MARKER_OFFSETS = {5:(.20,.08),6:(.05,.15),7:(-.08,.10),10:(-.14,.10),13:(.20,-.10),11:(-.03,-.03),8:(.10,.02)}
REGCOL = {'Norte':'green_ufc','Nordeste':'lacuna','Centro-Oeste':'red!65!blue','Sudeste':'blue_theme','Sul':'ativo'}
def tex(s):
    for a,b in [ ('\\',r'\textbackslash{}'), ('&',r'\&'), ('%',r'\%'), ('_',r'\_'), ('#',r'\#') ]:
        s=s.replace(a,b)
    return s

def create_poster(groups, orgs):
    rows=[r'\documentclass[10pt,a3paper]{article}',r'\usepackage[landscape,margin=14mm,top=24mm,bottom=18mm,headheight=25pt,footskip=8mm]{geometry}',r'\input{estilo.tex}',r'\colorlet{blue_theme}{azul}\definecolor{green_ufc}{RGB}{0,146,62}\definecolor{lacuna}{RGB}{199,123,0}\definecolor{ativo}{RGB}{0,132,75}',r'\makeatletter\def\input@path{{../slides/}}\makeatother',r'\input{brasil_mapa.tex}',r'\hypersetup{pdftitle={Microeletrônica no Brasil — mapa e organizações por polo}}',r'\begin{document}',r'\titulo{Microeletrônica no Brasil}{Mapa próprio a partir do Brazil Silicon Roadmap · Matheus Grossi}',r'\begin{minipage}[t]{.28\linewidth}\vspace{0pt}\small\raggedright']
    def cluster(i):
        polo=POLOS[i-1]
        rows.append(r'\textcolor{azul}{\textbf{'+str(i)+' · '+tex(polo[0])+r'}}\par')
        for org in groups[polo[0]]:
            marker=r'$\bullet$' if orgs[org]['tipo'].startswith(('Empresa','Estatal')) else r'$\circ$'
            rows.append(marker+' '+tex(org)+r'\par')
        rows.append(r'\vspace{2mm}')
    for i in [1,3,4,2,5,6,9,12]:cluster(i)
    rows.extend([r'\end{minipage}\hfill',r'\begin{minipage}[t]{.40\linewidth}\vspace{0pt}\centering',r'\resizebox{\linewidth}{!}{\mapaBrasil{1,2,3,4,5,6,7,8,9,10,11,12,13}}',r'\par\bigskip{\Large\color{azul}\textbf{54 organizações · 13 polos}}\par',r'\small 73 presenças: uma organização pode aparecer em vários polos.\par\medskip',r'$\bullet$ Empresa\quad $\circ$ Centro ou grupo de pesquisa\par\medskip',r'\footnotesize Pontos esquemáticos por polo; interiores representam áreas agregadas.\par\medskip',r'\href{https://github.com/MattGrossi12/brazil_silicon_roadmap}{Levantamento: Matheus Grossi · Brazil Silicon Roadmap}\par',r'\footnotesize Edição baseada na planilha PT-BR fornecida em 28/10/2026.\par\medskip',r'Contorno: \href{https://github.com/johan/world.geo.json/blob/master/countries/BRA.geo.json}{johan/world.geo.json}. Composição redesenhada em TikZ.\par\medskip',r'Desenho didático: Luan F. Nogueira e Luiz F. de Melo Soares.',r'\end{minipage}\hfill',r'\begin{minipage}[t]{.28\linewidth}\vspace{0pt}\small\raggedright'])
    for i in [7,10,13,11,8]:cluster(i)
    rows.extend([r'\end{minipage}',r'\end{document}'])
    (ROOT/'apoio/mapa_brasil.tex').write_text('\n'.join(rows)+'\n', encoding='utf-8')

def main():
    orgs={r['organizacao']:r for r in csv.DictReader((ROOT/'dados/organizacoes_brasil.csv').open(encoding='utf-8'))}
    groups=defaultdict(list)
    for row in csv.DictReader((ROOT/'dados/presencas_brasil.csv').open(encoding='utf-8')):
        groups[row['polo']].append(row['organizacao'])
    assert set(groups)=={p[0] for p in POLOS}
    lines=[r'% Gerado por scripts/gerar_brasil.py.',r'\input{brasil_contorno.tex}',r'\newcommand{\mapaBrasil}[1]{%',r'\begin{tikzpicture}[x=.75cm,y=.75cm,font=\scriptsize]',r'\ifdefined\SemRotulos\path[use as bounding box](-.3,-.6) rectangle (6.8,7);\else\path[use as bounding box](-.3,-.6) rectangle (11.7,7);\fi',r'\filldraw[fill=blue_theme!5,draw=blue_theme,line width=.8pt] \contornoBrasil;']
    for i,(name,lon,lat,region,label,lx,ly) in enumerate(POLOS,1):
        x,y=(lon+74)*.165,(lat+34)*.165
        lines.append(fr'\fill[black!22] ({x:.3f},{y:.3f})circle(.05);')
    lines.append(r'\foreach \selecionado in {#1}{')
    for i,(name,lon,lat,region,label,lx,ly) in enumerate(POLOS,1):
        x,y=(lon+74)*.165,(lat+34)*.165
        dx,dy=MARKER_OFFSETS.get(i,(0,0))
        x,y=x+dx,y+dy
        col=REGCOL[region]
        # Labels mostly outside the silhouette, so dense hubs remain readable.
        lines.append(fr'\ifnum\selecionado={i}\relax\ifdefined\SemRotulos\else\draw[{col},line width=.6pt]({x:.3f},{y:.3f})--({lx:.2f},{ly:.2f});\node[anchor=west,fill=white,inner sep=1.5pt,text={col},font=\scriptsize] at({lx:.2f},{ly:.2f}){{{tex(label)}}};\fi\node[circle,fill={col},text=white,inner sep=1.3pt,font=\tiny] at({x:.3f},{y:.3f}){{{i}}};\fi')
    lines.extend([r'}',r'\end{tikzpicture}}',r'\newcommand{\creditoBrasil}{\fonte{Levantamento: Matheus Grossi · \href{https://github.com/MattGrossi12/brazil_silicon_roadmap}{Brazil Silicon Roadmap}, planilha PT-BR fornecida. Mapa próprio; polos esquemáticos.}}'])
    (ROOT/'slides/brasil_mapa.tex').write_text('\n'.join(lines)+'\n', encoding='utf-8')
    fragments=[r'% Gerado por scripts/gerar_brasil.py. Relação integral de 73 presenças.',r'\section{Âmbito Brasil}',r'\begin{frame}{Microeletrônica no Brasil}',r'\duas{\begingroup\def\SemRotulos{1}\figura{\mapaBrasil{1,2,3,4,8,9}}\endgroup}{\vspace{5mm}\textcolor{blue_theme}{\Huge 54}\ organizações\par\medskip\textcolor{blue_theme}{\Huge 13}\ polos\par\medskip Projeto • ferramentas • integração • fabricação • pesquisa}',r'\creditoBrasil',r'\end{frame}']
    pages=[('Norte e Nordeste',[1,3,4]),('Centro-Oeste e Minas Gerais',[2,5,6]),('São Paulo · polo de Campinas',[7]),('São Paulo · outros polos',[10,13]),('Paraná e Santa Catarina',[11,8]),('Rio Grande do Sul',[9,12])]
    for title,ids in pages:
        fragments.extend([fr'\begin{{frame}}{{Âmbito Brasil · {title}}}',r'\begin{columns}[T,onlytextwidth]',r'\begin{column}{.35\textwidth}',fr'\figura{{\mapaBrasil{{{",".join(map(str,ids))}}}}}',r'{\tiny $\bullet$ empresa\par $\circ$ centro/grupo}',r'\end{column}',r'\begin{column}{.63\textwidth}',r'\footnotesize\setlength{\columnsep}{3mm}\begin{multicols}{2}\raggedright'])
        for i in ids:
            name,label=POLOS[i-1][0],POLOS[i-1][4]
            fragments.append(fr'\textcolor{{blue_theme}}{{\textbf{{{tex(label)}}}}}\par\smallskip')
            for org in groups[name]:
                marker=r'$\bullet$' if orgs[org]['tipo'].startswith(('Empresa','Estatal')) else r'$\circ$'
                fragments.append(r'\noindent\parbox{\linewidth}{'+marker+' '+tex(org)+r'}\par')
            fragments.append(r'\medskip')
        fragments.extend([r'\end{multicols}',r'\end{column}',r'\end{columns}',r'\creditoBrasil',r'\end{frame}'])
    (ROOT/'slides/brasil_trecho.tex').write_text('\n'.join(fragments)+'\n', encoding='utf-8')
    create_poster(groups, orgs)
    print(f'Mapa e seis páginas regionais: {len(orgs)} organizações, {sum(map(len,groups.values()))} presenças.')

if __name__=='__main__':main()
