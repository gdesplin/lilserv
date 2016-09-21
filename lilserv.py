from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from datetime import datetime

def logPathTime(c):
	f = open('log.txt', 'a')
	f.write("Path: %s; Time: %s \n" % (c.path, BaseHTTPRequestHandler.date_time_string(c)))
	return

class MyServer(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content.Type', 'text/html')
		self.end_headers()
		query = parse_qs(urlparse(self.path).query)
		if self.path == "/chickens":
			self.wfile.write(bytes("<p>I like chickens<p>", "utf-8"))
			logPathTime(self)
		else:
			self.wfile.write(bytes("Hello", "utf-8"))
			logPathTime(self)
		return

	def do_POST(self):
		self.send_response(200)
		self.send_header('Content.Type', 'text/plain')
		self.end_headers
		length = int(self.headers[Content_Length])
		self.rfile.read(length).decode("utf-8")
		parsed_data = parse_qs(data)

def run():
	listen = ('127.0.0.1', 8080)
	server = HTTPServer(listen,MyServer)
	print ("Listening...")
	server.serve_forever()

run()
