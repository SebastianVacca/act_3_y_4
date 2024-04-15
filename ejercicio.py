import pandas as pd
import numpy as np
import networkx as nx
from networkx.classes.reportviews import NodeView, EdgeView

df = pd.read_csv('estaciones.csv', index_col=None)

TRANS = nx.from_pandas_edgelist(df, source='Origen', target='Destino', edge_attr='Longitud')



TRANS.nodes()
NodeView(('portal suba', 'campiña', 'tv 91', 'suba av boyaca', 'calle 127', 'humedal cordoba', 'calle 116', 'puente largo', 'suba calle 100',
          'calle 95', 'rionegro', 'san martin', 'escuela militar', 'carrera 47', 'carrera 53', 'ferias', 'titan plaza', 'minuto de dios', 'granja', 'quirigua', 'portal 80', ''
          , 'polo ', 'calle 76', 'calle 72 ', 'flores', 'calle 67', 'calle 63', 'calle 57', 'marly', 'calle 45', 'calle 39', 'profamilia', 'calle 26', 'calle 22', 'calle 19'))


TRANS.edges()
EdgeView([('portal suba', 'campiña'), ('campiña', 'tv 91'), ('tv 91', 'suba av boyaca'), ('suba av boyaca', 'calle 127'), ('calle 127', 'humedal cordoba'), ('humedal cordoba', 'calle 116'),
          ('calle 116', 'puente largo'), ('puente largo', 'suba calle 100'), ('suba calle 100', 'calle 95'), ('calle 95', 'rionegro'), ('rionegro', 'san martin'), ('san martin', 'escuela militar'), ('escuela militar', 'polo'),
          ('polo', 'calle 76'), ('calle 76', 'calle 72'), ('calle 72', 'flores'), ('flores', 'calle 67'), ('calle 67', 'calle 63'), ('calle 63', 'calle 57'),  ('calle 57', 'marly'), ('marly', 'calle 45'), ('calle 45', 'calle 39'),
          ('calle 39', 'profamilia'), ('profamilia', 'calle 26'), ('calle 26', 'calle 22'), ('calle 22', 'calle 19'), ('escuela militar', 'carrera 47'), ('carrera 47', 'carrera 53'), ('carrera 53', 'ferias'), ('ferias', 'titan plaza'), ('titan plaza', 'minuto de dios'), ('minuto de dios', 'granja'), ('granja', 'quirigua'), ('quirigua', 'portal 80') ])

TRANS.order()
35

for x in TRANS.nodes():
    if TRANS.degree(x) > 2:
        print(x)

djk_path=nx.dijkstra_path(TRANS, source='portal suba', target='calle 19', weight=True)
djk_path

