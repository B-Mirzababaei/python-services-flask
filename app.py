#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
from flask_restful import Api
from config import create_app
from resources.warrant_detection.warrant import WARRANT
from resources.claim_detection.claim import CLAIM

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
api = Api(app)
print("global app")
##
# Actually setup the Api resource routing here
#
# TODO: Define Custom Error Messages
api.add_resource(CLAIM, '/v1/claim')  # first part is the class name in claim.py, the second part is url of request
api.add_resource(WARRANT, '/v1/warrant')

if __name__ == '__main__':
    app.run(debug=True, port=8030)
