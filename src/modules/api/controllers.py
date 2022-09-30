from queue import Empty
from modules.database import cursor


def SelectAlumnosPrepa():
    """
    Hace una consulta a la base de datos, selecciona unicamente las filas que cumplan la condición NIVEL='PREPA' y retorna una lista de diccionarios
    {
        NUMEROALUMNO,
        NIVEL,
        PATERNO,
        MATERNO,
        NOMBRE,
        GRADO,
        MATRICULA
    }

    Returns:
        Array: Lista de diccionarios con los valores de alumnos
    """
    with cursor:
        try:

            cursor.execute(
                "SELECT NUMEROALUMNO, NIVEL, PATERNO, MATERNO, NOMBRE, GRADO, MATRICULA, EMAIL FROM ALUMNOS WHERE NIVEL = 'PREPA'"
            )
            resultado = []

            # Obtenemos las llaves cursor.description > (('ID', <class 'int'>), ('NOMBRE', <class 'str'>))
            listHeader = []
            for elemento in cursor.description:
                listHeader.append(elemento[0])

            # Obtenemos los valores cursor.fetchall > [('C', 1972), ('Python', 1991)]
            resultadoCursor = cursor.fetchall()
            for item in resultadoCursor:
                if item:  # Si existen items
                    dic = {}
                    for index, value in enumerate(item):
                        dic[listHeader[index]] = value
                    resultado.append(dic)

            return resultado
        except Exception as e:
            print(e)
            return e


def SelectCxC(alumno: dict):
    """
    Recibe un diccionario con la propiedad NUMEROALUMNO y hace una consulta a la base de datos a la tabla ALUMNOS_CXC obteniendo los valores relevantes con el filtro NUMEROALUMNO

    Args:
        alumno (Dictionary): Diccionario de alumno con la propiedad NUMEROALUMNO

    Returns:
        resultado(Dictionary) : Retorna un diccionario con los valores
        {
            INICIAL,
            FINAL,
            PERIODO,
            ANIO,
            MES,
            CANTIDADPROGRAMADA,
            FECHA_SP1,
            FECHA_SP2,
            REFERENCIA,
            REFERENCIA2,
            REFERENCIA3
        }
    """
    with cursor:
        try:
            resultado = {}
            cursor.execute(
                "SELECT INICIAL, FINAL, PERIODO, ANIO, MES, CANTIDADPROGRAMADA, FECHA_SP1, FECHA_SP2, REFERENCIA, REFERENCIA2, REFERENCIA3 FROM ALUMNOS_CXC WHERE NUMEROALUMNO = ?",
                [alumno["NUMEROALUMNO"]],
            )

            resultadoCursor = cursor.fetchall()

            if not resultadoCursor:
                # print("EMPTY")
                return

            listHeaders = []
            for item in cursor.description:
                listHeaders.append(item[0])

            for item in resultadoCursor:
                if item:
                    for indice, valor in enumerate(item):
                        resultado[listHeaders[indice]] = valor

            return resultado

        except Exception as e:
            print("EXCEPTION from modules>api>controllers.py>SelectCxC()", e)
            return e


def SelectNivel(arreglo):
    resultado = []

    for item in arreglo:
        cursor.execute(
            "SELECT NIVEL FROM ALUMNOS_NIVELES WHERE NUMEROALUMNO = ?",
            [item["NUMEROALUMNO"]],
        )

        listHeader = []
        for element in cursor.description:
            listHeader.append(element[0])

        for item in cursor.fetchall():
            if item:
                dic = {}
                for index, value in enumerate(item):
                    dic[listHeader[index]] = value
                resultado.append(dic)

    merged = []
    """ print(arreglo) """
    print(resultado)
    for index, value in enumerate(resultado):
        merg = value | arreglo[index]
        merged.append(merg)

    return merged
