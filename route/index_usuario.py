from flask import redirect, render_template, Blueprint, url_for, session
from DAO.token_verificacao import verificar_session, verificar_integridade_token
from DAO.shows_request import shows_request
from DAO.meus_shows_request import listar_shows_usuario


index_usuario = Blueprint('index_usuario', __name__)

@index_usuario.route('/index/usuario', methods = ['GET'])
def index_usuario_generator():
    try:
        token = session['token']
        id = session['id_user']

        if verificar_session(token, id) == False or verificar_integridade_token(token, id) == False:
            return redirect(url_for('login.login_generator'))
        
        shows = shows_request()

        return render_template('index_main_usuario.html', shows=shows)
    
    except Exception as ex:
        print(f'erro11 {ex}')
        return redirect(url_for('login.login_generator'))

@index_usuario.route('/index/usuario/meusShows', methods = ['GET'])
def index_meus_shows_generator():
    try:
        token = session['token']
        id = session['id_user']

        if verificar_session(token, id) == False or verificar_integridade_token(token, id) == False:
            return redirect(url_for('login.login_generator'))
        
        meu_show = listar_shows_usuario(id)

        if meu_show:
            return render_template('index_meus_shows.html', meu_show=meu_show)
        else:
            sem_nada = "Você ainda não possui shows comprados!"
            print(sem_nada)
            return render_template('index_meus_shows.html', sem_nada=sem_nada)

    except Exception as ex:
        print(f'erro12 {ex}')
        return redirect(url_for('login.login_generator'))
        

@index_usuario.route('/logout', methods = ['GET'])
def index_usuario_logout():
    session.clear()
    return redirect(url_for('login.login_generator'))