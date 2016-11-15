fp = open('park.dot', 'rb')
buf = fp.read()
fp.close()
buf = buf[3:]
fp = open('park.dot', 'wb')
fp.write(buf)
fp.close()

