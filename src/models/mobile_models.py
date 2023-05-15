from config import cursor
import utils
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta


def ObtenerCamposAlumno(numeroalumno):
    # Obtenemos los meses y el periodo
    meses = ObtenerMeses()
    periodo = ObtenerPeriodo(numeroalumno)
    with cursor:
        cursor.execute(
            f"""SELECT
                    A.NOMBRE,
                    A.PATERNO,
                    A.MATERNO,
                    A.NOMBRETUTOR,
                    A.TELEFONO,
                    A.CELULAR,
                    B.NUMEROALUMNO,
                    B.PAGADO,
                    B.PERIODO,
                    B.MES
                FROM ALUMNOS A, ALUMNOS_CXC B
                WHERE A.NUMEROALUMNO = B.NUMEROALUMNO
                    AND A.NUMEROALUMNO={numeroalumno}
                    AND B.MES IN({meses})
                    AND B.PERIODO={periodo}"""
        )

        headers = utils.FirebirdGetHeaders(cursor.description)
        values = utils.MergeHeadersValues(headers, cursor.fetchall())

        alum = {}
        estado = []
        for dic in values:
            d = {}
            for k, v in dic.items():
                if k == "pagado" or k == "periodo" or k == "mes":
                    d[k] = v
                    continue
                else:
                    alum[k] = v

            estado.append(d)

        alum["colegiaturas"] = estado

        return alum

    with cursor:
        # ? TABLA ALUMNOS_CXC
        cursor.execute(
            f"SELECT NUMEROALUMNO, PAGADO FROM ALUMNOS_CXC WHERE NUMEROALUMNO='{numeroalumno}'"
        )

        headersCxc = utils.FirebirdGetHeaders(cursor.description)
        valuesCxc = utils.MergeHeadersValues(headersCxc, cursor.fetchall())

        # ? TABLA ALUMNOS
        cursor.execute(
            f"SELECT NUMEROALUMNO, NOMBRE, PATERNO, MATERNO, NIVEL FROM ALUMNOS WHERE NUMEROALUMNO='{numeroalumno}'"
        )

        headersAlumno = utils.FirebirdGetHeaders(cursor.description)
        valuesAlumno = utils.MergeHeadersValues(headersAlumno, cursor.fetchall())

        # MERGED
        merged = utils.MergedListsOfDicts(valuesCxc, valuesAlumno, "numeroalumno")

        return merged


def ObtenerPeriodo(numeroAlumno: int):
    """Obtenemos el maximo periodo actual a partir del numero del alumno"""

    # Obtenemos los meses
    meses = ObtenerMeses()

    # Ejecutamos la consulta
    with cursor:
        cursor.execute(
            f"SELECT MAX(PERIODO) FROM ALUMNOS_CXC WHERE NUMEROALUMNO='{numeroAlumno}' AND MES IN({meses})"
        )
        # print(cursor.fetchall()[0][0])

        return cursor.fetchall()[0][0]


def ObtenerMeses():
    """Regresa un string con el número del mes actual y los dos meses anteriores según está ordenado en la base de datos con sep = 1"""

    meses = {
        1: "5",
        2: "6",
        3: "7",
        4: "8",
        5: "9",
        6: "10",
        7: "11",
        8: "12",
        9: "1",
        10: "2",
        11: "3",
        12: "4",
    }

    m = datetime.now()
    meses_str = ""
    for i in range(3):
        meses_str = meses_str + meses[(m - relativedelta(months=i)).month] + ", "
    # print(meses_str[: len(meses_str) - 2])
    meses_str = meses_str[: len(meses_str) - 2]

    # revisar doc https://how.okpedia.org/es/python/como-extraer-elementos-de-la-lista-de-python

    return meses_str
