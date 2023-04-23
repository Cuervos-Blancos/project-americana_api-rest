from datetime import datetime
from config import cursor
import utils

def CargarCiclos():
    # ? CICLOS --> Ciclo: 2022/2023
    # ! SELECCIONO LOS QUE EMPIEZAN POR ESTE AÑO
    try:
        with cursor:
            #   Ejecutamos la consulta
            """cursor.execute(
                f"SELECT CODIGO_CORTO, PERIODO FROM CICLOS WHERE CODIGO_CORTO LIKE '{datetime.now().year}%'"
            )"""

            cursor.execute(
                f"SELECT CODIGO_CORTO, PERIODO FROM CICLOS WHERE CODIGO_CORTO LIKE '2022%'"
            )

            listHeaders = utils.FirebirdGetHeaders(cursor.description)
            listValues = utils.MergeHeadersValues(listHeaders, cursor.fetchall())

            return listValues
    except Exception as e:
        print(e)
        return "error"


def CargarCarreras(periodo):
    # ? NIVELES --> Carreras
    # ! BUSCAR TABLA EN DONDE SOLO HAYA NIVELES
    with cursor:
        cursor.execute(f"SELECT DISTINCT NIVEL FROM GRUPOS WHERE PERIODO = {periodo}")

        listHeaders = utils.FirebirdGetHeaders(cursor.description)
        listValues = utils.MergeHeadersValues(listHeaders, cursor.fetchall())

        return listValues


def CargarGrupos(periodo, nivel):
    # ? GRUPOS --> 1010 ARQ
    with cursor:
        cursor.execute(
            f"SELECT CODIGOGRUPO FROM GRUPOS WHERE PERIODO = {periodo} AND NIVEL = '{nivel}'"
        )

        listHeaders = utils.FirebirdGetHeaders(cursor.description)
        listValues = utils.MergeHeadersValues(listHeaders, cursor.fetchall())

        return listValues


def CargarMeses():
    resultadoDataFields = {}

    listHeaders = ["mes"]
    listValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    resultadoDataFields[listHeaders[0]] = listValues

    return resultadoDataFields
