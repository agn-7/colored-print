from colored_print import log


log.success("Hello", 123, "Bye").store()
log.info("Hello", 123, "Bye")
log.warn("Hello", 123, "Bye")
log.warning("Hello", 123, "Bye")
log.err("Hello", 123, "Bye").store(path='log.log')
log.error("Hello", 123, "Bye")
log.critical("Hello", 123, "Bye")
log.pink("Hello", 123, "Bye")
log.green("Hello", 123, "Bye")
log.red("Hello", 123, "Bye")
log.blue("Hello", 123, "Bye")
log.yellow("Hello", 123, "Bye")
log("Hello", 123, "Bye")
log.store("Hello", 123, "Bye", path='log.log')
