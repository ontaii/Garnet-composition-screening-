import itertools; import math; import time
from xml.dom.minidom import Element
import pandas as pd

Elements = {
    'Li+' : {'Val':1,'Negativity':0.98,'Radius_8CN':0.92,'Radius_6CN':0.76,'Radius_4CN':0.59},
    'Be2+' : {'Val':2,'Negativity':1.57,'Radius_6CN':0.45,'Radius_4CN':0.27,'Radius_3CN':0.16},
    'B3+' : {'Val':3,'Negativity':2.04,'Radius_6CN':0.27,'Radius_4CN':0.11,'Radius_3CN':0.01},
    'C4+' : {'Val':4,'Negativity':2.55,'Radius_6CN':0.16,'Radius_4CN':0.15,'Radius_3CN':-0.08},
    'N3-' : {'Val':-3,'Negativity':3.04,'Radius_4CN':1.46},
    'N3+' : {'Val':3,'Negativity':3.04,'Radius_6CN':0.16},
    'N5+' : {'Val':5,'Negativity':3.04,'Radius_6CN':0.13,'Radius_3CN':-0.104},
    'O2-' : {'Val':-2,'Negativity':3.44,'Radius_8CN':1.42,'Radius_6CN':1.4,'Radius_4CN':1.38,'Radius_3CN':1.36,'Radius_2CN':1.35},
    'F-' : {'Val':-1,'Negativity':3.98,'Radius_6CN':1.33,'Radius_4CN':1.31,'Radius_3CN':1.3,'Radius_2CN':1.285},
    'F7+' : {'Val':7,'Negativity':3.98,'Radius_4CN':0.08,},
    'Na+' : {'Val':1,'Negativity':0.96,'Radius_12CN':1.39,'Radius_9CN':1.24,'Radius_8CN':1.18,'Radius_7CN':1.12,'Radius_6CN':1.02,'Radius_5CN':1,'Radius_4CN':0.99},
    'Mg2+' : {'Val':2,'Negativity':1.31,'Radius_8CN':0.89,'Radius_6CN':0.72,'Radius_5CN':0.66,'Radius_4CN':0.57},
    'Al3+' : {'Val':3,'Negativity':1.61,'Radius_6CN':0.535,'Radius_5CN':0.48,'Radius_4CN':0.39},
    'Si4+' : {'Val':4,'Negativity':1.90,'Radius_6CN':0.40,'Radius_4CN':0.26},
    'P3+' : {'Val':3,'Negativity':2.19,'Radius_6CN':0.44},
    'P5+' : {'Val':5,'Negativity':2.19,'Radius_6CN':0.38,'Radius_5CN':0.29,'Radius_4CN':0.17},
    'S2-' : {'Val':-2,'Negativity':2.58,'Radius_6CN':1.84},
    'S4+' : {'Val':4,'Negativity':2.58,'Radius_6CN':0.37},
    'S6+' : {'Val':6,'Negativity':2.58,'Radius_6CN':0.29,'Radius_4CN':0.12},
    'Cl-' : {'Val':-1,'Negativity':3.16,'Radius_6CN':1.81},
    'Cl5+' : {'Val':5,'Negativity':3.16,'Radius_3CN':0.12},
    'Cl7+' : {'Val':7,'Negativity':3.16,'Radius_6CN':0.27,'Radius_4CN':0.06},
    'K+' :  {'Val':1,'Negativity':0.82,'Radius_12CN':1.64,'Radius_10CN':1.59,'Radius_9CN':1.55,'Radius_8CN':1.51,'Radius_7CN':1.46,'Radius_6CN':1.38,'Radius_4CN':1.37},
    'Ca2+' : {'Val':2,'Negativity':1.00,'Radius_12CN':1.34,'Radius_10CN':1.23,'Radius_9CN':1.18,'Radius_8CN':1.12,'Radius_7CN':1.06,'Radius_6CN':1},
    'Sc3+' : {'Val':3,'Negativity':1.36,'Radius_8CN':0.87,'Radius_6CN':0.745},
    'Ti2+' : {'Val':2,'Negativity':1.54,'Radius_6CN':0.86},
    'Ti3+' : {'Val':3,'Negativity':1.54,'Radius_6CN':0.67},
    'Ti4+' : {'Val':4,'Negativity':1.54,'Radius_8CN':0.74,'Radius_6CN':0.605,'Radius_5CN':0.51,'Radius_4CN':0.42},
    'V2+' : {'Val':2,'Negativity':1.63,'Radius_6CN':0.79},
    'V3+' : {'Val':3,'Negativity':1.63,'Radius_6CN':0.64},
    'V4+' : {'Val':4,'Negativity':1.63,'Radius_8CN':0.72,'Radius_6CN':0.64,'Radius_5CN':0.53},
    'V5+' : {'Val':5,'Negativity':1.63,'Radius_6CN':0.54,'Radius_5CN':0.46,'Radius_4CN':0.355},
    'Cr2+' : {'Val':2,'Negativity':1.66,'Radius_6CN':0.8,'Radius_6CN_L':0.73},
    'Cr3+' : {'Val':3,'Negativity':1.66,'Radius_6CN':0.615,'Radius_4CN':0.47}, #4CN, guess
    'Cr4+' : {'Val':4,'Negativity':1.66,'Radius_6CN':0.55,'Radius_4CN':0.41},
    'Cr5+' : {'Val':5,'Negativity':1.66,'Radius_8CN':0.57,'Radius_6CN':0.49,'Radius_4CN':0.345},
    'Cr6+' : {'Val':6,'Negativity':1.66,'Radius_6CN':0.44,'Radius_4CN':0.26},
    'Mn2+' : {'Val':2,'Negativity':1.55,'Radius_8CN':0.96,'Radius_7CN':0.9,'Radius_6CN':0.83,'Radius_6CN_L':0.67,'Radius_5CN':0.75,'Radius_4CN':0.66},
    'Mn3+' : {'Val':3,'Negativity':1.55,'Radius_6CN':0.645,'Radius_6CN_L':0.58,'Radius_5CN':0.58},
    'Mn4+' : {'Val':4,'Negativity':1.55,'Radius_6CN':0.53,'Radius_4CN':0.39},
    'Mn5+' : {'Val':5,'Negativity':1.55,'Radius_4CN':0.33},
    'Mn6+' : {'Val':6,'Negativity':1.55,'Radius_4CN':0.255},
    'Mn7+' : {'Val':7,'Negativity':1.55,'Radius_6CN':0.46,'Radius_4CN':0.25},
    'Fe2+' : {'Val':2,'Negativity':1.83,'Radius_8CN':0.92,'Radius_6CN':0.78,'Radius_6CN_L':0.61,'Radius_4CN':0.63},
    'Fe3+' : {'Val':3,'Negativity':1.83,'Radius_8CN':0.78,'Radius_6CN':0.645,'Radius_6CN_L':0.55,'Radius_5CN':0.58,'Radius_4CN':0.49},
    'Fe4+' : {'Val':4,'Negativity':1.83,'Radius_6CN':0.585},
    'Fe6+' : {'Val':6,'Negativity':1.83,'Radius_4CN':0.25},
    'Co2+' : {'Val':2,'Negativity':1.88,'Radius_8CN':0.9,'Radius_6CN':0.745,'Radius_6CN_L':0.65,'Radius_5CN':0.67,'Radius_4CN':0.58},
    'Co3+' : {'Val':3,'Negativity':1.88,'Radius_6CN':0.61,'Radius_6CN_L':0.545},
    'Co4+' : {'Val':4,'Negativity':1.88,'Radius_6CN':0.53,'Radius_4CN':0.4},
    'Ni2+' : {'Val':2,'Negativity':1.91,'Radius_6CN':0.69,'Radius_5CN':0.63,'Radius_4CN':0.55},
    'Ni3+' : {'Val':3,'Negativity':1.91,'Radius_6CN':0.6,'Radius_6CN_L':0.56},
    'Ni4+' : {'Val':4,'Negativity':1.91,'Radius_6CN':0.48},
    'Cu+' : {'Val':1,'Negativity':1.9,'Radius_8CN':0.93,'Radius_6CN':0.77,'Radius_4CN':0.6,'Radius_2CN':0.46}, #8CN, guess
    'Cu2+' : {'Val':2,'Negativity':1.9,'Radius_8CN':0.89,'Radius_6CN':0.73,'Radius_4CN':0.65,'Radius_4CN':0.57}, #8CN, guess
    'Cu3+' : {'Val':3,'Negativity':1.9,'Radius_6CN_L':0.54},
    'Zn2+' : {'Val':2,'Negativity':1.65,'Radius_8CN':0.90,'Radius_6CN':0.74,'Radius_5CN':0.68,'Radius_4CN':0.60},
    'Ga3+' : {'Val':3,'Negativity':1.81,'Radius_6CN':0.62,'Radius_5CN':0.55,'Radius_4CN':0.47},
    'Ge2+' : {'Val':2,'Negativity':2.01,'Radius_6CN':0.73},
    'Ge4+' : {'Val':4,'Negativity':2.01,'Radius_6CN':0.53,'Radius_4CN':0.39},
    'As3+' : {'Val':3,'Negativity':2.18,'Radius_6CN':0.58},
    'As5+' : {'Val':5,'Negativity':2.18,'Radius_6CN':0.46,'Radius_4CN':0.335},
    'Se2-' : {'Val':-2,'Negativity':2.55,'Radius_6CN':1.98},
    'Se4+' : {'Val':4,'Negativity':2.55,'Radius_6CN':0.5},
    'Se6+' : {'Val':6,'Negativity':2.55,'Radius_6CN':0.28},
    'Br-' : {'Val':-1,'Negativity':2.96,'Radius_6CN':1.96},
    'Br3+' : {'Val':3,'Negativity':2.96,'Radius_4CN':0.59},
    'Br5+' : {'Val':5,'Negativity':2.96,'Radius_3CN':0.31},
    'Br7+' : {'Val':7,'Negativity':2.96,'Radius_6CN':0.39,'Radius_4CN':0.25},
    'Rb+' : {'Val':1,'Negativity':0.82,'Radius_14CN':1.83,'Radius_12CN':1.72,'Radius_11CN':1.69,'Radius_10CN':1.66,'Radius_9CN':1.63,'Radius_8CN':1.61,'Radius_7CN':1.56,'Radius_6CN':1.52},
    'Sr2+' : {'Val':2,'Negativity':0.95,'Radius_12CN':1.44,'Radius_10CN':1.36,'Radius_9CN':1.31,'Radius_8CN':1.26,'Radius_7CN':1.21,'Radius_6CN':1.18},
    'Y3+' :  {'Val':3,'Negativity':1.22,'Radius_9CN':1.075,'Radius_8CN':1.019,'Radius_7CN':0.96,'Radius_6CN':0.9},
    'Zr4+' : {'Val':4,'Negativity':1.33,'Radius_9CN':0.89,'Radius_8CN':0.84,'Radius_7CN':0.78,'Radius_6CN':0.72,'Radius_5CN':0.66,'Radius_4CN':0.59},
    'Nb3+' : {'Val':3,'Negativity':1.6,'Radius_6CN':0.72},
    'Nb4+' : {'Val':4,'Negativity':1.6,'Radius_8CN':0.79,'Radius_6CN':0.68},
    'Nb5+' : {'Val':5,'Negativity':1.6,'Radius_8CN':0.74,'Radius_7CN':0.69,'Radius_6CN':0.64,'Radius_4CN':0.48},
    'Mo3+' : {'Val':3,'Negativity':2.16,'Radius_6CN':0.69},
    'Mo4+' : {'Val':4,'Negativity':2.16,'Radius_6CN':0.65},
    'Mo5+' : {'Val':5,'Negativity':2.16,'Radius_6CN':0.61,'Radius_4CN':0.46},
    'Mo6+' : {'Val':6,'Negativity':2.16,'Radius_7CN':0.73,'Radius_6CN':0.59,'Radius_5CN':0.5,'Radius_4CN':0.41},
    'Tc4+' : {'Val':4,'Negativity':1.9,'Radius_6CN':0.645},
    'Tc5+' : {'Val':5,'Negativity':1.9,'Radius_6CN':0.6},
    'Tc7+' : {'Val':7,'Negativity':1.9,'Radius_6CN':0.56,'Radius_4CN':0.37},
    'Ru3+' : {'Val':3,'Negativity':2.2,'Radius_6CN':0.68},
    'Ru4+' : {'Val':4,'Negativity':2.2,'Radius_6CN':0.62},
    'Ru5+' : {'Val':5,'Negativity':2.2,'Radius_6CN':0.565},
    'Ru7+' : {'Val':7,'Negativity':2.2,'Radius_4CN':0.38},
    'Ru8+' : {'Val':8,'Negativity':2.2,'Radius_4CN':0.36},
    'Rh3+' : {'Val':3,'Negativity':2.28,'Radius_6CN':0.665},
    'Rh4+' : {'Val':4,'Negativity':2.28,'Radius_6CN':0.6},
    'Rh5+' : {'Val':5,'Negativity':2.28,'Radius_6CN':0.55},
    'Pd+' : {'Val':1,'Negativity':2.2,'Radius_2CN':0.59},
    'Pd2+' : {'Val':2,'Negativity':2.2,'Radius_6CN':0.86,'Radius_4CN':0.64},
    'Pd3+' : {'Val':3,'Negativity':2.2,'Radius_6CN':0.76},
    'Pd4+' : {'Val':4,'Negativity':2.2,'Radius_6CN':0.615},
    'Ag+' :  {'Val':1,'Negativity':1.93,'Radius_8CN':1.28,'Radius_7CN':1.22,'Radius_6CN':1.15,'Radius_5CN':1.06,'Radius_4CN':1,'Radius_2CN':0.67},
    'Ag2+' :  {'Val':2,'Negativity':1.93,'Radius_6CN':0.94,'Radius_4CN':0.79},
    'Ag3+' :  {'Val':3,'Negativity':1.93,'Radius_6CN':0.75,'Radius_4CN':0.67},
    'Cd2+' :  {'Val':2,'Negativity':1.69,'Radius_12CN':1.31,'Radius_8CN':1.1,'Radius_7CN':1.03,'Radius_6CN':0.95,'Radius_5CN':0.87,'Radius_4CN':0.78},
    'In3+' : {'Val':3,'Negativity':1.78,'Radius_8CN':0.92,'Radius_6CN':0.80,'Radius_4CN':0.62},
    'Sn4+' : {'Val':4,'Negativity':1.96,'Radius_8CN':0.81,'Radius_7CN':0.75,'Radius_6CN':0.69,'Radius_5CN':0.62,'Radius_4CN':0.55},
    'Sb3+' : {'Val':3,'Negativity':2.05,'Radius_6CN':0.76,'Radius_6CN':0.80,'Radius_6CN':0.76},
    'Sb5+' : {'Val':5,'Negativity':2.05,'Radius_6CN':0.60,'Radius_4CN':0.46}, #4CN, guess
    'Te2-' : {'Val':-2,'Negativity':2.1,'Radius_6CN':2.21},
    'Te4+' : {'Val':4,'Negativity':2.1,'Radius_6CN':0.97,'Radius_4CN':0.66,'Radius_3CN':0.52},
    'Te6+' : {'Val':6,'Negativity':2.1,'Radius_6CN':0.56,'Radius_4CN':0.43},
    'I-' : {'Val':-1,'Negativity':2.66,'Radius_6CN':2.2},
    'I5+' : {'Val':5,'Negativity':2.66,'Radius_6CN':0.95,'Radius_3CN':0.44},
    'I7+' : {'Val':7,'Negativity':2.66,'Radius_6CN':0.53,'Radius_4CN':0.42},
    'Cs+' : {'Val':1,'Negativity':0.79,'Radius_12CN':1.88,'Radius_11CN':1.85,'Radius_10CN':1.81,'Radius_9CN':1.78,'Radius_8CN':1.74,'Radius_6CN':1.67},
    'Ba2+' : {'Val':2,'Negativity':0.89,'Radius_12CN':1.61,'Radius_11CN':1.57,'Radius_10CN':1.52,'Radius_9CN':1.47,'Radius_8CN':1.42,'Radius_7CN':1.38,'Radius_6CN':1.35},
    'La3+' : {'Val':3,'Negativity':1.10,'Radius_12CN':1.36,'Radius_10CN':1.27,'Radius_9CN':1.216,'Radius_8CN':1.16,'Radius_7CN':1.1,'Radius_6CN':1.032},
    'Ce3+' : {'Val':3,'Negativity':1.12,'Radius_12CN':1.34,'Radius_10CN':1.25,'Radius_9CN':1.196,'Radius_8CN':1.143,'Radius_7CN':1.07,'Radius_6CN':1.01},
    'Ce4+' : {'Val':4,'Negativity':1.12,'Radius_12CN':1.14,'Radius_10CN':1.07,'Radius_8CN':0.97,'Radius_6CN':0.87},
    'Pr3+' : {'Val':3,'Negativity':1.13,'Radius_9CN':1.179,'Radius_8CN':1.126,'Radius_6CN':0.99},
    'Pr4+' : {'Val':4,'Negativity':1.13,'Radius_8CN':0.96,'Radius_6CN':0.85},
    'Nd2+' : {'Val':2,'Negativity':1.14,'Radius_9CN':1.35,'Radius_8CN':1.29},
    'Nd3+' : {'Val':3,'Negativity':1.14,'Radius_12CN':1.27,'Radius_9CN':1.163,'Radius_8CN':1.109,'Radius_6CN':0.983},
    'Pm3+' : {'Val':3,'Negativity':1.13,'Radius_9CN':1.144,'Radius_8CN':1.093,'Radius_6CN':0.97},
    'Sm2+' : {'Val':2,'Negativity':1.17,'Radius_9CN':1.32,'Radius_8CN':1.27,'Radius_6CN':1.22},
    'Sm3+' : {'Val':3,'Negativity':1.17,'Radius_12CN':1.24,'Radius_9CN':1.132,'Radius_8CN':1.079,'Radius_7CN':1.02,'Radius_6CN':0.958},
    'Eu2+' : {'Val':2,'Negativity':1.2,'Radius_10CN':1.35,'Radius_9CN':1.3,'Radius_8CN':1.25,'Radius_7CN':1.2,'Radius_6CN':1.17},
    'Eu3+' : {'Val':3,'Negativity':1.2,'Radius_9CN':1.12,'Radius_8CN':1.066,'Radius_7CN':1.01,'Radius_6CN':0.947},
    'Gd3+' : {'Val':3,'Negativity':1.2,'Radius_9CN':1.107,'Radius_8CN':1.053,'Radius_7CN':1,'Radius_6CN':0.938},
    'Tb3+' : {'Val':3,'Negativity':1.1,'Radius_9CN':1.095,'Radius_8CN':1.04,'Radius_7CN':0.98,'Radius_6CN':0.923},
    'Tb4+' : {'Val':3,'Negativity':1.1,'Radius_8CN':0.88,'Radius_6CN':0.76},
    'Dy2+' : {'Val':2,'Negativity':1.22,'Radius_8CN':1.19,'Radius_7CN':1.13,'Radius_6CN':1.07},
    'Dy3+' : {'Val':3,'Negativity':1.22,'Radius_9CN':1.083,'Radius_8CN':1.027,'Radius_7CN':0.97,'Radius_6CN':0.912},
    'Ho3+' : {'Val':3,'Negativity':1.23,'Radius_10CN':1.12,'Radius_9CN':1.072,'Radius_8CN':1.015,'Radius_6CN':0.901},
    'Er3+' : {'Val':3,'Negativity':1.24,'Radius_9CN':1.062,'Radius_8CN':1.004,'Radius_7CN':0.945,'Radius_6CN':0.89},
    'Tm2+' : {'Val':2,'Negativity':1.25,'Radius_7CN':1.09,'Radius_6CN':1.03},
    'Tm3+' : {'Val':3,'Negativity':1.25,'Radius_9CN':1.052,'Radius_8CN':0.994,'Radius_6CN':0.88},
    'Yb2+' : {'Val':2,'Negativity':1.1,'Radius_8CN':1.14,'Radius_7CN':1.08,'Radius_6CN':1.02},
    'Yb3+' : {'Val':3,'Negativity':1.1,'Radius_9CN':1.042,'Radius_8CN':0.985,'Radius_7CN':0.925,'Radius_6CN':0.868},
    'Lu3+' : {'Val':3,'Negativity':1.27,'Radius_8CN':1.032,'Radius_8CN':0.977,'Radius_6CN':0.861},
    'Hf4+' : {'Val':4,'Negativity':1.30,'Radius_8CN':0.83,'Radius_7CN':0.76,'Radius_6CN':0.71,'Radius_4CN':0.58},
    'Ta3+' : {'Val':3,'Negativity':1.5,'Radius_6CN':0.72},
    'Ta4+' : {'Val':4,'Negativity':1.5,'Radius_6CN':0.68},
    'Ta5+' : {'Val':5,'Negativity':1.5,'Radius_8CN':0.74,'Radius_7CN':0.69,'Radius_6CN':0.64},
    'W4+' : {'Val':4,'Negativity':2.36,'Radius_6CN':0.66},
    'W5+' : {'Val':5,'Negativity':2.36,'Radius_6CN':0.62},
    'W6+' : {'Val':6,'Negativity':2.36,'Radius_6CN':0.6,'Radius_5CN':0.51,'Radius_4CN':0.42},
    'Re4+' : {'Val':4,'Negativity':1.9,'Radius_6CN':0.63},
    'Re5+' : {'Val':5,'Negativity':1.9,'Radius_6CN':0.58},
    'Re6+' : {'Val':6,'Negativity':1.9,'Radius_6CN':0.55},
    'Re7+' : {'Val':7,'Negativity':1.9,'Radius_6CN':0.53,'Radius_4CN':0.38},
    'Os4+' : {'Val':4,'Negativity':2.2,'Radius_6CN':0.63},
    'Os5+' : {'Val':5,'Negativity':2.2,'Radius_6CN':0.575},
    'Os6+' : {'Val':6,'Negativity':2.2,'Radius_6CN':0.545,'Radius_5CN':0.49},
    'Os7+' : {'Val':7,'Negativity':2.2,'Radius_6CN':0.525},
    'Os8+' : {'Val':8,'Negativity':2.2,'Radius_4CN':0.39},
    'Ir3+' : {'Val':3,'Negativity':2.2,'Radius_6CN':0.68},
    'Ir4+' : {'Val':4,'Negativity':2.2,'Radius_6CN':0.625},
    'Ir5+' : {'Val':5,'Negativity':2.2,'Radius_6CN':0.57},
    'Pt2+' : {'Val':2,'Negativity':2.28,'Radius_6CN':0.8,'Radius_4CN':0.6},
    'Pt4+' : {'Val':4,'Negativity':2.28,'Radius_6CN':0.625},
    'Pt5+' : {'Val':5,'Negativity':2.28,'Radius_6CN':0.57},
    'Au+' : {'Val':1,'Negativity':2.54,'Radius_6CN':1.37},
    'Au3+' : {'Val':3,'Negativity':2.54,'Radius_6CN':0.85,'Radius_4CN':0.68},
    'Au5+' : {'Val':5,'Negativity':2.54,'Radius_6CN':0.57},
    'Hg+' : {'Val':1,'Negativity':2,'Radius_6CN':1.19,'Radius_3CN':0.97},
    'Hg2+' : {'Val':2,'Negativity':2,'Radius_8CN':1.14,'Radius_6CN':1.02,'Radius_4CN':0.96,'Radius_2CN':0.69},
    'Tl+' : {'Val':1,'Negativity':1.62,'Radius_12CN':1.7,'Radius_8CN':1.59,'Radius_6CN':1.5},
    'Tl3+' : {'Val':3,'Negativity':1.62,'Radius_8CN':0.98,'Radius_6CN':0.885,'Radius_4CN':0.75},
    'Pb2+' : {'Val':2,'Negativity':1.87,'Radius_12CN':1.49,'Radius_11CN':1.45,'Radius_10CN':1.4,'Radius_9CN':1.35,'Radius_8CN':1.29,'Radius_7CN':1.23,'Radius_6CN':1.19,'Radius_4CN':0.98},
    'Pb4+' : {'Val':4,'Negativity':1.87,'Radius_8CN':0.94,'Radius_6CN':0.775,'Radius_5CN':0.73,'Radius_4CN':0.65},
    'Bi3+' : {'Val':3,'Negativity':2.02,'Radius_8CN':1.17,'Radius_6CN':1.03,'Radius_5CN':0.96},
    'Po4+' : {'Val':4,'Negativity':2,'Radius_8CN':1.08,'Radius_6CN':0.94},
    'Po6+' : {'Val':6,'Negativity':2,'Radius_6CN':0.67},
    'At6+' : {'Val':6,'Negativity':2.2,'Radius_6CN':0.62},
    'Fr+' : {'Val':1,'Negativity':0.79,'Radius_6CN':1.8},
    'Ra2+' : {'Val':2,'Negativity':0.9,'Radius_12CN':1.7,'Radius_8CN':1.48},
    'Ac3+' : {'Val':3,'Negativity':1.1,'Radius_6CN':1.12},
    'Th4+' : {'Val':4,'Negativity':1.3,'Radius_12CN':1.21,'Radius_11CN':1.18,'Radius_10CN':1.13,'Radius_9CN':1.09,'Radius_8CN':1.05,'Radius_6CN':0.94},
    'U3+' : {'Val':3,'Negativity':1.38,'Radius_6CN':1.025},
    'U4+' : {'Val':4,'Negativity':1.38,'Radius_12CN':1.17,'Radius_9CN':1.05,'Radius_8CN':1,'Radius_7CN':0.95,'Radius_6CN':0.89},
    'U5+' : {'Val':5,'Negativity':1.38,'Radius_7CN':0.84,'Radius_6CN':0.76},
    'U6+' : {'Val':6,'Negativity':1.38,'Radius_8CN':0.86,'Radius_7CN':0.81,'Radius_6CN':0.73,'Radius_4CN':0.52,'Radius_2CN':0.45},
}

