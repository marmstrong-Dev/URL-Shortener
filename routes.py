from flask import render_template, request, redirect, url_for, Blueprint
from data import DataCon


def home():
    initCreator = DataCon
    initCreator.table_creation()

    return render_template('index.html')

def product():
    
    return render_template('product.html')
