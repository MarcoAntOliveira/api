# API
Respositorio destinaddo a desnvolvimento de apis em python
## desenvolvimento usanndo o modulo HTTP do python

```python
class SimpleHandler(BaseHTTPRequestHandler):
  # configuranddo resquest por path
  def do_GET(self):
    if self.path == "/":
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        data = f"""
        <html>
            <head> <h1> Olá mundo </h1> </head>
            <body>
            <p> Testando nosso servidor HTTP</p>
            <p> Diretório:{self.path} </p>
            </body>
        </html>
        """.encode()
        self.wfile.write(data)
    elif self.path == "/eventos/":
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        stylesheet = """
        <style>
          table{
            border-collapse: collapse;
          }

          td, th{
            border: 1px solid #dddd;
            text-allign: left;
            padding: 8px;
          }
        </style>

        """
        eventos  =  ""
        for evento in event_list:
          eventos += f"""
               <tr>
                  <th scope="row">{evento.id}</th>
                  <td>{evento.nome}</td>
                </tr>
          """
        data = f"""
        <html>
            <head>
            {stylesheet}
            </head>
            <table>
              <caption>
                Front-end events 2025
              </caption>
              <thead>
                <tr>
                  <th scope="col">ID</th>
                  <th scope="col">nome</th>
                </tr>
              </thead>
              <tbody>
                {eventos}
             </tbody>
            </table>
        </html>
        """.encode()
        self.wfile.write(data)
    elif self.path == "/api/eventos/":
      self.send_response(200)
      self.send_header("Content-Type", "application/json; charset=utf-8")
      self.end_headers()
      lista_dict_eventos =[]
      for ev in event_list:
        lista_dict_eventos.append({
          "id" : ev.id,
          "nome": ev.nome,
        })

      data = json.dumps(lista_dict_eventos)

      self.wfile.write(data.encode())
```

### modo debug
no terrminal digitar export FLASK_DEBUG 1
```shell
export FLASK_DEBUG 1
```
 No momento de build a aplicação

 ```shell
  FLASK_APP=main.py FLASK_DEBUG=1 flask run
 ```