time1 = time.time() #time calculation at the beginning

'''Reading the input elements'''
f0 = open('./input.txt','r')
contents = f0.readlines()

for sen in contents:
    if 'A = ' in sen:
        A = sen.replace('A = ',"").replace('\n','')
        listA = A.split(', ')
    elif 'B = ' in sen:
        B = sen.replace('B = ',"").replace('\n','')
        listB = B.split(', ')
    elif 'C = ' in sen:
        C = sen.replace('C = ',"").replace('\n','')
        listC = C.split(', ')

'''Combination'''
f1 = open('./1_ABC_groups.txt','w',encoding='utf-8')

'''AAA'''
group_A = list(itertools.combinations_with_replacement(listA,3))
Length_A = len(group_A)
f1.write('AAA numbers:'+str(Length_A)+'\n')
m = 0

for Ai in group_A:
    m += 1
    Aii = str(Ai)
    Aii = Aii.replace('(','').replace(')','').replace(',','').replace("'",'')
    f1.write(str(m)+' '+str(Aii)+'\n')

f1.write('#####################################################################'+'\n')
'''BB'''
group_B = list(itertools.combinations_with_replacement(listB,2))
Length_B = len(group_B)
f1.write('BB numbers:'+str(Length_B)+'\n')
n = 0

for Bi in group_B:
    n += 1
    Bii = str(Bi)
    Bii = Bii.replace('(','').replace(')','').replace(',','').replace("'",'')
    f1.write(str(n)+' '+str(Bii)+'\n')

