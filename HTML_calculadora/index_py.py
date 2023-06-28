import sqlite3

# Connect to the database
conn = sqlite3.connect('deudor.db')
cursor = conn.cursor()

# Retrieve deudor data from the database
cursor.execute('SELECT * FROM deudor')
deudor_data = cursor.fetchall()

# Close the database connection
conn.close()

# Generate the HTML table dynamically
table_html = '<table>\n'
table_html += '  <thead>\n'
table_html += '    <tr>\n'
table_html += '      <th>Id</th>\n'
table_html += '      <th>Nombre</th>\n'
table_html += '      <th>Monto</th>\n'
table_html += '    </tr>\n'
table_html += '  </thead>\n'
table_html += '  <tbody>\n'
for deudor in deudor_data:
    table_html += '    <tr>\n'
    table_html += f'      <td>{deudor[0]}</td>\n'  # Assuming deudor name is in the first column
    table_html += f'      <td>{deudor[1]}</td>\n'  # Assuming deudor amount is in the second column
    table_html += f'      <td>{deudor[2]}</td>\n'  # Assuming deudor contact is in the third column
    table_html += '    </tr>\n'
table_html += '  </tbody>\n'
table_html += '</table>'

# Create the HTML file
html_content = f'''
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
  <title>Deudores</title>
</head>
<body>
  <h1>Lista de deudores</h1>

  {table_html}
</body>
</html>
'''

with open('lista_deudores.html', 'w') as file:
    file.write(html_content)
