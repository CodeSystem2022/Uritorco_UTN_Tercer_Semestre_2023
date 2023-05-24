import logging as log
# docs.python.org/3/howto/logging.html

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s -- %(levelname)s -- [%(filename)s | línea: %(lineno)s]: %(message)s',
                datefmt='%D %I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug("Mensaje de debug")
    log.info("Mensaje de info")
    log.warning("Mensaje de warning")
    log.error("Mensaje de error")
    log.critical("Mensaje crítico")