f1.write('#####################################################################'+'\n')
'''CCC'''
group_C = list(itertools.combinations_with_replacement(listC,3))
Length_C = len(group_C)
f1.write('CCC numbers:'+str(Length_C)+'\n')
o = 0

for Ci in group_C:
    o += 1
    Cii = str(Ci)
    Cii = Cii.replace('(','').replace(')','').replace(',','').replace("'",'')
    f1.write(str(o)+' '+str(Cii)+'\n')

f1.write('#####################################################################'+'\n')
f1.close()

'''Combination & Val_sum'''
AAABBCCC = itertools.product(group_A,group_B,group_C)
Combination = pd.DataFrame(AAABBCCC, columns=['A', 'B', 'C'])
Cation_Val_Sum = []

for i in range(len(Combination)):
    A1_Val = Elements[Combination['A'][i][0]]['Val']
    A2_Val = Elements[Combination['A'][i][1]]['Val']
    A3_Val = Elements[Combination['A'][i][2]]['Val']
    B1_Val = Elements[Combination['B'][i][0]]['Val']
    B2_Val = Elements[Combination['B'][i][1]]['Val']
    C1_Val = Elements[Combination['C'][i][0]]['Val']
    C2_Val = Elements[Combination['C'][i][1]]['Val']
    C3_Val = Elements[Combination['C'][i][2]]['Val']
    Sum = A1_Val + A2_Val + A3_Val + B1_Val + B2_Val + C1_Val + C2_Val + C3_Val
    Cation_Val_Sum.append(Sum)

