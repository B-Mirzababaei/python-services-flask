#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
from flask_restful import reqparse, Api
from config import create_app
from resources.ocr import OCR
from resources.warrant import WARRANT

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
api = Api(app)

##
# Actually setup the Api resource routing here
#
# TODO: Define Custom Error Messages
api.add_resource(OCR, '/ocr')
api.add_resource(WARRANT, '/warrant')

if __name__ == '__main__':
    app.run(debug=True, port=8030)
