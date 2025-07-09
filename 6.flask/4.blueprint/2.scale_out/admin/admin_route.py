from flask import render_template, Blueprint

admin_bp = Blueprint('admin', __name__, template_folder='../templates/admin')

@admin_bp.route('/')
def admin_page():
    return render_template('admin.html')