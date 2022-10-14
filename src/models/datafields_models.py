from datetime import datetime
from config import cursor


def SeleccionarCien():
    with cursor:
        try:
            # Ejecutamos la consulta
            cursor.execute(
                " SELECT FIRST 100 NOMBRE, PATERNO, NUMEROALUMNO FROM ALUMNOS"
            )

            # Obtenemos los encabezados de la tabla
            listHeaders = []
            for elemento in cursor.description:
                listHeaders.append(elemento[0])

            resultadoCursor = cursor.fetchall()

            # Guardamos los resultados
            resultado = []
            for item in resultadoCursor:
                dic = {}
                for indice, valor in enumerate(item):
                    dic[listHeaders[indice]] = valor
                resultado.append(dict(sorted(dic.items())))

            # Retornamos
            return resultado
        except Exception as e:
            print(e)
            return e


def CargarDataFields():
    with cursor:
        resultadoDataFields = {}

        # ? NIVELES --> Carreras
        # ! BUSCAR TABLA EN DONDE SOLO HAYA NIVELES
        cursor.execute("SELECT NIVEL FROM ALUMNOS")

        # cursor.description > (('ID', <class 'int'>), ('NOMBRE', <class 'str'>))
        # cursor.fetchall > [('C', 1972), ('Python', 1991)]

        # Obtenemos una lista de cabeceras
        listHeaders = []
        for elemento in cursor.description:
            listHeaders.append(elemento[0].lower())

        # Obtenemos una lista de todos los valores
        resultadoCursor = cursor.fetchall()
        listValues = []
        for valor in resultadoCursor:
            if valor[0] not in listValues:
                listValues.append(valor[0])

        # inicializar las cabeceras como arrays y asignamos los valores
        resultadoDataFields[listHeaders[0]] = listValues

        # ? CICLOS --> Ciclo: 2022/2023
        # ! SELECCIONO LOS QUE EMPIEZAN POR ESTE AÑO
        cursor.execute(
            f"SELECT CODIGO_CORTO, PERIODO FROM CICLOS WHERE CODIGO_CORTO LIKE '{datetime.now().year}%'"
        )
        # print(datetime.now().year)

        listHeaders = []
        for elemento in cursor.description:
            listHeaders.append(elemento[0].lower())

        resultadoCursor = cursor.fetchall()
        listValues = []

        for item in resultadoCursor:
            dic = {}
            for indice, valor in enumerate(item):
                dic[listHeaders[indice]] = valor
            listValues.append(dic)

        resultadoDataFields[listHeaders[0]] = listValues

        # ? MES
        listHeaders = ["mes"]
        listValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        resultadoDataFields[listHeaders[0]] = listValues

        # ? GRUPOS --> 1010 ARQ
        # ! BUSCAR TABLA EN DONDE SOLO HAYA GRUPOS
        cursor.execute("SELECT FIRST 200 CODIGOGRUPO FROM ALUMNOS_GRUPOS")
        # cursor.execute("SELECT CODIGOGRUPO FROM ALUMNOS_GRUPOS")

        listHeaders = []
        for item in cursor.description:
            listHeaders.append(item[0].lower())

        resultadoCursor = cursor.fetchall()
        listValues = []
        for valor in resultadoCursor:
            if valor[0] not in listValues:
                listValues.append(valor[0])

        resultadoDataFields[listHeaders[0]] = listValues

        return resultadoDataFields
