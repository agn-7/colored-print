from colored_print import ColoredPrint


log = ColoredPrint()

log.success("Hello", 123, "Bye").store()
log.info("Hello", 123, "Bye")
log.warn("Hello", 123, "Bye")
log.err("Hello", 123, "Bye").store()
log.pink("Hello", 123, "Bye")
