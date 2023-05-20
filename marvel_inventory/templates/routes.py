from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from marvel_inventory.forms import HeroForm
from marvel_inventory.models import Hero, db

site = Blueprint('site', __name__, template_folder='site_templates')



@site.route('/')
def home():
    print("ooga booga in the terminal")
    return render_template('index.html')

@site.route('/profile', methods = ['GET','POST'])
@login_required
def profile():
    my_hero = HeroForm()

    try:
        if request.method == 'POST' and my_hero.validate_on_submit():
            descriptor = my_hero.descriptor.data
            hero_data = my_hero.hero_data.data
            user_token = current_user.token

            hero = Hero( descriptor, hero_data, user_token)
            # print(hero)
            db.session.add(hero)
            db.session.commit()

            return redirect(url_for('site.profile'))

    except:
        raise Exception('Hero not added, please check your form and try again!') 

    current_user_token = current_user.token

    heroes = Hero.query.filter_by(user_token=current_user_token)

    return render_template('profile.html', form=my_hero, heroes = heroes)


# @site.route('/hero_page')
# @login_required
# def hero_page():
    
#     return render_template('hero_page.html')