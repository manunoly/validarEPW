from weasyprint import HTML, CSS
css = '''
        table {
            border-collapse: collapse;
            width: 80%;
            margin-left: auto;
            margin-right: auto;
        }

        td,
        th {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }'''

html = HTML(string='''
        <p style="text-align: right;"> Fecha del Reporte 01-01-2011</p>
    <div style="text-align: center;">
        <h2>Reporte de Información</h2>
        <h3>Empresa Cnel Gyquil</h3>
    </div>

    <table>
        <tr>
            <th colspan="2" style="text-align: center">Leyenda de Notificaciones</th>
        </tr>
        <tr>
            <td>Notificación tipo <b>1</b></td>
            <td>Notificaciónd de Energía reportada en 0.</td>
        </tr>
        <tr>
            <td>Notificación tipo <b>2</b></td>
            <td>Notificaciónd de Energía reportada negativa y no es tarifa de refacturación.</td>
        </tr>
        <tr>
            <td>Notificación tipo <b>3</b></td>
            <td>Notificaciónd de Factor de Potencia fuera del rango establecido entre 0 - 1.
            </td>
        </tr>
        <tr>
            <td>Notificación tipo <b>4</b></td>
            <td>Notificaciónd de Factor de Potencia calculado difiere del reportando</td>
        </tr>
    </table>
    <br>
    <table>
        <tr>
            <th colspan="4" style="text-align: center"> Notificaciones encontradas. </th>
        </tr>
        <tr>
            <th>Cuenta</th>
            <th>Medidor</th>
            <th>Fecha</th>
            <th>Notificación</th>
        </tr>
        <tr>
            <td>985609</td>
            <td>00-000092</td>
            <td>2017-05-01</td>
            <td>2</td>
        </tr>
        <tr>
            <td>3028149</td>
            <td>1001444194</td>
            <td>2017-05-01</td>
            <td>1</td>
        </tr>
    </table>
''')

html.write_pdf(
    'example.pdf',
    stylesheets=[CSS(string='''
        table {
            border-collapse: collapse;
            width: 80%;
            margin-left:auto;
            margin-right:auto;
        }

        td, th {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }''')])