from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from psycopg2.extensions import AsIs
import pandas.io.sql as sqlio
import numpy as np
import pandas as pd
import psycopg2

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA
from fastapi.responses import JSONResponse

app = FastAPI()

conn = psycopg2.connect(
    host="cmdb-rr.cbo3ijdmzhje.ap-south-1.rds.amazonaws.com",
    database="cmdb",
    user="cm",
    password="cm")
cursor=conn.cursor()