Combination['Cation_Val_Sum'] = Cation_Val_Sum
Combination.to_csv('2_Combin_All.csv',index=True)

Val24 = []

for i in range(len(Combination)):
    if Combination['Cation_Val_Sum'].iloc[i] == 24:
        Val24.append(Combination.iloc[i])

Combination24 = pd.DataFrame(Val24).reset_index()
del Combination24['index']
Combination24.to_csv('3_Combin_24.csv',index=True)

'''Judge the smallest B ion is larger than the biggest A ion'''
B_C = []

for i in range(len(Combination24)):
    B1 = Elements[Combination24.iloc[i]['B'][0]]['Radius_6CN']
    B2 = Elements[Combination24.iloc[i]['B'][1]]['Radius_6CN']
    ListB = [B1,B2]
    C1 = Elements[Combination24.iloc[i]['C'][0]]['Radius_6CN']
    C2 = Elements[Combination24.iloc[i]['C'][1]]['Radius_6CN']
    C3 = Elements[Combination24.iloc[i]['C'][2]]['Radius_6CN']
    ListC = [C1,C2,C3]
    if min(ListB) >= max(ListC):
        B_C.append(Combination24.iloc[i])

B_C = pd.DataFrame(B_C).reset_index()
del B_C['index']
B_C.to_csv('4_B_C.csv',index = True)

