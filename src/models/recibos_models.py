from config import cursor
import utils


def GenerarTickets(nivel, codigogrupo, periodo, mes):
    with cursor:
        cursor.execute(
            f"""SELECT
                    ALUMNOS_CXC.NUMEROALUMNO, 
                    ALUMNOS_CXC.REFERENCIA,  
                    ALUMNOS_CXC.CANTIDADPROGRAMADA, 
                    ALUMNOS_CXC.REFERENCIA2, 
                    ALUMNOS_CXC.MES,
                    ALUMNOS_GRUPOS.CODIGOGRUPO, 
                    ALUMNOS_GRUPOS.PERIODO, 
                    ALUMNOS.NOMBRE, 
                    ALUMNOS.MATERNO, 
                    ALUMNOS.PATERNO,
                    ALUMNOS.NIVEL,
                    ALUMNOS.CORREO_INSTITUCIONAL
                FROM (
                    (ALUMNOS_CXC INNER JOIN ALUMNOS_GRUPOS ON ALUMNOS_CXC.NUMEROALUMNO = ALUMNOS_GRUPOS.NUMEROALUMNO)
                        INNER JOIN ALUMNOS ON ALUMNOS_CXC.NUMEROALUMNO = ALUMNOS.NUMEROALUMNO)
                    WHERE ALUMNOS_GRUPOS.CODIGOGRUPO= '{codigogrupo}'
                    AND ALUMNOS.NIVEL = '{nivel}'
                    AND ALUMNOS_GRUPOS.PERIODO= {periodo}
                    AND ALUMNOS_CXC.PERIODO= {periodo}
                    AND ALUMNOS_CXC.MES = {mes} """
        )

        listHeaders = []
        listValues = []

        listHeaders = utils.FirebirdGetHeaders(cursor.description)
        listValues = utils.MergeHeadersValues(listHeaders, cursor.fetchall())

        cursor.execute(
            f"""SELECT 
                            SUBSTRING(CFGPAGOS_DET.PERIODO_INICIO FROM 1 FOR 10) AS PAGO_PRONTO,
                            SUBSTRING(CFGPAGOS_DET.PERIODO_FINAL FROM 1 FOR 10) AS PAGO_ATRASADO
                        FROM CFGPAGOS_DET 
                            WHERE CFGPAGOS_DET.PERIODO = {periodo} 
                            AND CFGPAGOS_DET.NIVEL = '{nivel}' 
                            AND CFGPAGOS_DET.MES = {mes} """
        )

        listHeadersPagos = []
        listValuesPagos = []

        listHeadersPagos = utils.FirebirdGetHeaders(cursor.description)
        listValuesPagos = utils.MergeHeadersValues(listHeadersPagos, cursor.fetchall())

        # print(listValuesPagos)

        listMergedValues = []

        for alumno in listValues:
            for fecha in listValuesPagos:
                listMergedValues.append(alumno | fecha)

        l = utils.RemoveDuplicateDicts(listMergedValues)
        l = utils.RemoveDictsWithNull(l)

        return l
