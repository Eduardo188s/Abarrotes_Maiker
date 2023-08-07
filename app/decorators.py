from flask import request, session, redirect,url_for

from functools import wraps
from models.menu_roles  import Menu_roles
from models.menus import Menus


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        ruta = request.path
        menu_rol =[]
        menus = []

        menus = Menus.get_all()
        beter= filter(lambda x: x.ruta == ruta, menus)
        beter = list(beter)
        
        print("Ruta->" + ruta)

        for o in beter:
            print("Imprimiendo un menu")
            print(o)
        if not "name" in session:
            print("Sin sesion")
            
            menu_rol =  Menu_roles.get(3)
        else:
            print("Con sesion")
            menu_rol =  Menu_roles.get(session.get("role"))
        
        print(session.get("role"))
        menus_encontrado =filter(lambda x: x.ruta == ruta, menus)
        
        menus_encontrado  = list(menus_encontrado)

        if len(menus_encontrado) > 0:
            print("Imprimiendo los menus con rol")
            print(ruta)
            menu_en = filter(lambda x: x.ruta ==  ruta ,  menu_rol) 
            menu_en = list(menu_en)

            print(menu_en)

            if len(menu_en) == 0 :
                return redirect(url_for('user.login', next=request.path))

            
       
        return f(*args, **kwargs)

    return wrapper