'''Stability Factor Calculation'''
Stability_Factors = []
for i in range(len(B_C)):
    RA_Av = (Elements[B_C.iloc[i]['A'][0]]['Radius_8CN'] + Elements[B_C.iloc[i]['A'][1]]['Radius_8CN'] + 
             Elements[B_C.iloc[i]['A'][2]]['Radius_8CN'])/3
    RB_Av = (Elements[B_C.iloc[i]['B'][0]]['Radius_6CN'] + Elements[B_C.iloc[i]['B'][1]]['Radius_6CN'])/2
    RC_Av = (Elements[B_C.iloc[i]['C'][0]]['Radius_4CN'] + Elements[B_C.iloc[i]['C'][1]]['Radius_4CN'] + 
             Elements[B_C.iloc[i]['C'][2]]['Radius_4CN'])/3
    SF = 3*(((RB_Av+1.38)**2 - 4/9*((RA_Av+1.38)**2))**(0.5))/2/(RC_Av+1.38)
    Stability_Factors.append(SF)

B_C['Stability_Factors'] = Stability_Factors
del Combination24['Cation_Val_Sum']
B_C.to_csv('5_Combin_SF.csv',index=True)

'''Stability Factor Extraction: 0.95~1.05'''
SF_Extracted = []
for i in range(len(B_C)):
    if B_C.iloc[i]['Stability_Factors'] >= 0.95 and B_C.iloc[i]['Stability_Factors'] <= 1.05:
        SF_Extracted.append(B_C.iloc[i])

