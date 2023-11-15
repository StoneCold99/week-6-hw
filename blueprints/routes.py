from flask import blueprints, render_template



site = blueprints('site', __name__, template_folder='site_templates')


@site.route('/')
def shop():
    return render_template('shop.html')