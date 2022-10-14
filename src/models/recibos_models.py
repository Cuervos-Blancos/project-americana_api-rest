from operator import truediv
from config import cursor


def GenerarTickets(nivel, codigogrupo, periodo, mes):
    with cursor:

        # ? TABLA ALUMNOS
        cursor.execute(
            f"SELECT NUMEROALUMNO, NOMBRE, MATERNO, PATERNO FROM ALUMNOS WHERE NIVEL='{nivel}'"
        )
        headersAlumnos = []
        valuesAlumnos = []

        for item in cursor.description:
            headersAlumnos.append(item[0].lower())

        resultadoCursor = cursor.fetchall()
        if not resultadoCursor:
            return []
        for item in resultadoCursor:
            dic = {}
            for indice, valor in enumerate(item):
                dic[headersAlumnos[indice]] = valor
            valuesAlumnos.append(dic)

        # ? TABLA ALUMNOS_GRUPOS
        cursor.execute(
            f"SELECT NUMEROALUMNO, CODIGOGRUPO, PERIODO FROM ALUMNOS_GRUPOS WHERE CODIGOGRUPO='{codigogrupo}' AND PERIODO='{periodo}'"
        )
        headersAlumnosGrupos = []
        valuesAlumnosGrupos = []

        for item in cursor.description:
            headersAlumnosGrupos.append(item[0].lower())

        resultadoCursor = cursor.fetchall()
        if not resultadoCursor:
            return []
        for item in resultadoCursor:
            dic = {}
            for indice, valor in enumerate(item):
                dic[headersAlumnosGrupos[indice]] = valor
            valuesAlumnosGrupos.append(dic)

        # ? TABLA ALUMNOS_CXC
        cursor.execute(
            f"SELECT NUMEROALUMNO, REFERENCIA, FECHA_SP1, CANTIDADPROGRAMADA, REFERENCIA2, FECHA_SP2, MES FROM ALUMNOS_CXC WHERE MES ='{mes}' AND PERIODO='{periodo}'"
        )
        headersAlumnosCxc = []
        valuesAlumnosCxc = []

        for item in cursor.description:
            headersAlumnosCxc.append(item[0].lower())

        resultadoCursor = cursor.fetchall()
        if not resultadoCursor:
            return []
        for item in resultadoCursor:
            dic = {}
            for indice, valor in enumerate(item):
                dic[headersAlumnosCxc[indice]] = valor
            valuesAlumnosCxc.append(dic)

        # ? MERGES

        """ alum = list(
            filter(lambda per: per["NUMEROALUMNO"] == 10230, resultadoAlumnosGrupos)
        )
        print(alum) # ==> [{'INICIAL': 2020, 'FINAL': 2021, 'NUMEROALUMNO': 10230}, {'INICIAL': 2020, 'FINAL': 2021, 'NUMEROALUMNO': 10230}, {'INICIAL': 2021, 'FINAL': 2021, 'NUMEROALUMNO': 10230}, {'INICIAL': 2022, 'FINAL': 2022, 'NUMEROALUMNO': 10230}, {'INICIAL': 2022, 'FINAL': 2022, 'NUMEROALUMNO': 10230}, {'INICIAL': 2022, 'FINAL': 2022, 'NUMEROALUMNO': 10230}]

        alum = next(
            item for item in resultadoAlumnosGrupos if item["NUMEROALUMNO"] == 10230
        )
        print(alum)  # ==> {'INICIAL': 2020, 'FINAL': 2021, 'NUMEROALUMNO': 10230} """

        # * merged alumnos - alumnos_grupos
        mergedValues = []
        for item in valuesAlumnos:
            try:
                filtro = next(
                    alumno
                    for alumno in valuesAlumnosGrupos
                    if alumno["numeroalumno"] == item["numeroalumno"]
                )
                mergedValues.append(item | filtro)
            except StopIteration:
                pass

        if not mergedValues:
            return []

        # * merged alumnos-alumnos_grupos - alumnos_cxc
        ticketsValues = []
        for item in mergedValues:
            try:
                filtro = next(
                    alumno
                    for alumno in valuesAlumnosCxc
                    if alumno["numeroalumno"] == item["numeroalumno"]
                )
                ticketsValues.append(item | filtro)
            except StopIteration:
                pass

    return ticketsValues
