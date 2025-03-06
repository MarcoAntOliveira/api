from http.server import HTTPServer, BaseHTTPRequestHandler
from articles import Article1, Article2, Event1, Event2, Event3
import json

art1 = Article1()
art2 = Article2()
eve1  = Event1()
eve2  = Event2()
eve3  = Event3()

event_list = [eve1, eve2, eve3, eve1, eve2, eve3]

class SimpleHandler(BaseHTTPRequestHandler):
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




server = HTTPServer(('localhost', 8000), SimpleHandler)
server.serve_forever()
