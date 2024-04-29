import random

def port(): # Genera una lista de puertos
  randomPort = random.randint(1,65535)
  # scan = [i for i in range(65536)]
  port = [20,21,22,139,137,445,53,443,80,8080,8443,23,25,69,randomPort,443,80,8080,443,80,8080,443,80,8080,443,80,8080,443,80,8080,443,80,8080,443,80,8080,443,80,8080,443,80,8080,443,80,8080,443,80,8080,443,80,8080,443,80,8080,443,80,8080,21,22,21,22,randomPort] # Lista de puertos mas atacados y una probabilidad de puerto aleatorio teniendo que el 80, 8080 y 443 tienen mucho mas trafico
  
  portScan = port[random.randint(0,len(port)) - 1]
  return portScan

def originIp():
  ip = '192.168.' + str(random.randint(1,255)) + '.' + str(random.randint(1,255))
  return ip

def attempt(portAttempt):
  if portAttempt == 80 or portAttempt == 443 or portAttempt == 8080:
    attemptTry = 'aprobado'
  elif portAttempt == 20 or portAttempt == 21 or portAttempt == 22 or portAttempt == 23 or portAttempt == 25 or portAttempt == 53 or portAttempt == 69 or portAttempt == 137 or portAttempt == 139 or portAttempt == 445:
    attemptTry = 'rechazado'
  else:
    attemptTry = 'fallido'
  
  return attemptTry

def traffic(): # Simulador de trafico
  portAttempt = port()
  ip = originIp()
  
  
  traffic = {
    'port' : str(portAttempt),
    'origin' : str(ip),
    'status' : attempt(portAttempt),
    }
  return traffic

print(traffic())