# Tarea 9
# Germán Jordi Arreortua Reyes

'''RegEx module '''
import re


# 1. Extraer el nombre de un archivo de una trayectoria del sistema de archivos
# P. ej. "$HOME/proyecto1/modulo5/programa3.py" -> "programa3.py"

nombre_del_archivo = re.match('.*/(.*)$', '$HOME/proyecto1/modulo5/programa3.py')
print(nombre_del_archivo.group(1))


# 2. Escribir la función date_in_spanish. Use re.sub para sustituir
# los nombres de los meses.
def date_in_spanish(date):
    """
        Translates a string date to spanish. That is, all references to months
        abbreviations like 'Jan', 'Feb', 'Mar' and so on are changed to 'Ene',
        'Feb', 'Mar', respectively.

        Parameters
        ----------
        date : str
            Date to be translated.

        Returns
        ------
            str
            The translated base_date.

        Examples
        --------
        >>> date_in_spanish("23-Apr-2021")
        23-Abr-2021
        >>> date_in_spanish("Dec-24-2020")
        Dic-24-2020
        """
    new_date = re.sub('Jan', 'Ene', date)
    new_date = re.sub('Apr', 'Abr', new_date)
    new_date = re.sub('Aug', 'Ago', new_date)
    new_date = re.sub('Dec', 'Dic', new_date)
    return new_date


print(date_in_spanish("23-Apr-2021"))
print(date_in_spanish("Dec-24-2020"))


# 3. Escribir la siguiente función
# def from_standard_equity_option_convention(code: str) -> dict:
def from_standard_equity_option_convention(code):
    """
        Transform a standard equity option convention code to record representation.

        Parameters
        ----------
        code : str
            Standard equity option convention code (see
            https://en.wikipedia.org/wiki/Option_naming_convention).

        Returns
        -------
            dict
            A dictionary containing:
            'symbol': Symbol name
            'expire': Option expiration base_date
            'right': Put (P) or Call (C).
            'strike': Option strike

        Examples:
        >>> from_standard_equity_option_convention('YHOO150416C00030000')
        {'symbol': 'YHOO', 'expire': '20150416', 'right': 'C', 'strike': 30.0}
        """
    datos = re.match(r'(\D{1,6})(\d{,6})([C,P])(\d{5})(\d{3})', code)
    diccionario = {'symbol': datos.group(1), 'expire': '20' + datos.group(2),
                   'right': datos.group(3),
                   'strike':  float(datos.group(4) + '.' + datos.group(5))}
    return diccionario


print(from_standard_equity_option_convention('YHOO150416C00030000'))


# 4. Explique con palabras qué hace la siguiente instrucción
# symbols_str = re.sub(r"'", "''", str(symbols))
# Respuesta
# Sustituye una comilla simple (') por dos comillas simples ('') en str(symbols)
# Ejemplo 1234'asd''wsa'ñ'* lo cambia por 1234''asd''''wsa''ñ''*
print(re.sub(r"'", "''", "1234'asd''wsa'ñ'*"))


# 5. Escriba una cadena 'account' apropiada para que se ejecute la
# instrucción print
# if re.match(r'DU[0-9]{7}', account):
#   print("Account: ", account)
# Respuesta
# account ='DU1324357'
ACCOUNT = 'DU1324357'
if re.match(r'DU[0-9]{7}', ACCOUNT):
    print("Account: ", ACCOUNT)


# 6. Escriba la expresión regular de manera más sintética pero preservando
# la funcionalidad.
# if re.match('^([0-9][0-9][0-9][0-9][0-9][0-9])$', text):
#   LOGGER.info("Correct OTP format: %s.", text)
# Respuesta
# Podemos cambiar '^([0-9][0-9][0-9][0-9][0-9][0-9])$' por '^(\d{6})$' ya que \d
# es la coincidencia basada en si el carácter es un dígito decimal.
# Así pues tendríamos lo siguiente
# if re.match('^(\d{6})$', text):
#   LOGGER.info("Correct OTP format: %s.", text)


# 7. ¿Cuál es el valor de 'reg_exp' que hace funcionar el código siguiente?
#   if re.match(reg_exp, text) is None:
#        error_message = \
#            "Try again, your answer does not correspond to a comma " + \
#            "separated integers list. Type something like '1, 2, 3' " + \
#            "without the apostrophes."
# Respuesta
# reg_exp='[0-9]+(,\s[0-9]+)*$' pues los enteros están separados por comas,
# además siguiendo el ejemplo: '1, 2, 3' hay un espacio después de las comas
# por lo cual pongo el metacarácter \s entre la coma y [0,9]
print(re.match(r'[0-9]+(,\s[0-9]+)*$', '123456, 242, 3'))


