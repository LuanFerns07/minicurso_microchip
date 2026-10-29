#!/usr/bin/env python3
"""Gera gráficos e tabelas Beamer a partir de contagens documentadas por die."""
from pathlib import Path
import csv
ROOT=Path(__file__).resolve().parents[1]
ROWS=list(csv.DictReader((ROOT/'dados/integracao_processadores.csv').open(encoding='utf-8')))
COLORS={'Intel':'blue_theme','Apple':'ativo','NVIDIA':'lacuna'}
def tex(s):
    return s.replace('&',r'\&').replace('%',r'\%').replace('_',r'\_').replace('µ',r'$\mu$')
def number(n):
    n=int(n)
    if n>=1_000_000_000:return (f'{n/1e9:g}'.replace('.',',')+' bi')
    if n>=1_000_000:return(f'{n/1e6:g}'.replace('.',',')+' mi')
    return (f'{n/1e3:g}'.replace('.',',')+' mil')
# Os rótulos Intel alternam os lados da trajetória para ficar legíveis em 4:3.
OFFSETS=[(2,10),(0,14),(-1,14),(-1,-22),(-2,15),(-20,-25),(14,-17),(7,18)]
plot=[r'% Gerado por scripts/gerar_integracao.py.',r'\newcommand{\graficoIntegracao}[1]{%',r'\begin{tikzpicture}',r'\begin{semilogyaxis}[width=11.4cm,height=5.5cm,xmin=1969,xmax=2027,ymin=1000,ymax=1.2e11,xtick={1971,1980,1990,2000,2010,2020},xticklabel style={/pgf/number format/1000 sep={}},ytick={1e3,1e5,1e7,1e9,1e11},yticklabels={mil,100 mil,10 mi,1 bi,100 bi},ylabel={Transistores por die},xlabel={Ano de lançamento},grid=major,major grid style={gray!18},axis lines=left,set layers=standard,tick label style={font=\scriptsize},label style={font=\scriptsize},clip=false]']
intel=[r for r in ROWS if r['familia']=='Intel']
coords=' '.join(f"({r['ano']},{r['transistores']})" for r in intel)
plot += [r'\ifnum#1=1',fr'\addplot[blue_theme!45,thin,mark=*,mark options={{fill=blue_theme}},mark size=1.7pt] coordinates {{{coords}}};']
for r,(dx,dy) in zip(intel,OFFSETS):
    label=tex(r['rotulo'])+r'\\'+tex(number(r['transistores']))+' · '+tex(r['processo_rotulo'])
    plot.append(fr'\node[font=\tiny,align=center,fill=white,fill opacity=.9,text opacity=1,inner sep=1pt,xshift={dx}pt,yshift={dy}pt] at (axis cs:{r["ano"]},{r["transistores"]}){{{label}}};')
plot += [r'\else',fr'\addplot[gray!45,thin,mark=*,mark size=1.4pt] coordinates {{{coords}}};']
for family,mark in [('Apple','square*'),('NVIDIA','triangle*')]:
    rows=[r for r in ROWS if r['familia']==family]
    coords=' '.join(f"({r['ano']},{r['transistores']})" for r in rows)
    plot.append(fr'\addplot[only marks,{COLORS[family]},mark={mark},mark size=2.1pt] coordinates {{{coords}}};')
plot += [r'\begin{pgfonlayer}{axis foreground}',r'\node[anchor=north west,fill=white,inner sep=3pt] at (rel axis cs:.02,.98){\scriptsize\begin{tabular}{lrrr}\textbf{Chip}&\textbf{Ano}&\textbf{Transistores}&\textbf{Processo}\\'];
for r in ROWS:
    if r['familia']=='Intel':continue
    plot.append(fr'\textcolor{{{COLORS[r["familia"]]}}}{{{tex(r["rotulo"])}}}&{r["ano"]}&{tex(number(r["transistores"]))}&{tex(r["processo_rotulo"])}\\')
