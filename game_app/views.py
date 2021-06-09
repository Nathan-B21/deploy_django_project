from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Knight, Rogue, Mage, Enemy
import bcrypt
import math
def index(request):
    return render(request, "index.html")

def register(request):
    errors = User.objects.registration_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            if key == 'first_name':
                messages.error(request, value, extra_tags='first_name')
            if key == 'last_name':
                messages.error(request, value, extra_tags='last_name')
            if key == 'reg_email':
                messages.error(request, value, extra_tags='reg_email')
            if key == 'reg_password':
                messages.error(request, value, extra_tags='reg_password')
            if key == 'confirm_pw':
                messages.error(request, value, extra_tags='confirm_pw')
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        hashed_password = bcrypt.hashpw(request.POST['reg_password'].encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['reg_email'],
            password = hashed_password
            )
        request.session['user_id'] = user.id
        return redirect('/charactercreation')

def login(request):
    errors = User.objects.login_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            if key == 'log_email':
                messages.error(request, value, extra_tags='log_email')
            if key == 'log_password':
                messages.error(request, value, extra_tags='log_password')
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        user_list = User.objects.filter(email=request.POST['log_email'])
        if len(user_list) == 0:
            messages.error(request, 'We could not find a user with that email address', extra_tags='log_email')
            return redirect('/')
        else:
            user = user_list[0]
            if bcrypt.checkpw(request.POST['log_password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id
                return redirect(f'/home/{user.id}')
            else:
                messages.error(request, 'Your password was incorrect.',
                extra_tags='log_password')
                return redirect('/')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        context = {
            'user': User.objects.get(id=request.session['user_id'])
        }
        return render(request, "charactercreation.html", context)
    
def create_character(request):
    if request.POST['form_select'] == 'knight':
        print("***************************")
        errors = Knight.objects.character_creation_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                if key == 'character_name':
                    messages.error(request, value, extra_tags='character_name')
                if key == 'form_select':
                    messages.error(request, value, extra_tags='form_select')
            # redirect the user back to the form to fix the errors
            return redirect('/charactercreation')
        else:
            # creation of a knight object
            user_character = Knight.objects.create(
                character_name = request.POST['character_name'],
                max_health = 15,
                health = 15,
                max_attack = 3,
                attack = 3,
                # user = request.session["user_id"]
                user = User.objects.get(id=request.session['user_id'])
            )
            user = User.objects.get(id=request.session['user_id'])

            return redirect(f"/home/{user.id}") #render or redirect???? Do I need context?
        
    elif request.POST['form_select'] == "rogue":
        errors = Rogue.objects.character_creation_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                if key == 'character_name':
                    messages.error(request, value, extra_tags='character_name')
                if key == 'form_select':
                    messages.error(request, value, extra_tags='form_select')
            # redirect the user back to the form to fix the errors
            return redirect('/charactercreation')
        else:
            # Creation of a Rogue Object
            user_character = Rogue.objects.create(
                character_name = request.POST['character_name'],
                max_health = 11,
                health = 11,
                max_attack = 5,
                attack = 5,
                # user = request.session["usr_id"]
                user = User.objects.get(id=request.session['user_id'])
            )
            user = User.objects.get(id=request.session['user_id'])
            return redirect(f'/home/{user.id}') # render or redirect? Do I need context?
        
    elif request.POST['form_select'] == "mage":
        errors = Mage.objects.character_creation_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                if key == 'character_name':
                    messages.error(request, value, extra_tags='character_name')
                if key == 'form_select':
                    messages.error(request, value, extra_tags='form_select')
            # redirect the user back to the form to fix the errors
            return redirect('/charactercreation')
        else:
            # Creation of a Mage Object
            user_character = Mage.objects.create(
                character_name = request.POST['character_name'],
                max_health = 8,
                health = 8,
                max_attack = 10,
                attack = 10,
                max_magic = 10,
                magic = 10,
                # user = request.session["user_id"]
                user = User.objects.get(id=request.session['user_id'])
            )
            user = User.objects.get(id=request.session['user_id'])
            return redirect(f'/home/{user.id}') #render or redirect??? Do i need context???

def logout(request):
    request.session.flush()
    return redirect('/')









def home_page(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
        
        }
    return render(request, "home.html", context)

def forest_page(request,user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, "forest.html", context)







def forest_battle_page(request,user_id):
    # testing = Enemy.objects.get(id=request.session['enemy_id'])
    # print("testing", testing.health, testing.id )
    # print("enemy id",request.session['enemy_id'] )
    # del request.session['player_health_bar']
    # if player.knight{
    #     request.session['player_health_bar'] = user.knight.health
    # }
    if 'activities' not in request.session:
        request.session['activities'] = []
    if 'player_health_bar' not in request.session:
        new_enemy = Enemy.objects.create(enemy_name = "Bandit", max_health=20, health = 20, max_attack = 2, attack = 2)
        request.session['enemy_id'] = new_enemy.id
        request.session['player_health_bar'] = 100
        request.session['enemy_health_bar'] = 100
    context = {
        'user': User.objects.get(id=user_id),
        'enemy': Enemy.objects.get(id=request.session['enemy_id']),
        # 'health_bar': 70
    }
    return render(request, "forest_battle_scene.html", context)


def attack(request, user_id):
    if 'activities' not in request.session:
        request.session['activities'] = []
    new_enemy = Enemy.objects.get(id=request.session['enemy_id'])

    player = User.objects.get(id=request.session['user_id'])
    if new_enemy.health <= 0:
        print("Enemy slain")
        del request.session['enemy_health_bar']
        del request.session['player_health_bar']
        request.session['activities'].append(f"{new_enemy.enemy_name} was defeated")
        return redirect(f"/win/{player.id}")
    if player.knight:
        if player.knight.health <= 0:
            print("you died")
            del request.session['enemy_health_bar']
            del request.session['player_health_bar']
            return redirect(f"/lose/{player.id}")
            request.session['activities'].append(f"{player.knight.character_name} was defeated") #move to lose page
        else:
            print("enemy health in post method before", new_enemy.health, new_enemy.id)
            new_enemy.health = new_enemy.health - player.knight.attack
            request.session['activities'].append(f"{player.knight.character_name} hit {new_enemy.enemy_name} for 3 damage")
            new_enemy.save()
            if new_enemy.health <= 0:
                return redirect(f"/win/{player.id}")
                
            print("enemy health in post method after", new_enemy.health)
            request.session['enemy_health_bar'] = math.floor((new_enemy.health/new_enemy.max_health) * 100)
            player.knight.health = player.knight.health - new_enemy.attack
            request.session['activities'].append(f"{new_enemy.enemy_name} hit {player.knight.character_name} for 2 damage")
            player.save()
            print('player_health:', player.knight.health)
            if player.knight.health <= 0:
                return redirect(f"lose/{player.id}") #PLAYER LOSE PAGE NOT MADE YET
            print(request.session['enemy_health_bar'])
            request.session['player_health_bar'] = math.floor((player.knight.health/player.knight.max_health) * 100) #Math.floor
            print(request.session['player_health_bar'])
            print("enemy health in post method after", new_enemy.health)
            return redirect(f"/forest_battle_scene/{player.id}")
    elif player.rogue:
        if player.rogue.health == 0:
            print("you died!")
        else:
            new_enemy.health = new_enemy.health - player.rogue.attack
            new_enemy.save()
            
            request.session['enemy_health_bar'] = math.floor((new_enemy.health/new_enemy.max_health) * 100)
            
            player.rogue.health = player.rogue.health - new_enemy.attack
            player.save()
            request.session['player_health_bar'] = math.floor((player.rogue.health/player.rogue.max_health) * 100)
            
            return redirect(f"/forest_battle_scene/{player.id}")
    elif player.mage:
        if player.mage.health == 0:
            print("you died!")
        else:
            new_enemy.health = new_enemy.health - player.mage.attack
            new_enemy.save()
            request.session['enemy_health_bar'] = math.floor((new_enemy.health/new_enemy.max_health) * 100)
            
            player.mage.health = player.mage.health - new_enemy.attack
            player.save()
            request.session['player_health_bar'] = math.floor((player.mage.health/player.mage.max_health) * 100)
            
            return redirect(f"/forest_battle_scene/{player.id}")

def win_page(request, user_id):
    player = User.objects.get(id=request.session['user_id'])
    context = {
        'user': User.objects.get(id=user_id)
    }
    request.session['activities'].append(f"{player.knight.character_name} has won the battle") 
    return render(request, "win_page.html", context)




