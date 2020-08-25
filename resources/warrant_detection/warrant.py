import traceback

from flask import current_app, request
from flask_restful import Resource, reqparse, abort
from pathlib import Path
from auth import auth
# import werkzeug

parser = reqparse.RequestParser()
# region global variables
global global_var_warrant
global_var_warrant = {'w1':"W1", 'w2':'W2'}
print("global global_var_warrant")
# endregion

# Recognize text from image
# by accepting either a filename or upload file stream
# TODO: Return minifed json result
class WARRANT(Resource):

    def __init__(self):
        pass
    @auth.login_required
    def post(self):
        global global_var_warrant

        print(global_var_warrant['c2'])

        # images_root_path = Path(current_app.config['IMAGES_ROOT'])
        # uploads_path = Path(images_root_path / 'uploads')
        # uploads_path.mkdir(parents=True, exist_ok=True)
        # allowed_extensions = {'png', 'jpg', 'jpeg'}  # 'pdf',
        # custom_tesseract_config = r'--oem 3 --psm 6'
        #
        # def allowed_file(filename):
        #     return '.' in filename and \
        #            filename.rsplit('.', 1)[1].lower() in allowed_extensions

        parser.add_argument('text', type=str, help='user\'s response')
        args = parser.parse_args()

        # lang = 'fas_np'
        # if args['lang']:
        #     lang = args['lang']

        # Handle relative image file path request
        if args['text']:

            lable = args['text']
            return {"lable": "ACT_HUMANLY"}, 200
            # if not text.is_absolute():
            #     image_absolute_path = images_root_path / Path(args['text'])
            # else:
            #     image_absolute_path = text
            #
            # if image_absolute_path.exists():
            #     # TODO: Parametric timeout
            #     text = pytesseract.image_to_string(Image.open(image_absolute_path), lang=lang, timeout=30,
            #                                        config=custom_tesseract_config)
            #     return {"text": text}, 200

            # else:
            #     abort(404, message="Image doesn't exist: {}".format(args['text']))

        # TODO: Need to validate the input and return appropriate response
        # Handle image upload request
        # img_uploaded = request.files['image']
        # if img_uploaded and allowed_file(img_uploaded.filename):
        #     image_filepath = Path(uploads_path / img_uploaded.filename)
        #     image_filepath.write_bytes(img_uploaded.read())
        #
        #     text = pytesseract.image_to_string(Image.open(image_filepath), lang=lang, timeout=30,
        #                                        config=custom_tesseract_config)
        #     return {"text": text}, 200
