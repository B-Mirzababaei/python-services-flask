from flask_restful import abort, request

# def abort_if_todo_doesnt_exist(todo_id):
#     if todo_id not in TODOS:
#         abort(404, message="To-do {} doesn't exist".format(todo_id))


# def get_image(url_field, file_field):
#     if url_field in request.form:
#         return request.form[url_field], False
#     else:
#         return request.files[file_field].read(), True
