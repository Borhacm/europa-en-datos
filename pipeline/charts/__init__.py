from . import comercio, ia, libertades, productividad

# Orden: por tema y, dentro de cada tema, por mirada
BUILDERS = [*ia.BUILDERS, *comercio.BUILDERS, *productividad.BUILDERS, *libertades.BUILDERS]
