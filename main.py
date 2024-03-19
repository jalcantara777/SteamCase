from fastapi import FastAPI, Query
import pandas as pd

app = FastAPI()

df_genres_PTG=pd.read_csv('Data4_FuncReturn2API/playtimeforever.csv')
df_genres_UFG=pd.read_csv('Data4_FuncReturn2API/UsersForGenre.csv')
df_years_URG =pd.read_csv('Data4_FuncReturn2API/usersrecforyear.csv')
df_years_UNRG=pd.read_csv('Data4_FuncReturn2API/usersnotrecforyear.csv')
df_years_SA  =pd.read_csv('Data4_FuncReturn2API/sentanalyforyear.csv')
df_games_RG5 =pd.read_csv('Data4_FuncReturn2API/RecGame5forUser.csv')

lst_genres   =df_genres_PTG.genre.to_list()
lst_games    =df_games_RG5.user_id.to_list()

@app.get('/')
def welcome_message():
    return "Bienvenido a la Aplicación de Recomendación de juegos del portal STEAM."

@app.get('/PlayTimeGenre')
def PlayTimeGenre(genero: str= Query(..., description=f"Ingrese desde las 3 primeras letras de los valores posibles de esta lista: {lst_genres}")):
    """
    Retorna el año de lanzamiento con más horas jugadas para el género ingresado como parámetro.
    
    NOTA.
    Si no ingresó la palabra completa correspondiente al género deseado, verifique que sea el que quería ya que puede haber coincidencia con otro género similar.
    """
    retyear =df_genres_PTG[df_genres_PTG.genre.str.lower().str.startswith(genero.lower())].maxplaytime_year.iloc[0]
    genre   =df_genres_PTG[df_genres_PTG.genre.str.lower().str.startswith(genero.lower())].genre.iloc[0]
    retval ="Año de lanzamiento con más horas jugadas para el Género "+genre.upper()+" : "+str(retyear)
    return retval

@app.get('/UserForGenre')
def UserForGenre(genero: str= Query(..., description=f"Ingrese desde las 3 primeras letras de los valores posibles de esta lista: {lst_genres}")):
    """
    Retorna el usuario que acumula más horas jugadas para el género ingresado como parámetro y una lista de la acumulación de horas jugadas por año.
    
    NOTA.
    Si no ingresó la palabra completa correspondiente al género deseado, verifique que sea el que quería ya que puede haber coincidencia con otro género similar.
    """
    retuser =df_genres_UFG[df_genres_UFG.genre.str.lower().str.startswith(genero.lower())].user.iloc[0]
    retlsth =df_genres_UFG[df_genres_UFG.genre.str.lower().str.startswith(genero.lower())].list_played_hours.iloc[0]
    genre   =df_genres_PTG[df_genres_PTG.genre.str.lower().str.startswith(genero.lower())].genre.iloc[0]
    retval ="Usuario con más horas jugadas para el Género "+genre.upper()+" : "+retuser+" , Horas jugadas: "+retlsth
    return retval

@app.get('/UsersRecommend')
def UsersRecommend(anio: int= Query(..., description="Ingrese el año, el cual debe estar entre el rango sólo en que se hicieron recomendaciones de los juegos: 2010-2016 ", ge=2010, le=2016)):
    """
    Retorna el top 3 de juegos MÁS recomendados por usuarios para el año dado.
    """
    retusrrg1=df_years_URG[df_years_URG.posted_year==anio].usrrec_game1.iloc[0]
    retusrrg2=df_years_URG[df_years_URG.posted_year==anio].usrrec_game2.iloc[0]
    retusrrg3=df_years_URG[df_years_URG.posted_year==anio].usrrec_game3.iloc[0]
    retval ='"Puesto 1" : '+retusrrg1+'"Puesto 2" : '+retusrrg2+'"Puesto 3" : '+retusrrg3
    return retval

@app.get('/UsersNotRecommend')
def UsersNotRecommend(anio: int= Query(..., description="Ingrese el año, el cual debe estar entre el rango sólo en que se hicieron revisiones de los juegos: 2010-2016 ", ge=2010, le=2016)):
    """
    Retorna el top 3 de juegos MENOS recomendados por usuarios para el año dado.
    """
    retusrnrg1=df_years_UNRG[df_years_UNRG.posted_year==anio].usrnrec_game1.iloc[0]
    retusrnrg2=df_years_UNRG[df_years_UNRG.posted_year==anio].usrnrec_game2.iloc[0]
    retusrnrg3=df_years_UNRG[df_years_UNRG.posted_year==anio].usrnrec_game3.iloc[0]
    retval ='{"Puesto 1" : '+retusrnrg1+'}, {"Puesto 2" : '+retusrnrg2+'} "Puesto 3" : '+retusrnrg3+'}'
    return retval

@app.get('/sentiment_analysis')
def sentiment_analysis(anio: int= Query(..., description="Ingrese el año, el cual debe estar entre el rango sólo en que se lanzaron los juegos: 1989-2017 ", ge=1989, le=2017)):
    """
    Retorna una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento para el año de lanzamiento dado.
    """
    retsentneg=df_years_UNRG[df_years_UNRG.release_year==anio].Negativo.iloc[0]
    retsentneu=df_years_UNRG[df_years_UNRG.release_year==anio].Neutro.iloc[0]
    retsentpos=df_years_UNRG[df_years_UNRG.release_year==anio].Positivo.iloc[0]
    retval ='Negative = '+retsentneg+'  Neutral = '+retsentneu+'  Positive = '+retsentpos
    return retval

@app.get('/recomendacion_usuario')
def recomendacion_usuario(userid: str= Query(..., description=f"Ingrese uno de los valores posibles de esta lista: {lst_games}")):
    """
    Retorna una lista con los 5 IDs de los juegos recomendados similares al ingresado.
    """
    retlst_rg5=df_games_RG5[df_games_RG5.user_id==userid].lst_rg5.iloc[0]
    return f"Lista con los 5 IDs de los juegos recomendados similares: {retlst_rg5}"
