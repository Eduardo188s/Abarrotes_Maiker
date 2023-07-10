from flask import Blueprint, render_template

error_views=Blueprint('error',__name__)

@error_views.errorhandler(404)
def page_not_fount(error):
    return render_template('error/404.html')