# 8. Programar el método siguiente.
# def collect_commission_adjustment(data):
def collect_commission_adjustment(data):
    """
        Retrieve a commision adjustment record from the section "Commission
        Adjustments" in one Interactive Brokers activity report.

        PARAMETERS
        ----------
        data : list[]
            Line from the activity report in the "Commission Adjustment" section
            in list format. That is, each element in the list is a comma
            separated item from the line.

        RETURNS
        -------
            dict
            Containing the open position information in dictionary format.

        Examples
        --------
        >>> collect_commission_adjustment(['Commission Adjustments', 'Data', 'USD',
        ... '2021-04-23',
        ... 'Commission Computed After Trade Reported (C     210430C00069000)',
        ... '-1.0906123', '\\n'])
        {'end_date': '20210423', 'symbol': 'C', 'expire': '20210430', \
    'right': 'C', 'strike': 69.0, 'sectype': 'OPT', 'amount': -1.0906123}
        >>> collect_commission_adjustment(
        ... ['Commission Adjustments', 'Data', 'USD', '2021-02-19',
        ... 'Commission Computed After Trade Reported (ALB)', '-0.4097', '\\n'])
        {'end_date': '20210219', 'symbol': 'ALB', 'sectype': 'STK', \
    'amount': -0.4097}
            """

    diccionario = {}
    diccionario['end_date'] = re.sub('-', '', data[3])
    commission_adj = re.match(r'Commission Computed After Trade Reported \(([A-Z]+)\)',
                              data[4])
    if commission_adj:
        diccionario['symbol'] = commission_adj.group(1)
        diccionario['sectype'] = 'STK'

    else:
        commission_adj = re.match(r'Commission Computed After Trade Reported'
                                  r' \(([A-Z]+)\s*(\d{6})(\D+)(\d{5})(\d{3})\)',
                                  data[4])
        diccionario['symbol'] = commission_adj.group(1)
        diccionario['expire'] = '20' + commission_adj.group(2)
        diccionario['rigth'] = commission_adj.group(3)
        diccionario['strike'] = float(commission_adj.group(4) + '.' + commission_adj.group(5))
        diccionario['sectype'] = 'OPT'
    diccionario['amount'] = data[5]
    return diccionario


f = ['Commission Adjustments', 'Data', 'USD', '2021-04-23',
     'Commission Computed After Trade Reported (C     210430C00069000)', '-1.0906123', '\\n']
g = ['Commission Adjustments', 'Data', 'USD', '2021-02-19',
     'Commission Computed After Trade Reported (ALB)', '-0.4097', '\\n']

print(collect_commission_adjustment(f))
print(collect_commission_adjustment(g))


# 9. De dos ejemplos de uso del siguiente método. En el primero el método debe
# regresar un número de punto flotante y en el segundo np.nan
# def banxico_value(tag, data):

# Parameters
#    tag : str
#        Internal tag name of the variable to retrieve.
#    data : str
#        Html page to locate the tag value.
#    Returns
#    --------
#        float
#        The associated tag value.
#    float_nt = "[^0-9-]*([-]*[0-9]+.[0-9]+)[^0-9]"
#    try:
#        res = float(re.search(tag + float_nt, data).group(1))
#    except AttributeError:
#        res = np.nan
#    return res
# Respuesta
# Un ejemplo en que devuelva un número de punto flotante es
# data = tag + 'Abc/Html-3.1416x', luego
# res = float(re.search(tag + float_nt, data).group(1)) = float(-3.1416)
# Un ejemplo donde nos devolvería np.nan es data = tag + 'abc'


# 10. Describa en palabras qué hace el siguiente código.
# col_sel = list(
#        map(
#            lambda s: s if re.match("[Ii][Mm][Ff][0-9]+", s) else None,
#            dat_df.columns,
#        ))
# col_sel = [c for c in col_sel if c is not None]
# print(col_sel)
# Respuesta
# A cada elemento de dat_df.columns, se le asigna el mismo elemento si coincide con la expresión
# [Ii][Mm][Ff][0-9]+, de los contario se le asignara None.
# Posteriormente se crea la lista col_sel con dichos valores.
# En la línea 226 lo que se hace es que se eliminan las entradas con valor None
# Así finalmente col_sel es una lista con los elementos de dat_df.columns
# que coinciden con la expresión [Ii][Mm][Ff][0-9]+.
