from config import cursor

# alumnos_cxc.pagado
# alumnos.nombre, paterno, materno, nombres, periodo, nivel
def ObtenerCamposAlumno(numeroalumno):
    with cursor:
        cursor.execute(
            f"SELECT NUMEROALUMNO, PAGADO FROM ALUMNOS_CXC WHERE NUMEROALUMNO='{numeroalumno}'"
        )

        headersCxc = []
        valuesCxc = []

        for item in cursor.description:
            headersCxc.append(item[0].lower())

        for item in cursor.fetchall():
            dic = {}
            for indice, valor in enumerate(item):
                dic[headersCxc[indice]] = valor
            valuesCxc.append(dic)

        cursor.execute(
            f"SELECT NUMEROALUMNO, NOMBRE, PATERNO, MATERNO, NIVEL FROM ALUMNOS WHERE NUMEROALUMNO='{numeroalumno}'"
        )
        headersAlumno = []
        valuesAlumno = []

        for item in cursor.description:
            headersAlumno.append(item[0].lower())

        for item in cursor.fetchall():
            dic = {}
            for indice, valor in enumerate(item):
                dic[headersAlumno[indice]] = valor
            valuesAlumno.append(dic)

        merged = []
        for item in valuesAlumno:
            try:
                filtro = next(
                    alumno
                    for alumno in valuesCxc
                    if alumno["numeroalumno"] == item["numeroalumno"]
                )
                merged.append(item | filtro)
            except StopIteration:
                pass

        return merged
