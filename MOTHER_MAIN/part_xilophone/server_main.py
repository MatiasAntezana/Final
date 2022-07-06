from part_xilophone.server.server import MockXyloServer

xylophone = MockXyloServer(host='localhost', port=8080)

xylophone.start()