SF_Extracted = pd.DataFrame(SF_Extracted).reset_index()
del SF_Extracted['index']
del SF_Extracted['Unnamed: 0']
SF_Extracted.to_csv('6_SF_Extracted.csv',index=True)

'''B_Site_Charge'''
Charge_B_Exctracted = []
for i in range(len(SF_Extracted)):
    B1_charge = Elements[SF_Extracted.iloc[i]['B'][0]]['Val']
    B2_charge = Elements[SF_Extracted.iloc[i]['B'][1]]['Val']
    if B1_charge == 3 or B2_charge == 3:
        Charge_B_Exctracted.append(SF_Extracted.iloc[i])

Charge_B_Exctracted = pd.DataFrame(Charge_B_Exctracted).reset_index()
del Charge_B_Exctracted['index']
Charge_B_Exctracted.to_csv('7_Charge_B_Exctracted.csv',index=True)

'''BV & Radii_Sum'''
BVS_B_Eval = []; Radii_Sum = []

for i in range(len(Charge_B_Exctracted)):
    RA = Elements[Charge_B_Exctracted.iloc[i]['A'][0]]['Radius_8CN'] + Elements[Charge_B_Exctracted.iloc[i]['A'][1]]['Radius_8CN'] + Elements[Charge_B_Exctracted.iloc[i]['A'][2]]['Radius_8CN']
    RB = Elements[Charge_B_Exctracted.iloc[i]['B'][0]]['Radius_6CN'] + Elements[Charge_B_Exctracted.iloc[i]['B'][1]]['Radius_6CN']
    RC = Elements[Charge_B_Exctracted.iloc[i]['C'][0]]['Radius_4CN'] + Elements[Charge_B_Exctracted.iloc[i]['C'][1]]['Radius_4CN'] + Elements[Charge_B_Exctracted.iloc[i]['C'][2]]['Radius_4CN']
    Av_BO = RB/2 + 1.38 #Prediction of the B-O bond length.
    BVS_B = 6*(math.exp((1.724 - Av_BO)/0.37))
    BVS_B_Eval0 = 100*(1-(abs(BVS_B-3)/3))
    BVS_B_Eval.append(BVS_B_Eval0)
    R_Sum = RA + RB + RC
    Radii_Sum.append(R_Sum)

Charge_B_Exctracted['BVS_B_Eval'], Charge_B_Exctracted['Radii_Sum'] = BVS_B_Eval, Radii_Sum
Charge_B_Exctracted.to_csv('8_BV_RadiiSum.csv',index=True)

'''Analysis Part:
BVS_B_Eval > 95; Radii_Sum < 5.6; Charge_B > 2.5 and < 3.5'''
Screened = []

for i in range(len(Charge_B_Exctracted)):
    if Charge_B_Exctracted.iloc[i]['BVS_B_Eval'] > 95 and Charge_B_Exctracted.iloc[i]['Radii_Sum'] < 5.6:
        Screened.append(Charge_B_Exctracted.iloc[i])

Results = pd.DataFrame(Screened).reset_index()
del Results['index']
Results.to_csv('9_Results.csv',index=True)

'''Time Calculation'''
time2 = time.time()
time_sum = time2 - time1
f_time = open('./time.txt','w',encoding='utf-8')
f_time.write('Total time: '+str(time_sum)+'s')
f_time.close()
print('Time:',time_sum,'s')