plot += [r'\end{tabular}};',r'\node[anchor=north east,align=right,font=\tiny,text=black!65] at (rel axis cs:1,.55){Cinza: Intel\\Verde: Apple (SoC Arm)\\Âmbar: NVIDIA (GPU)};',r'\end{pgfonlayer}',r'\fi',r'\end{semilogyaxis}',r'\end{tikzpicture}}']
(ROOT/'slides/integracao_visual.tex').write_text('\n'.join(plot)+'\n',encoding='utf-8')
frames=[r'% Gerado por scripts/gerar_integracao.py.',r'\begin{frame}{Integração: de milhares a bilhões de transistores}',r'\only<1|handout:0>{\figura{\graficoIntegracao{1}}\etapa{1/2}{Marcos Intel: mais transistores por circuito integrado.}}',r'\only<2|handout:1>{\figura{\graficoIntegracao{2}}\etapa{2/2}{SoCs Apple e GPU NVIDIA ampliam o panorama; funções e áreas são distintas.}}',r'\fonte{Fontes primárias: Intel (guia histórico e Nehalem), ISSCC 2012 (Ivy Bridge), Apple Newsroom (M1--M4) e NVIDIA (GA100). Eixo vertical logarítmico. Contagens por die, não por placa; processo é a designação publicada, não comprimento de porta. Dados e links em dados/integracao\_processadores.csv.}',r'\end{frame}',r'\begin{frame}{Ler o gráfico: o que significa ``integrar mais''?}',r'\duas{\textcolor{blue_theme}{\large\textbf{O que contamos}}\par\medskip Mais dispositivos no mesmo circuito integrado.\par\medskip CPU, memórias, interfaces e aceleradores podem dividir o die.}{\textcolor{blue_theme}{\large\textbf{O que também importa}}\par\medskip Processo, área do die e função do chip.\par\medskip A contagem sozinha não mede desempenho nem densidade.}',r'\chamada{VLSI: integração de muitos dispositivos e conexões em um chip.}',r'\fonte{M1--M4 são SoCs com arquitetura Arm; A100 é uma GPU. O histórico é uma seleção didática de produtos, sem ajuste de uma curva universal de Moore. As contagens recentes abrangem o chip completo.}',r'\end{frame}']
(ROOT/'slides/integracao_trecho.tex').write_text('\n'.join(frames)+'\n',encoding='utf-8')
poster=[r'\documentclass[10pt,a4paper]{article}',r'\usepackage[landscape,margin=14mm,top=22mm,bottom=18mm,headheight=25pt]{geometry}',r'\input{estilo.tex}',r'\usepackage{pgfplots}\pgfplotsset{compat=1.18}',r'\definecolor{blue_theme}{RGB}{0,83,134}\definecolor{ativo}{RGB}{0,132,75}\definecolor{lacuna}{RGB}{199,123,0}',r'\makeatletter\def\input@path{{../slides/}}\makeatother',r'\input{integracao_visual.tex}',r'\begin{document}',r'\titulo{Histórico de integração em processadores}{Luan F. Nogueira e Luiz F. de Melo Soares · contagens por die · seleção 1971--2024}',r'\begin{minipage}[t]{.48\linewidth}\vspace{0pt}\centering\resizebox{\linewidth}{!}{\graficoIntegracao{2}}\par\smallskip\footnotesize CPU, SoC e GPU têm funções e áreas diferentes. Contagem não equivale a desempenho ou densidade. Nós de processo não medem uniformemente o comprimento da porta.\end{minipage}\hfill',r'\begin{minipage}[t]{.49\linewidth}\vspace{0pt}\scriptsize\begin{tabular}{rllrr}\toprule Ano&Chip&Classe&Transistores&Processo\\\midrule']
for r in ROWS:poster.append(fr'{r["ano"]}&{tex(r["rotulo"])}&{tex(r["classe"])}&{tex(number(r["transistores"]))}&{tex(r["processo_rotulo"])}\\')
poster += [r'\bottomrule\end{tabular}\par\medskip\footnotesize Fontes: Intel, Apple, NVIDIA e artigo de Ivy Bridge no ISSCC 2012. Links individuais, revisões selecionadas e observações no CSV e no documento FONTES\_INTEGRACAO.md.\end{minipage}',r'\end{document}']
(ROOT/'apoio/integracao_processadores.tex').write_text('\n'.join(poster)+'\n',encoding='utf-8')
print(f'Gráfico e tabela: {len(ROWS)} chips com contagens e processos documentados.')
